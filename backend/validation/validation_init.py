"""
Validation Engine Package for Swing Trade Analyzer
Day 15: Data Validation + Forward Testing Framework
"""

from .engine import ValidationEngine, ValidationReport, ValidationStatus
from .scrapers import YahooFinanceScraper, FinvizScraper
from .comparators import DataComparator, ValidationResult
from .forward_tracker import ForwardTestTracker, SignalType, SignalOutcome

__all__ = [
    'ValidationEngine',
    'ValidationReport', 
    'ValidationStatus',
    'YahooFinanceScraper',
    'FinvizScraper',
    'DataComparator',
    'ValidationResult',
    'ForwardTestTracker',
    'SignalType',
    'SignalOutcome',
]
