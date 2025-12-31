#!/bin/bash
# Test Batch 3 - Diverse Edge Cases
OUTPUT_FILE="test_results_day19_batch3.txt"
TICKERS="NFLX CRM UNH V HD LLY COIN SMCI F SQ"

echo "=============================================" > $OUTPUT_FILE
echo "SWING TRADE ANALYZER - TEST RESULTS BATCH 3" >> $OUTPUT_FILE
echo "Date: $(date)" >> $OUTPUT_FILE
echo "Tickers: $TICKERS" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE

# S&R API for each ticker
echo "" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE
echo "S&R API (Trade Setup for each ticker)" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE

for TICKER in $TICKERS; do
  echo "" >> $OUTPUT_FILE
  echo "--- $TICKER S&R ---" >> $OUTPUT_FILE
  curl -s http://localhost:5001/api/sr/$TICKER | python3 -m json.tool >> $OUTPUT_FILE 2>&1
done

# Validation API
echo "" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE
echo "VALIDATION API" >> $OUTPUT_FILE  
echo "=============================================" >> $OUTPUT_FILE
curl -s -X POST http://localhost:5001/api/validation/run \
  -H "Content-Type: application/json" \
  -d '{"tickers": ["NFLX","CRM","UNH","V","HD","LLY","COIN","SMCI","F","SQ"]}' \
  | python3 -m json.tool >> $OUTPUT_FILE 2>&1

echo "" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE
echo "TEST COMPLETE" >> $OUTPUT_FILE
echo "=============================================" >> $OUTPUT_FILE

echo "Tests complete! Results saved to $OUTPUT_FILE"