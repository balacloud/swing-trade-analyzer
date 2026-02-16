"""
Validation Engine for Swing Trade Analyzer
Day 15: Data Validation + Forward Testing Framework
Day 16: Fixed pass rate calculation, replaced Yahoo with StockAnalysis

This module validates our API data against external sources
and tracks forward test signals for backtesting.

Sources:
- Our API: localhost:5001
- StockAnalysis: Primary source for price/52-week data (Day 16)
- Finviz: Scraped for fundamental cross-check (ROE, D/E)
"""

import requests
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import sqlite3

# Import scrapers
from .scrapers import YahooFinanceScraper, FinvizScraper, StockAnalysisScraperWrapper
from .comparators import DataComparator, ValidationStatus
from .report_generator import HTMLReportGenerator


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


@dataclass
class TickerValidation:
    """Complete validation for one ticker"""
    ticker: str
    timestamp: str
    overall_status: ValidationStatus
    pass_count: int
    fail_count: int
    warning_count: int
    skip_count: int  # Track skipped validations
    results: List[ValidationResult]


@dataclass
class ValidationReport:
    """Complete validation report"""
    run_id: str
    timestamp: str
    tickers: List[str]
    overall_pass_rate: float
    coverage_rate: float  # What % of checks had data
    accuracy_rate: float  # Of checks with data, what % passed
    ticker_results: List[TickerValidation]
    summary: Dict


class ValidationEngine:
    """
    Main validation engine that orchestrates data validation
    against external sources.
    """
    
    # Default test tickers
    DEFAULT_TICKERS = ['AAPL', 'NVDA', 'JPM', 'MU', 'COST']
    
    # Our API base URL
    API_BASE = 'http://localhost:5001/api'
    
    # Validation tolerances (as decimal, e.g., 0.05 = 5%)
    # Day 54: Updated for v4.14 multi-source providers (was Defeat Beta)
    # - Our providers (Finnhub/FMP/yfinance) vs external (Finviz/StockAnalysis)
    # - Growth rates: our providers return DECIMAL (0.15), Finviz returns PERCENTAGE (15.0)
    #   → we normalize (×100) before comparing, so tolerance can be tighter now
    # - Debt/Equity: providers may use total debt vs long-term only
    TOLERANCES = {
        'price': 0.02,           # 2% for prices (delayed data)
        'roe': 0.20,             # 20% - calculation methodology varies
        'eps_growth': 0.25,      # 25% for EPS growth (timing + methodology)
        'revenue_growth': 0.25,  # 25% (was 85% — units bug fixed Day 54)
        'pe_ratio': 0.10,        # 10% for P/E ratio
        'debt_equity': 0.50,     # 50% - total debt vs long-term only
        '52w_high': 0.01,        # 1% for 52-week high
        '52w_low': 0.01,         # 1% for 52-week low
    }
    
    def __init__(self, tickers: List[str] = None, results_dir: str = None):
        """
        Initialize validation engine.
        
        Args:
            tickers: List of tickers to validate (default: DEFAULT_TICKERS)
            results_dir: Directory to store results (default: validation_results/)
        """
        self.tickers = tickers or self.DEFAULT_TICKERS
        self.results_dir = results_dir or os.path.join(
            os.path.dirname(__file__), '..', 'validation_results'
        )
        
        # Ensure results directory exists
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Initialize scrapers
        # Day 16: Using StockAnalysis as primary (Yahoo is broken)
        self.stockanalysis_scraper = StockAnalysisScraperWrapper()
        self.yahoo_scraper = YahooFinanceScraper()  # Kept as fallback
        self.finviz_scraper = FinvizScraper()
        
        # Initialize comparator
        self.comparator = DataComparator(self.TOLERANCES)
        
        # Initialize report generator
        self.report_generator = HTMLReportGenerator()
        
        # Results storage
        self.results: List[ValidationResult] = []
    
    def run_validation(self) -> ValidationReport:
        """
        Run full validation suite for all tickers.
        
        Returns:
            ValidationReport with all results
        """
        run_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        timestamp = datetime.now().isoformat()
        
        print(f"\n{'='*60}")
        print(f"🔍 VALIDATION ENGINE - Run {run_id}")
        print(f"{'='*60}")
        print(f"Tickers: {', '.join(self.tickers)}")
        print(f"Timestamp: {timestamp}")
        print(f"{'='*60}\n")
        
        ticker_results = []
        total_pass = 0
        total_fail = 0
        total_warning = 0
        total_skip = 0
        
        for ticker in self.tickers:
            print(f"\n📊 Validating {ticker}...")
            ticker_validation = self._validate_ticker(ticker)
            ticker_results.append(ticker_validation)
            
            total_pass += ticker_validation.pass_count
            total_fail += ticker_validation.fail_count
            total_warning += ticker_validation.warning_count
            total_skip += ticker_validation.skip_count
            
            # Print summary for this ticker
            status_emoji = {
                ValidationStatus.PASS: "✅",
                ValidationStatus.FAIL: "❌",
                ValidationStatus.WARNING: "⚠️"
            }
            print(f"   {status_emoji.get(ticker_validation.overall_status, '❓')} "
                  f"{ticker}: {ticker_validation.pass_count} pass, "
                  f"{ticker_validation.fail_count} fail, "
                  f"{ticker_validation.warning_count} warning, "
                  f"{ticker_validation.skip_count} skip")
        
        # =============================================
        # Proper metric calculations (Day 16 fix)
        # =============================================
        total_checks = total_pass + total_fail + total_warning + total_skip
        total_validated = total_pass + total_fail + total_warning
        
        # Coverage: What % of checks actually had data to compare
        coverage_rate = (total_validated / total_checks * 100) if total_checks > 0 else 0
        
        # Accuracy: Of checks WITH data, what % passed
        accuracy_rate = (total_pass / total_validated * 100) if total_validated > 0 else 0
        
        # Overall Quality: Coverage × Accuracy (the TRUE health metric)
        overall_quality = (coverage_rate * accuracy_rate) / 100
        
        # Legacy pass_rate for backward compatibility
        overall_pass_rate = accuracy_rate
        
        # Create report
        report = ValidationReport(
            run_id=run_id,
            timestamp=timestamp,
            tickers=self.tickers,
            overall_pass_rate=round(overall_pass_rate, 1),
            coverage_rate=round(coverage_rate, 1),
            accuracy_rate=round(accuracy_rate, 1),
            ticker_results=ticker_results,
            summary={
                'total_checks': total_checks,
                'validated': total_validated,
                'skipped': total_skip,
                'passed': total_pass,
                'failed': total_fail,
                'warnings': total_warning,
                'coverage_rate': round(coverage_rate, 1),
                'accuracy_rate': round(accuracy_rate, 1),
                'quality_score': round(overall_quality, 1),
                'pass_rate': round(accuracy_rate, 1)
            }
        )
        
        # Save results
        self._save_results(report)
        
        # Generate HTML report
        html_path = self.report_generator.generate(report, self.results_dir)
        
        # Close StockAnalysis scraper (releases Chrome)
        self._cleanup()
        
        print(f"\n{'='*60}")
        print(f"📋 VALIDATION COMPLETE")
        print(f"{'='*60}")
        print(f"Total Checks: {total_checks}")
        print(f"  └─ Validated: {total_validated} ({coverage_rate:.1f}% coverage)")
        print(f"  └─ Skipped:   {total_skip} (missing external data)")
        print(f"")
        print(f"Of Validated Checks:")
        print(f"  └─ Passed:   {total_pass}")
        print(f"  └─ Failed:   {total_fail}")
        print(f"  └─ Warnings: {total_warning}")
        print(f"")
        print(f"📊 METRICS:")
        print(f"  └─ Coverage Rate: {coverage_rate:.1f}% (data availability)")
        print(f"  └─ Accuracy Rate: {accuracy_rate:.1f}% (of validated)")
        print(f"  └─ Quality Score: {overall_quality:.1f}% (coverage × accuracy)")
        print(f"")
        print(f"Results saved to: {self.results_dir}")
        print(f"HTML Report: {html_path}")
        print(f"{'='*60}\n")
        
        return report
    
    def _cleanup(self):
        """Clean up resources (close browser, etc.)."""
        try:
            self.stockanalysis_scraper.close()
        except:
            pass
    
    def _validate_ticker(self, ticker: str) -> TickerValidation:
        """
        Validate all data for a single ticker.
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            TickerValidation with all results for this ticker
        """
        results = []
        timestamp = datetime.now().isoformat()
        
        # Fetch our data
        our_data = self._fetch_our_data(ticker)
        if not our_data:
            return TickerValidation(
                ticker=ticker,
                timestamp=timestamp,
                overall_status=ValidationStatus.SKIP,
                pass_count=0,
                fail_count=0,
                warning_count=0,
                skip_count=1,
                results=[]
            )
        
        # Fetch external data
        # Day 16: Using StockAnalysis instead of Yahoo (Yahoo is broken)
        stockanalysis_data = self.stockanalysis_scraper.scrape(ticker)
        finviz_data = self.finviz_scraper.scrape(ticker)
        
        # === PRICE VALIDATIONS (using StockAnalysis) ===
        if stockanalysis_data:
            # Current price
            results.append(self.comparator.compare(
                ticker=ticker,
                metric='current_price',
                our_value=our_data.get('currentPrice'),
                external_value=stockanalysis_data.get('price'),
                external_source='StockAnalysis',
                tolerance_key='price'
            ))
            
            # 52-week high
            results.append(self.comparator.compare(
                ticker=ticker,
                metric='52w_high',
                our_value=our_data.get('fiftyTwoWeekHigh'),
                external_value=stockanalysis_data.get('52w_high'),
                external_source='StockAnalysis',
                tolerance_key='52w_high'
            ))
            
            # 52-week low
            results.append(self.comparator.compare(
                ticker=ticker,
                metric='52w_low',
                our_value=our_data.get('fiftyTwoWeekLow'),
                external_value=stockanalysis_data.get('52w_low'),
                external_source='StockAnalysis',
                tolerance_key='52w_low'
            ))
            
            # P/E Ratio from StockAnalysis
            results.append(self.comparator.compare(
                ticker=ticker,
                metric='pe_ratio',
                our_value=our_data.get('fundamentals', {}).get('pe'),
                external_value=stockanalysis_data.get('pe_ratio'),
                external_source='StockAnalysis',
                tolerance_key='pe_ratio'
            ))
            
            # EPS from StockAnalysis
            results.append(self.comparator.compare(
                ticker=ticker,
                metric='eps',
                our_value=our_data.get('fundamentals', {}).get('eps'),
                external_value=stockanalysis_data.get('eps'),
                external_source='StockAnalysis',
                tolerance_key='price'  # Use price tolerance for EPS
            ))
        
        # === FUNDAMENTAL VALIDATIONS (using Finviz) ===
        fundamentals = our_data.get('fundamentals', {})
        
        if finviz_data:
            results.append(self.comparator.compare(
                ticker=ticker,
                metric='roe',
                our_value=fundamentals.get('roe'),
                external_value=finviz_data.get('roe'),
                external_source='Finviz',
                tolerance_key='roe'
            ))
            
            results.append(self.comparator.compare(
                ticker=ticker,
                metric='debt_equity',
                our_value=fundamentals.get('debtToEquity'),
                external_value=finviz_data.get('debt_equity'),
                external_source='Finviz',
                tolerance_key='debt_equity'
            ))
            
            # Day 54: Normalize growth rates from decimal to percentage
            # Our providers (FMP/yfinance info) return 0.1565 (decimal),
            # Finviz shows 15.65 (percentage). Multiply by 100 if < 1.
            # Edge case: growth > 100% (e.g., 1.50 = 150%) won't normalize,
            # but that's rare and would only trigger a WARNING, not a FAIL.
            rev_growth_raw = fundamentals.get('revenueGrowth')
            rev_growth_pct = rev_growth_raw * 100 if rev_growth_raw is not None and abs(rev_growth_raw) < 1 else rev_growth_raw
            results.append(self.comparator.compare(
                ticker=ticker,
                metric='revenue_growth',
                our_value=rev_growth_pct,
                external_value=finviz_data.get('sales_growth'),
                external_source='Finviz',
                tolerance_key='revenue_growth'
            ))

            # Day 54: Add epsGrowth comparison (was missing entirely)
            # Same decimal→percentage normalization
            eps_growth_raw = fundamentals.get('epsGrowth')
            eps_growth_pct = eps_growth_raw * 100 if eps_growth_raw is not None and abs(eps_growth_raw) < 1 else eps_growth_raw
            results.append(self.comparator.compare(
                ticker=ticker,
                metric='eps_growth',
                our_value=eps_growth_pct,
                external_value=finviz_data.get('eps_growth'),
                external_source='Finviz',
                tolerance_key='eps_growth'
            ))

        # === S&R LOGIC VALIDATIONS ===
        sr_data = self._fetch_sr_data(ticker)
        if sr_data:
            results.extend(self._validate_sr_logic(ticker, sr_data))
        
        # Filter out None results
        results = [r for r in results if r is not None]
        
        # Count ALL statuses including SKIP
        pass_count = sum(1 for r in results if r.status == ValidationStatus.PASS)
        fail_count = sum(1 for r in results if r.status == ValidationStatus.FAIL)
        warning_count = sum(1 for r in results if r.status == ValidationStatus.WARNING)
        skip_count = sum(1 for r in results if r.status == ValidationStatus.SKIP)
        
        # Determine overall status
        if fail_count > 0:
            overall_status = ValidationStatus.FAIL
        elif warning_count > 0:
            overall_status = ValidationStatus.WARNING
        elif skip_count > pass_count:
            overall_status = ValidationStatus.WARNING
        else:
            overall_status = ValidationStatus.PASS
        
        return TickerValidation(
            ticker=ticker,
            timestamp=timestamp,
            overall_status=overall_status,
            pass_count=pass_count,
            fail_count=fail_count,
            warning_count=warning_count,
            skip_count=skip_count,
            results=results
        )
    
    def _validate_sr_logic(self, ticker: str, sr_data: Dict) -> List[ValidationResult]:
        """
        Validate S&R logic (not external comparison, just sanity checks).
        """
        results = []
        timestamp = datetime.now().isoformat()
        current_price = sr_data.get('currentPrice', 0)
        
        # Check 1: Entry should be below current price (if exists)
        entry = sr_data.get('suggestedEntry')
        if entry is not None:
            entry_valid = entry < current_price
            results.append(ValidationResult(
                ticker=ticker,
                metric='sr_entry_below_price',
                our_value=entry,
                external_value=current_price,
                external_source='Logic Check',
                variance_pct=None,
                tolerance_pct=0,
                status=ValidationStatus.PASS if entry_valid else ValidationStatus.FAIL,
                timestamp=timestamp,
                notes=f"Entry ${entry:.2f} {'<' if entry_valid else '>='} Current ${current_price:.2f}"
            ))
            
            # Check 2: Entry within 20% of current price (proximity filter)
            if entry_valid:
                proximity = (current_price - entry) / current_price
                proximity_valid = proximity <= 0.20
                results.append(ValidationResult(
                    ticker=ticker,
                    metric='sr_entry_proximity',
                    our_value=round(proximity * 100, 1),
                    external_value=20.0,
                    external_source='Logic Check',
                    variance_pct=None,
                    tolerance_pct=20.0,
                    status=ValidationStatus.PASS if proximity_valid else ValidationStatus.FAIL,
                    timestamp=timestamp,
                    notes=f"Entry is {proximity*100:.1f}% below current (max 20%)"
                ))
        
        # Check 3: Target should be above current price (if exists)
        target = sr_data.get('suggestedTarget')
        if target is not None:
            target_valid = target > current_price
            results.append(ValidationResult(
                ticker=ticker,
                metric='sr_target_above_price',
                our_value=target,
                external_value=current_price,
                external_source='Logic Check',
                variance_pct=None,
                tolerance_pct=0,
                status=ValidationStatus.PASS if target_valid else ValidationStatus.FAIL,
                timestamp=timestamp,
                notes=f"Target ${target:.2f} {'>' if target_valid else '<='} Current ${current_price:.2f}"
            ))
        
        # Check 4: Stop should be below entry (if both exist)
        stop = sr_data.get('suggestedStop')
        if stop is not None and entry is not None:
            stop_valid = stop < entry
            results.append(ValidationResult(
                ticker=ticker,
                metric='sr_stop_below_entry',
                our_value=stop,
                external_value=entry,
                external_source='Logic Check',
                variance_pct=None,
                tolerance_pct=0,
                status=ValidationStatus.PASS if stop_valid else ValidationStatus.FAIL,
                timestamp=timestamp,
                notes=f"Stop ${stop:.2f} {'<' if stop_valid else '>='} Entry ${entry:.2f}"
            ))
        
        # Check 5: Risk/Reward should be reasonable (0.5-15 range)
        rr = sr_data.get('riskReward')
        if rr is not None:
            rr_valid = 0.5 <= rr <= 15
            results.append(ValidationResult(
                ticker=ticker,
                metric='sr_risk_reward_reasonable',
                our_value=rr,
                external_value=None,
                external_source='Logic Check',
                variance_pct=None,
                tolerance_pct=0,
                status=ValidationStatus.PASS if rr_valid else ValidationStatus.WARNING,
                timestamp=timestamp,
                notes=f"R:R {rr:.2f}:1 {'in' if rr_valid else 'outside'} reasonable range (0.5-15)"
            ))
        
        return results
    
    def _fetch_our_data(self, ticker: str) -> Optional[Dict]:
        """Fetch data from our API endpoints."""
        try:
            # Fetch stock data
            stock_resp = requests.get(f"{self.API_BASE}/stock/{ticker}", timeout=30)
            if not stock_resp.ok:
                print(f"   ⚠️ Failed to fetch stock data for {ticker}")
                return None
            stock_data = stock_resp.json()
            
            # Fetch fundamentals
            # fund_resp = requests.get(f"{self.API_BASE}/fundamentals/{ticker}", timeout=30)
            #if fund_resp.ok:
            #   stock_data['fundamentals'] = fund_resp.json()

            # Fetch fundamentals from Defeat Beta and MERGE with yfinance fundamentals
            fund_resp = requests.get(f"{self.API_BASE}/fundamentals/{ticker}", timeout=30)
            if fund_resp.ok:
                defeatbeta_funds = fund_resp.json()
            # Merge: Defeat Beta values override yfinance, but keep yfinance values not in Defeat Beta
            yfinance_funds = stock_data.get('fundamentals', {})
            merged_funds = {**yfinance_funds, **defeatbeta_funds}
            stock_data['fundamentals'] = merged_funds    
            
            return stock_data
            
        except Exception as e:
            print(f"   ❌ Error fetching our data for {ticker}: {e}")
            return None
    
    def _fetch_sr_data(self, ticker: str) -> Optional[Dict]:
        """Fetch S&R data from our API."""
        try:
            resp = requests.get(f"{self.API_BASE}/sr/{ticker}", timeout=30)
            if resp.ok:
                return resp.json()
            return None
        except Exception as e:
            print(f"   ⚠️ Error fetching S&R data for {ticker}: {e}")
            return None
    
    def _sanitize_for_json(self, value):
        """
        Convert NaN/Inf values to None for JSON serialization.
        Day 41 Fix: NaN is not valid JSON
        """
        import math
        if value is None:
            return None
        if isinstance(value, float):
            if math.isnan(value) or math.isinf(value):
                return None
        return value

    def _save_results(self, report: ValidationReport):
        """Save validation results to JSON file."""
        filename = f"validation_{report.run_id}.json"
        filepath = os.path.join(self.results_dir, filename)

        # Convert to dict for JSON serialization
        # Day 41 Fix: Sanitize all numeric values that could be NaN
        report_dict = {
            'run_id': report.run_id,
            'timestamp': report.timestamp,
            'tickers': report.tickers,
            'overall_pass_rate': self._sanitize_for_json(report.overall_pass_rate),
            'coverage_rate': self._sanitize_for_json(report.coverage_rate),
            'accuracy_rate': self._sanitize_for_json(report.accuracy_rate),
            'summary': report.summary,
            'ticker_results': []
        }
        
        for tv in report.ticker_results:
            tv_dict = {
                'ticker': tv.ticker,
                'timestamp': tv.timestamp,
                'overall_status': tv.overall_status.value,
                'pass_count': tv.pass_count,
                'fail_count': tv.fail_count,
                'warning_count': tv.warning_count,
                'skip_count': tv.skip_count,
                'results': []
            }
            for r in tv.results:
                # Day 41 Fix: Sanitize NaN values for JSON
                tv_dict['results'].append({
                    'metric': r.metric,
                    'our_value': self._sanitize_for_json(r.our_value),
                    'external_value': self._sanitize_for_json(r.external_value),
                    'external_source': r.external_source,
                    'variance_pct': self._sanitize_for_json(r.variance_pct),
                    'tolerance_pct': r.tolerance_pct,
                    'status': r.status.value,
                    'notes': r.notes
                })
            report_dict['ticker_results'].append(tv_dict)
        
        with open(filepath, 'w') as f:
            json.dump(report_dict, f, indent=2)
        
        print(f"   💾 Results saved to {filename}")


# CLI entry point
if __name__ == '__main__':
    engine = ValidationEngine()
    report = engine.run_validation()