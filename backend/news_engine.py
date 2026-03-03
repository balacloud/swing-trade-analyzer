"""
news_engine.py — Context Tab Column C
Day 62, v4.24

News sentiment (Alpha Vantage NEWS_SENTIMENT) + short interest (yfinance) per ticker.

Core STA engine is FROZEN. This file is additive / informational only.
"""

import os
import requests
import logging
import yfinance as yf
from datetime import datetime

logger = logging.getLogger(__name__)

ALPHAVANTAGE_API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')
AV_BASE_URL = 'https://www.alphavantage.co/query'

# ─── Alpha Vantage news fetch ─────────────────────────────────────────────────
def _fetch_av_news(ticker: str, limit: int = 10):
    """
    Fetch NEWS_SENTIMENT from Alpha Vantage.
    Returns list of raw article dicts or None on failure.
    """
    if not ALPHAVANTAGE_API_KEY:
        return None
    try:
        resp = requests.get(AV_BASE_URL, params={
            'function': 'NEWS_SENTIMENT',
            'tickers': ticker.upper(),
            'limit': limit,
            'sort': 'RELEVANCE',
            'apikey': ALPHAVANTAGE_API_KEY,
        }, timeout=12)
        resp.raise_for_status()
        data = resp.json()
        if 'Note' in data or 'Information' in data:
            # Rate limit hit
            logger.warning(f"Alpha Vantage rate limit: {data.get('Note') or data.get('Information')}")
            return None
        return data.get('feed', [])
    except Exception as e:
        logger.warning(f"Alpha Vantage news fetch failed for {ticker}: {e}")
        return None


def _score_to_emoji(score: float) -> str:
    if score > 0.15:
        return '🟢'
    if score < -0.15:
        return '🔴'
    return '🟡'


def _parse_articles(feed: list, ticker: str) -> list:
    """
    Parse Alpha Vantage feed items into clean article dicts.
    Filters to items that have a sentiment entry for the specific ticker.
    """
    articles = []
    ticker_upper = ticker.upper()
    for item in feed:
        # Find per-ticker sentiment entry
        ticker_sent = next(
            (t for t in item.get('ticker_sentiment', [])
             if t.get('ticker') == ticker_upper),
            None
        )
        if not ticker_sent:
            continue
        try:
            score = float(ticker_sent.get('ticker_sentiment_score', 0))
        except (ValueError, TypeError):
            score = 0.0

        title = item.get('title', '')
        if len(title) > 55:
            title = title[:52] + '...'

        articles.append({
            'title': title,
            'url': item.get('url', ''),
            'source': item.get('source', ''),
            'date': item.get('time_published', '')[:10],  # YYYYMMDDTHHMMSS → YYYY-MM-DD
            'score': round(score, 3),
            'emoji': _score_to_emoji(score),
            'sentiment_label': ticker_sent.get('ticker_sentiment_label', 'Neutral'),
        })

    return articles


def _aggregate_sentiment(articles: list) -> dict:
    """Compute aggregate sentiment from parsed article list."""
    if not articles:
        return {
            'label': 'NEUTRAL',
            'avg_score': 0.0,
            'bullish': 0,
            'bearish': 0,
            'neutral': 0,
        }
    scores = [a['score'] for a in articles]
    avg = sum(scores) / len(scores)
    bullish = sum(1 for s in scores if s > 0.15)
    bearish = sum(1 for s in scores if s < -0.15)
    neutral_count = len(scores) - bullish - bearish
    label = 'BULLISH' if avg > 0.1 else ('BEARISH' if avg < -0.1 else 'NEUTRAL')
    return {
        'label': label,
        'avg_score': round(avg, 3),
        'bullish': bullish,
        'bearish': bearish,
        'neutral': neutral_count,
    }


# ─── Short interest (yfinance) ────────────────────────────────────────────────
def _get_short_interest(ticker: str) -> dict:
    """Fetch short interest data from yfinance .info dict."""
    try:
        info = yf.Ticker(ticker).info
        short_pct = info.get('shortPercentOfFloat')
        short_ratio = info.get('shortRatio')
        if short_pct is not None:
            if short_pct > 0.20:
                assessment = 'High'
            elif short_pct > 0.05:
                assessment = 'Normal'
            else:
                assessment = 'Low'
        else:
            assessment = 'Unknown'
        return {
            'short_pct_float': round(short_pct * 100, 1) if short_pct is not None else None,
            'short_ratio': round(short_ratio, 1) if short_ratio is not None else None,
            'assessment': assessment,
        }
    except Exception as e:
        logger.warning(f"Short interest fetch failed for {ticker}: {e}")
        return {'short_pct_float': None, 'short_ratio': None, 'assessment': 'Unknown'}


# ─── Main entry point ─────────────────────────────────────────────────────────
def get_news(ticker: str) -> dict:
    """
    Returns news sentiment + short interest for ticker.
    Column C data — ticker-specific, cached 4h.
    """
    ticker = ticker.upper()

    # Fetch news
    feed = _fetch_av_news(ticker)

    if feed is None and ALPHAVANTAGE_API_KEY:
        # API call failed (not missing key)
        articles = []
        aggregate = None
        error = 'News fetch failed — API error or rate limit'
    elif not ALPHAVANTAGE_API_KEY:
        articles = []
        aggregate = None
        error = 'Configure ALPHAVANTAGE_API_KEY to enable news sentiment'
    else:
        articles = _parse_articles(feed, ticker)
        aggregate = _aggregate_sentiment(articles)
        error = None

    short_interest = _get_short_interest(ticker)

    return {
        'ticker': ticker,
        'articles': articles,
        'aggregate': aggregate,
        'short_interest': short_interest,
        'error': error,
        'timestamp': datetime.now().isoformat(),
        'av_available': ALPHAVANTAGE_API_KEY is not None,
    }
