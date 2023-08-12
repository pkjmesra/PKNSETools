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
from datetime import datetime
import requests
import pandas as pd
from PKNSETools.PKConstants import _head, _base_domain, _quote_url_path_html, _chart_data_preopen_url, _chart_data_open_url,_chart_data_index_preopen_url,_chart_data_index_open_url

class Intra_Day:
    baseNumber = None
    session = None
    ticker = None

    def __init__(self, ticker):
        self.baseNumber = 0
        self.session = requests.session()
        self.ticker = ticker
        self.session.get(f'{_base_domain}', headers=_head)
        self.session.get(f'{_base_domain}{_quote_url_path_html}'.format(ticker), headers=_head)

    def _secondsTotime(self, seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return hour, minutes, seconds

    def _dateCalculator(self, num):
        if self.baseNumber == 0:
            self.baseNumber = (num // 100000) * 100000
        num = abs(num - self.baseNumber)
        num = num / 1000
        num = int(num)
        today = datetime.today()
        (h, m, s) = self._secondsTotime(num)
        return datetime(today.year, today.month, today.day, 9 + h, m, s)

    def intraDay(self,):
        preopen_url = f'{_base_domain}{_chart_data_preopen_url}'.format(self.ticker)
        open_url = f'{_base_domain}{_chart_data_open_url}'.format(self.ticker)
        preopen_webdata = self.session.get(url=preopen_url, headers=_head)
        opened_webdata = self.session.get(url=open_url, headers=_head)
        timestamp = []
        data = []
        ticks_list = []
        for (i, j) in preopen_webdata.json()['grapthData']:
            data.append(j)
            t = self._dateCalculator(i)
            timestamp.append(t)
            ticks_list.append({'Date':t,'LTP':j})

        for (i, j) in opened_webdata.json()['grapthData']:
            data.append(j)
            t = self._dateCalculator(i)
            timestamp.append(t)
            ticks_list.append({'Date':t,'LTP':j})
        return timestamp, data

    def nifty_intraDay(self):
        varient = self.ticker
        varient = varient.upper()
        varient = varient.replace(' ', '%20')
        varient = varient.replace('-', '%20')
        preopen_url = f'{_base_domain}{_chart_data_index_preopen_url}'.format(varient)
        open_url = f'{_base_domain}{_chart_data_index_open_url}'.format(varient)

        preopen_webdata = self.session.get(url=preopen_url, headers=_head)
        open_webdata = self.session.get(url=open_url, headers=_head)
        data = []
        timestamp = []
        ticks_list = []
        for (i, j) in preopen_webdata.json()['grapthData']:
            data.append(j)
            t = self._dateCalculator(i)
            timestamp.append(t)
            ticks_list.append({'Date':t,'LTP':j})

        for (i, j) in open_webdata.json()['grapthData']:
            data.append(j)
            t = self._dateCalculator(i)
            timestamp.append(t)
            ticks_list.append({'Date':t,'LTP':j})

        return timestamp, data, ticks_list, self._ohlc(ticks_list)

    def _ohlc(self,prices,interval='1Min'):
        # Convert the index to datetime
        df = pd.DataFrame(prices, columns = ['Date', 'LTP'])
        # df["Date"] = df["Date"].apply(lambda x: datetime.utcfromtimestamp(x/1000))
        df.set_index('Date', inplace=True)
        # Resample LTP column to interval bars using resample function from pandas
        resample_LTP = df.resample(interval).ohlc()['LTP']
        resample_LTP = resample_LTP.reset_index(drop=False)
        return resample_LTP

# ID = Intra_Day('SBINEQN')
# timeStamp, dataPoints,prices,ohlc = ID.nifty_intraDay()
# print(ID.ohlc(prices))
