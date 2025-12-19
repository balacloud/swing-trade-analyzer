"""
HTML Report Generator for Validation Engine
Generates beautiful HTML reports from validation results

Day 15: Validation reporting
"""

import os
from datetime import datetime
from typing import Dict, List, Any


class HTMLReportGenerator:
    """
    Generates HTML reports from validation results.
    """
    
    def generate(self, report: Any, output_dir: str) -> str:
        """
        Generate HTML report from ValidationReport.
        
        Args:
            report: ValidationReport object
            output_dir: Directory to save the report
            
        Returns:
            Path to generated HTML file
        """
        html = self._build_html(report)
        
        filename = f"validation_report_{report.run_id}.html"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(html)
        
        return filepath
    
    def _build_html(self, report: Any) -> str:
        """Build the complete HTML document."""
        
        # Determine overall status color
        pass_rate = report.overall_pass_rate
        if pass_rate >= 90:
            overall_color = '#22c55e'  # green
            overall_emoji = '✅'
        elif pass_rate >= 70:
            overall_color = '#eab308'  # yellow
            overall_emoji = '⚠️'
        else:
            overall_color = '#ef4444'  # red
            overall_emoji = '❌'
        
        # Build ticker cards
        ticker_cards = []
        for tv in report.ticker_results:
            ticker_cards.append(self._build_ticker_card(tv))
        
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Validation Report - {report.run_id}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #e5e5e5;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .header {{
            text-align: center;
            padding: 30px;
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            margin-bottom: 30px;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        
        .header h1 {{
            font-size: 2rem;
            margin-bottom: 10px;
            color: #60a5fa;
        }}
        
        .header .timestamp {{
            color: #9ca3af;
            font-size: 0.9rem;
        }}
        
        .summary-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .summary-card {{
            background: rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        
        .summary-card .value {{
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        .summary-card .label {{
            color: #9ca3af;
            font-size: 0.9rem;
        }}
        
        .pass-rate {{
            color: {overall_color};
        }}
        
        .passed {{ color: #22c55e; }}
        .failed {{ color: #ef4444; }}
        .warnings {{ color: #eab308; }}
        
        .ticker-section {{
            margin-bottom: 30px;
        }}
        
        .ticker-card {{
            background: rgba(255,255,255,0.05);
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 20px;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        
        .ticker-header {{
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        
        .ticker-name {{
            font-size: 1.3rem;
            font-weight: bold;
        }}
        
        .ticker-status {{
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
        }}
        
        .status-pass {{ background: rgba(34, 197, 94, 0.2); color: #22c55e; }}
        .status-fail {{ background: rgba(239, 68, 68, 0.2); color: #ef4444; }}
        .status-warning {{ background: rgba(234, 179, 8, 0.2); color: #eab308; }}
        .status-skip {{ background: rgba(156, 163, 175, 0.2); color: #9ca3af; }}
        
        .results-table {{
            width: 100%;
            border-collapse: collapse;
        }}
        
        .results-table th,
        .results-table td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }}
        
        .results-table th {{
            background: rgba(255,255,255,0.03);
            color: #9ca3af;
            font-weight: 500;
            font-size: 0.85rem;
            text-transform: uppercase;
        }}
        
        .results-table tr:hover {{
            background: rgba(255,255,255,0.03);
        }}
        
        .metric-name {{
            font-weight: 500;
        }}
        
        .value-cell {{
            font-family: 'SF Mono', Monaco, monospace;
            font-size: 0.9rem;
        }}
        
        .variance {{
            font-weight: 500;
        }}
        
        .variance.good {{ color: #22c55e; }}
        .variance.warning {{ color: #eab308; }}
        .variance.bad {{ color: #ef4444; }}
        
        .notes {{
            font-size: 0.85rem;
            color: #9ca3af;
        }}
        
        .footer {{
            text-align: center;
            padding: 20px;
            color: #6b7280;
            font-size: 0.85rem;
        }}
        
        .badge {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 500;
        }}
        
        .badge-pass {{ background: rgba(34, 197, 94, 0.2); color: #22c55e; }}
        .badge-fail {{ background: rgba(239, 68, 68, 0.2); color: #ef4444; }}
        .badge-warning {{ background: rgba(234, 179, 8, 0.2); color: #eab308; }}
        .badge-skip {{ background: rgba(156, 163, 175, 0.2); color: #9ca3af; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 Validation Report</h1>
            <div class="timestamp">Run ID: {report.run_id} | {report.timestamp}</div>
        </div>
        
        <div class="summary-cards">
            <div class="summary-card">
                <div class="value pass-rate">{overall_emoji} {report.overall_pass_rate}%</div>
                <div class="label">Overall Pass Rate</div>
            </div>
            <div class="summary-card">
                <div class="value">{report.summary['total_checks']}</div>
                <div class="label">Total Checks</div>
            </div>
            <div class="summary-card">
                <div class="value passed">{report.summary['passed']}</div>
                <div class="label">Passed</div>
            </div>
            <div class="summary-card">
                <div class="value failed">{report.summary['failed']}</div>
                <div class="label">Failed</div>
            </div>
            <div class="summary-card">
                <div class="value warnings">{report.summary['warnings']}</div>
                <div class="label">Warnings</div>
            </div>
        </div>
        
        <div class="ticker-section">
            <h2 style="margin-bottom: 20px; color: #60a5fa;">📊 Results by Ticker</h2>
            {''.join(ticker_cards)}
        </div>
        
        <div class="footer">
            <p>Swing Trade Analyzer - Validation Engine v1.0</p>
            <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>'''
        
        return html
    
    def _build_ticker_card(self, tv: Any) -> str:
        """Build HTML for a single ticker's results."""
        
        # Determine status class
        status_class = f"status-{tv.overall_status.value}"
        status_text = tv.overall_status.value.upper()
        
        # Build results rows
        rows = []
        for r in tv.results:
            # Format values
            our_val = f"{r.our_value:.4f}" if r.our_value is not None else "N/A"
            ext_val = f"{r.external_value:.4f}" if r.external_value is not None else "N/A"
            
            # Variance formatting
            if r.variance_pct is not None:
                if r.variance_pct <= r.tolerance_pct:
                    var_class = "good"
                elif r.variance_pct <= r.tolerance_pct * 1.5:
                    var_class = "warning"
                else:
                    var_class = "bad"
                variance_html = f'<span class="variance {var_class}">{r.variance_pct:.1f}%</span>'
            else:
                variance_html = '<span class="variance">-</span>'
            
            # Status badge
            badge_class = f"badge-{r.status.value}"
            badge_html = f'<span class="badge {badge_class}">{r.status.value.upper()}</span>'
            
            rows.append(f'''
                <tr>
                    <td class="metric-name">{r.metric}</td>
                    <td class="value-cell">{our_val}</td>
                    <td class="value-cell">{ext_val}</td>
                    <td>{r.external_source}</td>
                    <td>{variance_html}</td>
                    <td>{badge_html}</td>
                    <td class="notes">{r.notes}</td>
                </tr>
            ''')
        
        return f'''
        <div class="ticker-card">
            <div class="ticker-header">
                <div class="ticker-name">{tv.ticker}</div>
                <div>
                    <span style="margin-right: 15px; color: #9ca3af;">
                        ✅ {tv.pass_count} | ❌ {tv.fail_count} | ⚠️ {tv.warning_count}
                    </span>
                    <span class="ticker-status {status_class}">{status_text}</span>
                </div>
            </div>
            <table class="results-table">
                <thead>
                    <tr>
                        <th>Metric</th>
                        <th>Our Value</th>
                        <th>External Value</th>
                        <th>Source</th>
                        <th>Variance</th>
                        <th>Status</th>
                        <th>Notes</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(rows)}
                </tbody>
            </table>
        </div>
        '''
