# n8n Workflow Integration - Research Notes

> **Created:** Day 50 (February 10, 2026)
> **Status:** RESEARCH NEEDED (Future Session)
> **Priority:** P3 - Enhancement

---

## What is n8n?

n8n is an open-source workflow automation tool (similar to Zapier/Make but self-hosted).

## Potential Use Cases for Swing Trade Analyzer

### 1. Automated Scanning Workflows
- Daily market scan at market open
- Filter stocks meeting criteria
- Push notifications when candidates found

### 2. Alert Workflows
- Price alert triggers when watchlist stock hits entry zone
- Volume spike detection
- Earnings calendar reminders

### 3. Portfolio Tracking
- Track opened positions
- Calculate real-time P&L
- Exit signal notifications

### 4. Data Pipeline
- Aggregate data from multiple sources
- Cache management automation
- Daily data refresh workflows

### 5. Reporting
- Daily/weekly summary reports
- Performance tracking emails
- Market regime change alerts

---

## Research Questions (For Future Session)

1. Can n8n call our Flask backend APIs?
2. What triggers are available (cron, webhook, price alerts)?
3. How to integrate with notification services (Telegram, Discord, Email)?
4. Self-hosted vs cloud - which is better for our use case?
5. Can n8n handle real-time market data?

---

## Resources to Review

- n8n documentation: https://docs.n8n.io/
- n8n + Finance integrations
- n8n + Python/Flask integration patterns

---

*Do NOT implement this session. Research only in future session.*
