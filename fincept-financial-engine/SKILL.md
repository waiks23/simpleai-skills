---
name: fincept-financial-engine
description: Use FinceptTerminal analytics scripts as a local institutional financial intelligence engine
version: 1.1.0
category: finance
tags: [finance, markets, valuation, analytics, hedge-fund, json]
---

## When to Use

Use for:
- market quotes
- historical prices
- portfolio analytics
- company analysis
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

2. Call Fincept through the wrapper.

Commands:

cd ~/FinceptTerminal

List available analytics:

python3 fincept_engine.py list

Run analytics:

python3 fincept_engine.py run SCRIPT_NAME --args '{"key":"value"}'

3. Prefer verified low-dependency tools first:

- portfolioManagement/fetch_quotes
- portfolioManagement/fetch_historical

4. Parse returned JSON.

5. Combine Fincept output with:

- OpenBB
- Deep Research
- institutional-research-loop
- SEC/company filings
- earnings transcripts

6. Analysis format:

Always include:
- source used
- raw data summary
- thesis
- risks
- uncertainty
- next information needed

7. Failure rules:

If data fails:
- show exact error
- try another available source
- never replace missing data with guesses

## Examples

Quote request:

python3 fincept_engine.py run portfolioManagement/fetch_quotes --args '{"symbols":["AAPL","MSFT","NVDA"]}'

Historical request:

python3 fincept_engine.py run portfolioManagement/fetch_historical --args '{"symbols":["AAPL"],"period":"5d","interval":"1d"}'

