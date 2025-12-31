#!/bin/bash
# Swing Trade Analyzer - Comprehensive Test Script
# Day 19: Bug Hunting & Documentation
# Tests 10 stocks across all APIs and outputs summary

OUTPUT_FILE="test_results_day19.txt"
TICKERS="AAPL NVDA AVGO MSFT META TSLA JPM XOM PLTR VOO"

echo "=============================================" > $OUTPUT_FILE
echo "SWING TRADE ANALYZER - TEST RESULTS" >> $OUTPUT_FILE
echo "Date: $(date)" >> $OUTPUT_FILE
echo "Tickers: $TICKERS" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE

# Test 1: Validation API (batch - all tickers at once)
echo "" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE
echo "TEST 1: VALIDATION API (Cross-verification)" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE
curl -s -X POST http://localhost:5001/api/validation/run \
  -H "Content-Type: application/json" \
  -d '{"tickers": ["AAPL","NVDA","AVGO","MSFT","META","TSLA","JPM","XOM","PLTR","VOO"]}' \
  | python3 -m json.tool >> $OUTPUT_FILE 2>&1

# Test 2: S&R API for each ticker (Trade Setup completeness)
echo "" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE
echo "TEST 2: S&R API (Trade Setup for each ticker)" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE

for TICKER in $TICKERS; do
  echo "" >> $OUTPUT_FILE
  echo "--- $TICKER S&R ---" >> $OUTPUT_FILE
  curl -s http://localhost:5001/api/sr/$TICKER | python3 -m json.tool >> $OUTPUT_FILE 2>&1
done

# Test 3: TradingView Scan (check if broken)
echo "" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE
echo "TEST 3: TRADINGVIEW SCAN API" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE
echo "--- Reddit Strategy ---" >> $OUTPUT_FILE
curl -s "http://localhost:5001/api/scan/tradingview?strategy=reddit&limit=5" >> $OUTPUT_FILE 2>&1
echo "" >> $OUTPUT_FILE

# Test 4: Health Check
echo "" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE
echo "TEST 4: BACKEND HEALTH CHECK" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE
curl -s http://localhost:5001/api/health | python3 -m json.tool >> $OUTPUT_FILE 2>&1

# Summary
echo "" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE
echo "TEST COMPLETE" >> $OUTPUT_FILE
echo "Output saved to: $OUTPUT_FILE" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE

echo "Tests complete! Results saved to $OUTPUT_FILE"