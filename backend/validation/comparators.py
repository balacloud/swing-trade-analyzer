"""
Data Comparator for Validation Engine
Compares our data against external sources with tolerance checking

Day 15: Validation comparison logic
"""

from typing import Dict, Optional
from datetime import datetime
from dataclasses import dataclass
from enum import Enum


class ValidationStatus(Enum):
    PASS = "pass"
    FAIL = "fail"
    WARNING = "warning"
    SKIP = "skip"


@dataclass
class ValidationResult:
    """Single validation comparison result"""
    ticker: str
    metric: str
    our_value: Optional[float]
    external_value: Optional[float]
    external_source: str
    variance_pct: Optional[float]
    tolerance_pct: float
    status: ValidationStatus
    timestamp: str
    notes: str = ""


class DataComparator:
    """
    Compares data values with tolerance-based validation.
    """
    
    def __init__(self, tolerances: Dict[str, float]):
        """
        Initialize comparator with tolerance settings.
        
        Args:
            tolerances: Dict mapping metric names to tolerance percentages (as decimals)
        """
        self.tolerances = tolerances
        self.default_tolerance = 0.10  # 10% default
    
    def compare(
        self,
        ticker: str,
        metric: str,
        our_value: Optional[float],
        external_value: Optional[float],
        external_source: str,
        tolerance_key: str = None,
        custom_tolerance: float = None
    ) -> Optional[ValidationResult]:
        """
        Compare our value against external value with tolerance.
        
        Args:
            ticker: Stock ticker
            metric: Name of the metric being compared
            our_value: Our calculated/fetched value
            external_value: Value from external source
            external_source: Name of external source
            tolerance_key: Key to look up tolerance in self.tolerances
            custom_tolerance: Override tolerance (as decimal, e.g., 0.05 for 5%)
            
        Returns:
            ValidationResult or None if comparison not possible
        """
        timestamp = datetime.now().isoformat()
        
        # Determine tolerance
        if custom_tolerance is not None:
            tolerance = custom_tolerance
        elif tolerance_key and tolerance_key in self.tolerances:
            tolerance = self.tolerances[tolerance_key]
        else:
            tolerance = self.default_tolerance
        
        tolerance_pct = tolerance * 100
        
        # Handle missing values
        if our_value is None and external_value is None:
            return ValidationResult(
                ticker=ticker,
                metric=metric,
                our_value=None,
                external_value=None,
                external_source=external_source,
                variance_pct=None,
                tolerance_pct=tolerance_pct,
                status=ValidationStatus.SKIP,
                timestamp=timestamp,
                notes="Both values missing"
            )
        
        if our_value is None:
            return ValidationResult(
                ticker=ticker,
                metric=metric,
                our_value=None,
                external_value=external_value,
                external_source=external_source,
                variance_pct=None,
                tolerance_pct=tolerance_pct,
                status=ValidationStatus.WARNING,
                timestamp=timestamp,
                notes="Our value missing"
            )
        
        if external_value is None:
            return ValidationResult(
                ticker=ticker,
                metric=metric,
                our_value=our_value,
                external_value=None,
                external_source=external_source,
                variance_pct=None,
                tolerance_pct=tolerance_pct,
                status=ValidationStatus.SKIP,
                timestamp=timestamp,
                notes="External value not available"
            )
        
        # Calculate variance
        if external_value == 0:
            # Can't calculate percentage variance if external is 0
            if our_value == 0:
                variance_pct = 0
                status = ValidationStatus.PASS
                notes = "Both values are 0"
            else:
                variance_pct = None
                status = ValidationStatus.WARNING
                notes = "External value is 0, can't calculate variance"
        else:
            variance_pct = abs(our_value - external_value) / abs(external_value) * 100
            
            # Determine status based on tolerance
            if variance_pct <= tolerance_pct:
                status = ValidationStatus.PASS
                notes = f"Within tolerance ({variance_pct:.1f}% <= {tolerance_pct:.1f}%)"
            elif variance_pct <= tolerance_pct * 1.5:
                status = ValidationStatus.WARNING
                notes = f"Near tolerance ({variance_pct:.1f}% vs {tolerance_pct:.1f}%)"
            else:
                status = ValidationStatus.FAIL
                notes = f"Exceeds tolerance ({variance_pct:.1f}% > {tolerance_pct:.1f}%)"
        
        return ValidationResult(
            ticker=ticker,
            metric=metric,
            our_value=round(our_value, 4) if our_value else None,
            external_value=round(external_value, 4) if external_value else None,
            external_source=external_source,
            variance_pct=round(variance_pct, 2) if variance_pct is not None else None,
            tolerance_pct=tolerance_pct,
            status=status,
            timestamp=timestamp,
            notes=notes
        )
    
    def compare_logic(
        self,
        ticker: str,
        metric: str,
        condition: bool,
        description: str,
        our_value: Optional[float] = None,
        reference_value: Optional[float] = None
    ) -> ValidationResult:
        """
        Create a logic-based validation result (not tolerance-based).
        
        Args:
            ticker: Stock ticker
            metric: Name of the check
            condition: Boolean result of the logic check
            description: Human-readable description of what was checked
            our_value: Optional value being checked
            reference_value: Optional reference value
            
        Returns:
            ValidationResult
        """
        return ValidationResult(
            ticker=ticker,
            metric=metric,
            our_value=our_value,
            external_value=reference_value,
            external_source="Logic Check",
            variance_pct=None,
            tolerance_pct=0,
            status=ValidationStatus.PASS if condition else ValidationStatus.FAIL,
            timestamp=datetime.now().isoformat(),
            notes=description
        )
