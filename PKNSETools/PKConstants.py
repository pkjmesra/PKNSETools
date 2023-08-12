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
_base_domain = 'https://www.nseindia.com'
_autoComplete_url_path = '/api/search/autocomplete?q={}'
_quote_url_path= '/api/quote-equity?symbol={}'
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
    "user-agent": "Chrome/87.0.4280.88"
}
_head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36 "
}