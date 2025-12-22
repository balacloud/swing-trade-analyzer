"""
Web Scrapers for Validation Engine
Scrapes StockAnalysis, Yahoo Finance, and Finviz for validation data

Day 15: Initial scrapers (Yahoo + Finviz)
Day 16: Added StockAnalysis scraper to replace broken Yahoo
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from typing import Dict, Optional
import random

# Try to import stockanalysis-scraper package
try:
    from stockanalysis_scraper.scraper.scraper import StockAnalysis as StockAnalysisScraper
    STOCKANALYSIS_AVAILABLE = True
except ImportError:
    STOCKANALYSIS_AVAILABLE = False
    print("⚠️ stockanalysis-scraper not installed. Run: pip install stockanalysis-scraper")


class BaseScraper:
    """Base class for web scrapers with common functionality."""
    
    # Common headers to mimic browser
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
    
    def _get_page(self, url: str, retries: int = 3) -> Optional[BeautifulSoup]:
        """
        Fetch and parse a webpage with retry logic.
        
        Args:
            url: URL to fetch
            retries: Number of retry attempts
            
        Returns:
            BeautifulSoup object or None on failure
        """
        for attempt in range(retries):
            try:
                # Add small random delay to be respectful
                time.sleep(random.uniform(0.5, 1.5))
                
                response = self.session.get(url, timeout=15)
                
                if response.status_code == 200:
                    return BeautifulSoup(response.text, 'html.parser')
                elif response.status_code == 429:
                    # Rate limited - wait longer
                    print(f"   ⏳ Rate limited, waiting...")
                    time.sleep(5 * (attempt + 1))
                else:
                    print(f"   ⚠️ HTTP {response.status_code} for {url}")
                    
            except requests.RequestException as e:
                print(f"   ⚠️ Request error (attempt {attempt + 1}): {e}")
                time.sleep(2)
        
        return None
    
    def _parse_number(self, text: str) -> Optional[float]:
        """
        Parse a number from text, handling formats like:
        - "123.45"
        - "1.23B" (billions)
        - "45.67M" (millions)
        - "12.34%" (percentages)
        - "N/A" or "-"
        
        Args:
            text: Text containing a number
            
        Returns:
            Parsed float or None
        """
        if not text or text.strip() in ['N/A', '-', '--', '', 'None']:
            return None
        
        # Convert to string if not already
        text = str(text).strip().replace(',', '').replace('$', '')
        
        # Handle percentages
        if '%' in text:
            text = text.replace('%', '')
            try:
                return float(text)
            except ValueError:
                return None
        
        # Handle multipliers (B, M, K, T)
        multipliers = {
            'T': 1e12,
            'B': 1e9,
            'M': 1e6,
            'K': 1e3,
        }
        
        for suffix, mult in multipliers.items():
            if suffix in text.upper():
                text = text.upper().replace(suffix, '')
                try:
                    return float(text) * mult
                except ValueError:
                    return None
        
        # Regular number
        try:
            return float(text)
        except ValueError:
            return None


class StockAnalysisScraperWrapper(BaseScraper):
    """
    Wrapper for stockanalysis-scraper package.
    
    Extracts: price, market cap, revenue, EPS, P/E ratio, 52-week range
    This replaces the broken Yahoo Finance scraper.
    
    Day 16: Added as primary price/fundamental source
    
    NOTE: This uses Selenium/Chrome under the hood, so it's slower
    but more reliable than direct scraping.
    """
    
    def __init__(self):
        super().__init__()
        self.scraper = None  # Lazy init to avoid Chrome startup on import
    
    def _get_scraper(self):
        """Lazy initialize the scraper (opens Chrome)."""
        if self.scraper is None and STOCKANALYSIS_AVAILABLE:
            try:
                self.scraper = StockAnalysisScraper()
            except Exception as e:
                print(f"   ⚠️ Failed to initialize StockAnalysis scraper: {e}")
        return self.scraper
    
    def scrape(self, ticker: str) -> Optional[Dict]:
        """
        Scrape StockAnalysis.com for a ticker.
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dict with scraped data or None on failure
        """
        if not STOCKANALYSIS_AVAILABLE:
            print(f"   ⚠️ StockAnalysis scraper not available")
            return None
        
        data = {
            'ticker': ticker,
            'source': 'StockAnalysis',
            'price': None,
            '52w_high': None,
            '52w_low': None,
            'pe_ratio': None,
            'eps': None,
            'market_cap': None,
            'revenue': None,
        }
        
        try:
            scraper = self._get_scraper()
            if not scraper:
                return None
            
            # Get stock data using the package
            stock_data = scraper.scrape_stock_data(ticker)
            
            if stock_data:
                # Parse price
                data['price'] = self._parse_number(stock_data.get('price'))
                
                # Parse overview section
                overview = stock_data.get('overview', {})
                data['market_cap'] = self._parse_number(overview.get('Market Cap'))
                data['revenue'] = self._parse_number(overview.get('Revenue (ttm)'))
                data['eps'] = self._parse_number(overview.get('EPS (ttm)'))
                data['pe_ratio'] = self._parse_number(overview.get('PE Ratio'))
                
                # Parse 52-week range
                range_52w = overview.get('52-Week Range', '')
                if ' - ' in range_52w:
                    parts = range_52w.split(' - ')
                    if len(parts) == 2:
                        data['52w_low'] = self._parse_number(parts[0])
                        data['52w_high'] = self._parse_number(parts[1])
                
            return data
            
        except Exception as e:
            print(f"   ⚠️ Error scraping StockAnalysis for {ticker}: {e}")
            return None
    
    def close(self):
        """Close the browser/scraper."""
        if self.scraper:
            try:
                self.scraper.close()
            except:
                pass
            self.scraper = None


class YahooFinanceScraper(BaseScraper):
    """
    Scraper for Yahoo Finance.
    
    NOTE: Yahoo frequently changes their HTML structure, causing this scraper
    to break. Consider using StockAnalysis scraper as primary source.
    
    Extracts: price, 52-week high/low, P/E ratio, EPS, market cap
    """
    
    BASE_URL = "https://finance.yahoo.com/quote"
    
    def scrape(self, ticker: str) -> Optional[Dict]:
        """
        Scrape Yahoo Finance for a ticker.
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dict with scraped data or None on failure
        """
        url = f"{self.BASE_URL}/{ticker}"
        soup = self._get_page(url)
        
        if not soup:
            print(f"   ⚠️ Failed to fetch Yahoo Finance page for {ticker}")
            return None
        
        data = {
            'ticker': ticker,
            'source': 'Yahoo Finance',
            'price': None,
            '52w_high': None,
            '52w_low': None,
            'pe_ratio': None,
            'eps': None,
            'market_cap': None,
        }
        
        try:
            # Method 1: Try data-test attributes (older Yahoo structure)
            data.update(self._scrape_data_test_attrs(soup))
            
            # Method 2: Try fin-streamer elements (newer Yahoo structure)
            if data['price'] is None:
                data.update(self._scrape_fin_streamer(soup, ticker))
            
            # Method 3: Try table-based extraction
            if data['pe_ratio'] is None:
                data.update(self._scrape_tables(soup))
            
        except Exception as e:
            print(f"   ⚠️ Error parsing Yahoo Finance for {ticker}: {e}")
        
        return data
    
    def _scrape_data_test_attrs(self, soup: BeautifulSoup) -> Dict:
        """Extract data using data-test attributes."""
        data = {}
        
        # Map of data-test values to our field names
        field_map = {
            'PREV_CLOSE-value': 'prev_close',
            'OPEN-value': 'open',
            'BID-value': 'bid',
            'ASK-value': 'ask',
            'DAYS_RANGE-value': 'day_range',
            'FIFTY_TWO_WK_RANGE-value': '52w_range',
            'TD_VOLUME-value': 'volume',
            'AVERAGE_VOLUME_3MONTH-value': 'avg_volume',
            'MARKET_CAP-value': 'market_cap',
            'BETA_5Y-value': 'beta',
            'PE_RATIO-value': 'pe_ratio',
            'EPS_RATIO-value': 'eps',
        }
        
        for data_test, field in field_map.items():
            elem = soup.find('td', {'data-test': data_test})
            if elem:
                text = elem.get_text(strip=True)
                data[field] = self._parse_number(text)
        
        # Parse 52-week range into high/low
        if '52w_range' in data and data.get('52w_range'):
            range_text = soup.find('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'})
            if range_text:
                range_text = range_text.get_text(strip=True)
                if ' - ' in range_text:
                    parts = range_text.split(' - ')
                    if len(parts) == 2:
                        data['52w_low'] = self._parse_number(parts[0])
                        data['52w_high'] = self._parse_number(parts[1])
        
        return data
    
    def _scrape_fin_streamer(self, soup: BeautifulSoup, ticker: str) -> Dict:
        """Extract data using fin-streamer elements (newer Yahoo)."""
        data = {}
        
        # Current price from fin-streamer
        price_elem = soup.find('fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketPrice'})
        if price_elem:
            data['price'] = self._parse_number(price_elem.get('data-value') or price_elem.get_text())
        
        return data
    
    def _scrape_tables(self, soup: BeautifulSoup) -> Dict:
        """Extract data from summary tables."""
        data = {}
        
        # Find all table rows
        for row in soup.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) >= 2:
                label = cells[0].get_text(strip=True).lower()
                value = cells[1].get_text(strip=True)
                
                if 'pe ratio' in label or 'p/e' in label:
                    data['pe_ratio'] = self._parse_number(value)
                elif 'eps' in label and 'ttm' in label:
                    data['eps'] = self._parse_number(value)
                elif 'market cap' in label:
                    data['market_cap'] = self._parse_number(value)
                elif '52' in label and 'week' in label and 'range' in label:
                    if ' - ' in value:
                        parts = value.split(' - ')
                        if len(parts) == 2:
                            data['52w_low'] = self._parse_number(parts[0])
                            data['52w_high'] = self._parse_number(parts[1])
        
        return data


class FinvizScraper(BaseScraper):
    """
    Scraper for Finviz.
    
    Extracts: ROE, Debt/Equity, Sales Growth, EPS Growth, P/E
    Finviz has a cleaner table structure that's easier to scrape.
    
    STATUS: WORKING (Day 16 verified)
    """
    
    BASE_URL = "https://finviz.com/quote.ashx"
    
    def scrape(self, ticker: str) -> Optional[Dict]:
        """
        Scrape Finviz for a ticker.
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dict with scraped data or None on failure
        """
        url = f"{self.BASE_URL}?t={ticker}"
        soup = self._get_page(url)
        
        if not soup:
            print(f"   ⚠️ Failed to fetch Finviz page for {ticker}")
            return None
        
        data = {
            'ticker': ticker,
            'source': 'Finviz',
            'price': None,
            'pe_ratio': None,
            'eps': None,
            'roe': None,
            'roi': None,
            'debt_equity': None,
            'sales_growth': None,
            'eps_growth': None,
            'profit_margin': None,
        }
        
        try:
            # Finviz uses a consistent table structure
            data.update(self._scrape_snapshot_table(soup))
            
        except Exception as e:
            print(f"   ⚠️ Error parsing Finviz for {ticker}: {e}")
        
        return data
    
    def _scrape_snapshot_table(self, soup: BeautifulSoup) -> Dict:
        """Extract data from Finviz snapshot table."""
        data = {}
        
        # Finviz snapshot table has class 'snapshot-table2'
        table = soup.find('table', class_='snapshot-table2')
        if not table:
            # Try alternative class names
            table = soup.find('table', class_='snapshot-table')
        
        if not table:
            return data
        
        # The table has alternating label/value cells
        cells = table.find_all('td')
        
        # Create label->value mapping
        i = 0
        while i < len(cells) - 1:
            label_cell = cells[i]
            value_cell = cells[i + 1]
            
            label = label_cell.get_text(strip=True).lower()
            value = value_cell.get_text(strip=True)
            
            # Map labels to our field names
            if label == 'p/e':
                data['pe_ratio'] = self._parse_number(value)
            elif label == 'eps (ttm)':
                data['eps'] = self._parse_number(value)
            elif label == 'roe':
                data['roe'] = self._parse_number(value)
            elif label == 'roi':
                data['roi'] = self._parse_number(value)
            elif label == 'debt/eq':
                data['debt_equity'] = self._parse_number(value)
            elif label == 'sales q/q':
                data['sales_growth'] = self._parse_number(value)
            elif label == 'eps q/q':
                data['eps_growth'] = self._parse_number(value)
            elif label == 'profit margin':
                data['profit_margin'] = self._parse_number(value)
            elif label == 'price':
                data['price'] = self._parse_number(value)
            
            i += 2
        
        return data


# Test scrapers directly
if __name__ == '__main__':
    print("="*50)
    print("SCRAPER TEST SUITE")
    print("="*50)
    
    ticker = 'AAPL'
    sa = None
    sa_data = None
    
    print(f"\n1. Testing StockAnalysis Scraper for {ticker}...")
    if STOCKANALYSIS_AVAILABLE:
        sa = StockAnalysisScraperWrapper()
        sa_data = sa.scrape(ticker)
        print(f"   StockAnalysis: {sa_data}")
    else:
        print("   ⚠️ StockAnalysis scraper not available")
    
    print(f"\n2. Testing Yahoo Finance Scraper for {ticker}...")
    yahoo = YahooFinanceScraper()
    yahoo_data = yahoo.scrape(ticker)
    print(f"   Yahoo: {yahoo_data}")
    
    print(f"\n3. Testing Finviz Scraper for {ticker}...")
    finviz = FinvizScraper()
    finviz_data = finviz.scrape(ticker)
    print(f"   Finviz: {finviz_data}")
    
    # Close StockAnalysis scraper (releases Chrome)
    if sa:
        sa.close()
    
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"StockAnalysis: {'✅ Working' if sa_data and sa_data.get('price') else '❌ Failed'}")
    print(f"Yahoo Finance: {'✅ Working' if yahoo_data and yahoo_data.get('price') else '❌ Failed'}")
    print(f"Finviz:        {'✅ Working' if finviz_data and finviz_data.get('roe') else '❌ Failed'}")