---
name: fincept-financial-engine
description: Use FinceptTerminal analytics scripts as a local financial intelligence engine
version: 1.0.0
category: finance
tags: [finance, markets, valuation, analytics, hedge-fund, json]
---

## When to Use

Use for:
- market quotes
- historical prices
- portfolio analytics
- financial research
- investment memos
- hedge-fund style analysis

## Procedure

1. Use real data only.

Never invent:
- prices
- OHLCV
- ratios
- earnings
- news

2. Call Fincept through the wrapper:

cd ~/FinceptTerminal

python3 fincept_engine.py list

python3 fincept_engine.py run SCRIPT_NAME --args '{"key":"value"}'

3. Prefer low-dependency scripts first:
- portfolioManagement/fetch_quotes
- portfolioManagement/fetch_historical

4. Parse returned JSON.

5. Combine Fincept data with:
- OpenBB
- Deep Research
- institutional-research-loop

6. If data fails:
- report the exact error
- do not simulate financial facts
- suggest next source

## Example Commands

Get quotes:

python3 fincept_engine.py run portfolioManagement/fetch_quotes --args '{"symbols":["AAPL","MSFT","NVDA"]}'

Get historical data:

python3 fincept_engine.py run portfolioManagement/fetch_historical --args '{"symbols":["AAPL"],"period":"5d","interval":"1d"}'
