
# PKNSETools

[![MADE-IN-INDIA][MADE-IN-INDIA-badge]][MADE-IN-INDIA] [![PyPI][pypi-badge]][pypi] [![is wheel][wheel-badge]][pypi] ![github license][github-license]

A comprehensive Python library for fetching stock market data from the National Stock Exchange (NSE) of India and NASDAQ.

---

## Table of Contents

- [What is PKNSETools?](#what-is-pknsetools)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Architecture Overview](#architecture-overview)
- [Core Modules](#core-modules)
  - [NSE Stock Data Fetcher](#1-nse-stock-data-fetcher)
  - [NSE API (Benny)](#2-nse-api-benny)
  - [Intraday Data](#3-intraday-data)
  - [Historical Data](#4-historical-data)
  - [All Stocks Data](#5-all-stocks-data)
  - [NASDAQ Index](#6-nasdaq-index)
  - [Morningstar Tools](#7-morningstar-tools)
- [API Reference](#api-reference)
- [Index Maps](#index-maps)
- [Contributing](#contributing)
- [Related Projects](#related-projects)

---

## What is PKNSETools?

**PKNSETools** provides tools for fetching and analyzing stock market data from NSE India. Key features include:

- 📊 **Multi-Index Support** - Nifty 50, Nifty Next 50, Nifty 500, and more
- 🔄 **Real-Time Intraday Data** - Live market data during trading hours
- 📈 **Historical Data** - Up to 3 years of historical OHLCV data
- 🌐 **Multiple Sources** - NSE official API, archives, and GitHub cache
- 🚀 **High-Performance Integration** - Works with PKBrokers for real-time data
- 📱 **NASDAQ Support** - Fetch NASDAQ index data
- ⭐ **Morningstar Integration** - Fair value and stock ratings

This library is part of the [PKScreener](https://github.com/pkjmesra/PKScreener) ecosystem.

---

## Installation

### From PyPI

```bash
pip install PKNSETools
```

### From Source

```bash
git clone https://github.com/pkjmesra/PKNSETools.git
cd PKNSETools
pip install -r requirements.txt
pip install -e .
```

### Requirements

- Python 3.9+
- See `requirements.txt` for dependencies

---

## Quick Start

### Fetch Stock Data

```python
from PKNSETools import nseStockDataFetcher

# Initialize fetcher
fetcher = nseStockDataFetcher()

# Fetch OHLCV data for a stock
df = fetcher.fetchStockData(
    stockCode="RELIANCE",
    period="1y",       # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, max
    interval="1d"      # 1m, 5m, 15m, 30m, 60m, 1d, 1wk, 1mo
)

print(df.head())
```

### Get Index Constituents

```python
from PKNSETools import nseStockDataFetcher

fetcher = nseStockDataFetcher()

# Get Nifty 50 stocks
nifty50_stocks = fetcher.fetchStockCodes(1)  # 1 = Nifty 50

# Get all NSE stocks
all_stocks = fetcher.fetchStockCodes(12)  # 12 = All equities
```

### Use NSE API Directly

```python
from PKNSETools.Benny.NSE import NSE

nse = NSE(download_folder="./data")

# Get stock quote
quote = nse.quote("RELIANCE")
print(f"LTP: {quote['priceInfo']['lastPrice']}")

# Get option chain
chain = nse.optionChain("NIFTY")

# Get market status
status = nse.marketStatus()
```

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PKNSETools Architecture                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────┐         │
│  │                    Application Layer                           │         │
│  │              PKScreener | Custom Applications                  │         │
│  └─────────────────────────────┬──────────────────────────────────┘         │
│                                │                                             │
│  ┌─────────────────────────────▼──────────────────────────────────┐         │
│  │                  nseStockDataFetcher                           │         │
│  │    (Unified data fetcher with source auto-selection)           │         │
│  └─────────────────────────────┬──────────────────────────────────┘         │
│                                │                                             │
│       ┌────────────────────────┼────────────────────────┐                   │
│       │                        │                        │                   │
│  ┌────▼────┐           ┌───────▼───────┐        ┌───────▼───────┐          │
│  │PKBrokers│           │  NSE API      │        │ yfinance      │          │
│  │(Real-   │           │  (Official)   │        │ (Fallback)    │          │
│  │ time)   │           │               │        │               │          │
│  └─────────┘           └───────────────┘        └───────────────┘          │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────┐       │
│  │                      Core Modules                                 │       │
│  ├──────────────────────────────────────────────────────────────────┤       │
│  │  NSE (Benny)     │  Intra_Day    │  PKCompanyStock  │  PKAllStocks│       │
│  │  PKNasdaqIndex   │  Morningstar  │  PKCompanyGeneral              │       │
│  └──────────────────────────────────────────────────────────────────┘       │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────┐       │
│  │                      Data Sources                                 │       │
│  ├──────────────────────────────────────────────────────────────────┤       │
│  │  NSE India API   │  NSE Archives  │  GitHub Cache  │  yfinance   │       │
│  └──────────────────────────────────────────────────────────────────┘       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Core Modules

### 1. NSE Stock Data Fetcher

The main interface for fetching stock data with automatic source selection.

```python
from PKNSETools import nseStockDataFetcher

fetcher = nseStockDataFetcher()
```

#### `fetchStockData(stockCode, period, interval, start, end)`

Fetch OHLCV data for a stock.

**Parameters**:
- `stockCode` (str): NSE symbol (e.g., "RELIANCE", "TCS")
- `period` (str): Data period - "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "max"
- `interval` (str): Candle interval - "1m", "5m", "15m", "30m", "60m", "1d", "1wk", "1mo"
- `start` (datetime, optional): Start date
- `end` (datetime, optional): End date

**Returns**: `pd.DataFrame` with Date, Open, High, Low, Close, Volume columns

**Example**:
```python
# Last 1 year daily data
df = fetcher.fetchStockData("INFY", period="1y", interval="1d")

# Last 5 days 15-minute data
df = fetcher.fetchStockData("TCS", period="5d", interval="15m")

# Custom date range
from datetime import datetime
df = fetcher.fetchStockData(
    "HDFC",
    start=datetime(2024, 1, 1),
    end=datetime(2024, 6, 30),
    interval="1d"
)
```

#### Data Source Priority

1. **PKBrokers Real-time** (if available and market is open)
2. **NSE Official API** (primary source)
3. **yfinance** (fallback)

---

#### `fetchStockCodes(index, stockCode=None)`

Fetch stock codes for an index.

**Parameters**:
- `index` (int): Index identifier (see [Index Maps](#index-maps))
- `stockCode` (str, optional): Filter for specific stock

**Returns**: List of stock codes

**Example**:
```python
# Get Nifty 50 constituents
nifty50 = fetcher.fetchStockCodes(1)
print(f"Nifty 50 stocks: {len(nifty50)}")

# Get all NSE equities
all_stocks = fetcher.fetchStockCodes(12)
print(f"Total NSE stocks: {len(all_stocks)}")

# Get F&O stocks
fno_stocks = fetcher.fetchStockCodes(14)
```

---

#### `fetchLatestNiftyDaily(proxyServer=None)`

Fetch latest Nifty 50 index data.

**Returns**: `pd.DataFrame` with index data

---

#### `fetchNiftyCodes(niftyIndex, proxyServer=None)`

Fetch Nifty index constituents from GitHub cache.

---

### 2. NSE API (Benny)

Direct interface to NSE India's official API.

```python
from PKNSETools.Benny.NSE import NSE

nse = NSE(download_folder="./data")
```

#### Stock Quotes

```python
# Get detailed quote
quote = nse.quote("RELIANCE")
print(f"LTP: {quote['priceInfo']['lastPrice']}")
print(f"Change: {quote['priceInfo']['change']}")
print(f"% Change: {quote['priceInfo']['pChange']}%")

# Get quote with trade info
trade_info = nse.quote("TCS", trade_info=True)
```

#### Option Chain

```python
# Get option chain for index
chain = nse.optionChain("NIFTY")

# Get option chain for stock
chain = nse.optionChain("RELIANCE", optionType="stock")

# Available indices: banknifty, nifty, finnifty, niftyit
```

#### Market Data

```python
# Market status
status = nse.marketStatus()

# Trading holidays
holidays = nse.holidays()

# Advances/Declines
advances = nse.advanceDecline()

# Pre-open market data
preopen = nse.preOpen()

# Market turnover
turnover = nse.marketTurnover()
```

#### Index Data

```python
# Get all indices
indices = nse.allIndices()

# Get specific index data
nifty50 = nse.indexData("NIFTY 50")

# Get index constituents
constituents = nse.indexStocks("NIFTY 50")
```

#### Block/Bulk Deals

```python
# Block deals
block = nse.blockDeal()

# Bulk deals
bulk = nse.bulkDeal()
```

#### Historical Data

```python
# Get historical data
history = nse.equityHistory(
    symbol="RELIANCE",
    series="EQ",
    from_date="01-01-2024",
    to_date="30-06-2024"
)
```

#### Download Reports

```python
# Download bhavcopy
nse.bhavCopyFull(date="2024-12-20")

# Download index report
nse.indexReport(date="2024-12-20")
```

---

### 3. Intraday Data

Real-time intraday data during market hours.

```python
from PKNSETools import Intra_Day

# Initialize for a stock
intraday = Intra_Day("RELIANCE")

# Get intraday data (9:00 AM to now)
timestamps, prices = intraday.intraDay()

# For NIFTY indices
nifty_intra = Intra_Day("NIFTY 50")
timestamps, prices = nifty_intra.nifty_intraDay()
```

#### Features

- Rate-limited (3 requests/second)
- Session-based with cookie handling
- Works during market hours (9:15 AM - 3:30 PM IST)

---

### 4. Historical Data

Fetch up to 3 years of historical data.

```python
from PKNSETools import get_Company_History_Data, get_nifty_History_Data

# Company historical data
df = get_Company_History_Data(
    company="RELIANCE",
    from_date="01-01-2023",
    to_date="31-12-2023"
)

# Nifty index historical data
df = get_nifty_History_Data(
    indexName="NIFTY 50",
    from_date="01-01-2023",
    to_date="31-12-2023"
)
```

---

### 5. All Stocks Data

Fetch daily report for all stocks.

```python
from PKNSETools import getTodayData

# Get today's data for all stocks
nifty_data, companies_data = getTodayData()

# Returns tuple:
# - nifty_data: NIFTY index performance
# - companies_data: All company data with OHLCV, volume, etc.
```

---

### 6. NASDAQ Index

Fetch NASDAQ index data.

```python
from PKNSETools.Nasdaq.PKNasdaqIndex import PKNasdaqIndex

nasdaq = PKNasdaqIndex()

# Get NASDAQ-100 constituents
constituents = nasdaq.get_nasdaq100()

# Get NASDAQ Composite data
composite = nasdaq.get_nasdaq_composite()
```

---

### 7. Morningstar Tools

Integration with Morningstar for fundamental data.

```python
from PKNSETools.morningstartools import PKMorningstarDataFetcher

# Initialize fetcher
ms = PKMorningstarDataFetcher()

# Get stock fair value
fair_value = ms.get_fair_value("RELIANCE")

# Get stock rating
rating = ms.get_stock_rating("TCS")

# Get mutual fund data
mf_data = ms.get_mutual_fund("HDFC Equity Fund")
```

#### Available Data

- Fair value estimates
- Star ratings
- Analyst reports
- Financial ratios
- Mutual fund performance

---

## API Reference

### Main Exports

```python
from PKNSETools import (
    # Stock Data
    nseStockDataFetcher,
    
    # Historical Data
    get_Company_History_Data,
    get_nifty_History_Data,
    
    # Intraday
    Intra_Day,
    
    # All Stocks
    getTodayData,
    
    # Constants
    NSE_INDEX_MAP,
    REPO_INDEX_MAP,
)

from PKNSETools.Benny.NSE import NSE

from PKNSETools.Nasdaq.PKNasdaqIndex import PKNasdaqIndex

from PKNSETools.morningstartools import PKMorningstarDataFetcher
```

### Module Structure

```
PKNSETools/
├── __init__.py                 # Main exports
├── PKAllStocks.py              # All stocks daily data
├── PKCompanyGeneral.py         # Company general info
├── PKCompanyStock.py           # Company historical data
├── PKConstants.py              # URL constants and headers
├── PKIntraDay.py               # Intraday data
├── PKNSEStockDataFetcher.py    # Main stock data fetcher
├── Benny/
│   ├── __init__.py
│   └── NSE.py                  # NSE API wrapper
├── Nasdaq/
│   ├── __init__.py
│   └── PKNasdaqIndex.py        # NASDAQ index tools
└── morningstartools/
    ├── __init__.py
    ├── PKMorningstarDataFetcher.py
    ├── funds.py                # Mutual fund data
    ├── stock.py                # Stock fundamental data
    ├── security.py             # Security data
    ├── search.py               # Search functionality
    ├── NSEStockDB.py           # Stock database
    ├── NSEStockFairValueDB.py  # Fair value database
    └── NSEStockMFIDB.py        # MFI database
```

---

## Index Maps

### NSE_INDEX_MAP (Direct NSE URLs)

| Index | Description | URL |
|-------|-------------|-----|
| 1 | Nifty 50 | `ind_nifty50list.csv` |
| 2 | Nifty Next 50 | `ind_niftynext50list.csv` |
| 3 | Nifty 100 | `ind_nifty100list.csv` |
| 4 | Nifty 200 | `ind_nifty200list.csv` |
| 5 | Nifty 500 | `ind_nifty500list.csv` |
| 6 | Nifty Smallcap 50 | `ind_niftysmallcap50list.csv` |
| 7 | Nifty Smallcap 100 | `ind_niftysmallcap100list.csv` |
| 8 | Nifty Smallcap 250 | `ind_niftysmallcap250list.csv` |
| 9 | Nifty Midcap 50 | `ind_niftymidcap50list.csv` |
| 10 | Nifty Midcap 100 | `ind_niftymidcap100list.csv` |
| 11 | Nifty Midcap 150 | `ind_niftymidcap150list.csv` |
| 12 | All Equities | `EQUITY_L.csv` |
| 14 | F&O Stocks | `NSE_FO_SosScheme.csv` |

### REPO_INDEX_MAP (GitHub Cache)

Same indices but fetched from PKScreener's GitHub repository for reliability.

---

## Constants

```python
from PKNSETools.PKConstants import (
    _base_domain,           # "https://www.nseindia.com"
    _headers,               # Default request headers
    _head,                  # Headers with cookies
    _quote_url_path,        # Quote API path
    _chart_data_open_url,   # Chart data URL
)
```

---

## Contributing

### Development Setup

```bash
git clone https://github.com/pkjmesra/PKNSETools.git
cd PKNSETools
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

### Running Tests

```bash
pytest test/
```

### Code Style

```bash
ruff check PKNSETools/
ruff format PKNSETools/
```

---

## Related Projects

- [PKScreener](https://github.com/pkjmesra/PKScreener) - Stock screening application
- [PKDevTools](https://github.com/pkjmesra/PKDevTools) - Common development tools
- [PKBrokers](https://github.com/pkjmesra/PKBrokers) - Broker integration and real-time data

---

## License

MIT License - see [LICENSE](LICENSE) file.

---

## Disclaimer

This library is for educational and research purposes only. Always verify data accuracy before making investment decisions. The authors are not responsible for any financial losses incurred through the use of this software.

---

[MADE-IN-INDIA-badge]: https://img.shields.io/badge/MADE%20WITH%20%E2%9D%A4%20IN-INDIA-orange
[MADE-IN-INDIA]: https://en.wikipedia.org/wiki/India
[pypi-badge]: https://img.shields.io/pypi/v/pknsetools.svg?style=flat-square
[pypi]: https://pypi.python.org/pypi/pknsetools
[wheel-badge]: https://img.shields.io/pypi/wheel/pknsetools.svg?style=flat-square
[github-license]: https://img.shields.io/github/license/pkjmesra/PKNSETools
