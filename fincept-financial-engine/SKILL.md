---
name: fincept-financial-engine
description: Use FinceptTerminal through Odysseus' native fincept tool or fincept_engine.py to fetch real financial JSON
version: 1.2.0
category: finance
tags: [finance, markets, valuation, analytics, hedge-fund, json, fincept]
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

## Core Rule

This skill must attempt Fincept execution first.

The skill fails if it uses:
- local notes
- markdown files
- cached fake data
- simulated prices
- invented quotes

Do not use recovery unless Fincept execution actually fails.

## Procedure

1. Call the native Odysseus `fincept` tool if available.

Tool input example:

script_name: portfolioManagement/fetch_quotes

args:
{"symbols":["AAPL","MSFT","NVDA"]}

2. If the native tool is unavailable, call the wrapper directly:

cd ~/FinceptTerminal

python3 fincept_engine.py run portfolioManagement/fetch_quotes --args '{"symbols":["AAPL","MSFT","NVDA"]}'

3. For historical data:

python3 fincept_engine.py run portfolioManagement/fetch_historical --args '{"symbols":["AAPL"],"period":"5d","interval":"1d"}'

4. Parse returned JSON.

5. Report:
- exact tool/command used
- returned data
- price
- previous close
- largest move if comparing symbols
- missing fields

6. If Fincept fails:
- show exact error
- then try OpenBB or Deep Research
- do not invent financial facts

## Success Condition

The skill succeeds only if:
- the native fincept tool was called successfully
or
- fincept_engine.py was executed successfully
or
- a real Fincept error was captured and reported

Local note recovery is not a valid success path for this skill.
