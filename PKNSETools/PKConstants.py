#!/usr/bin/python3
"""
    The MIT License (MIT)

    Copyright (c) 2023 pkjmesra

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""
from PKDevTools.classes.Utils import random_user_agent

_base_domain = 'https://www.nseindia.com'
_autoComplete_url_path = '/api/search/autocomplete?q={}'
_quote_url_path= '/api/quote-equity?symbol={}'
# Board meetings, corporate actions, financial results, latest announcements, shareholding patterns, 
# https://www.nseindia.com/api/top-corp-info?symbol=SBIN&market=equities

# Bulk block deals, market dept order book/bid/ask, security wise DP
_quote_url_path_trade_info = f"{_quote_url_path}&section=trade_info&series=EQ"

# Equity meta data
# https://www.nseindia.com/api/equity-meta-info?symbol=SBIN
_daily_report_url_path = '/api/merged-daily-reports?key=favCapital'
_quote_url_path_html = '/get-quotes/equity?symbol={}'
_historical_company_data_url_path_html = '/api/historical/cm/equity?symbol={}'
_historical_company_data_url_path = '/api/historical/cm/equity?symbol={}&series=[%22EQ%22]&from={}&to={}&csv=true'
_historical_index_data_url_path = '/api/historical/indicesHistory?indexType={}&from={}&to={}'
_chart_data_preopen_url = '/api/chart-databyindex?index={}&preopen=true'
_chart_data_open_url = '/api/chart-databyindex?index={}'
_chart_data_index_preopen_url='/api/chart-databyindex?index={}&indices=true&preopen=true'
_chart_data_index_open_url='/api/chart-databyindex?index={}&indices=true'
_headers = {
    "user-agent": random_user_agent()
}
_head = {
    "user-agent": random_user_agent()
}