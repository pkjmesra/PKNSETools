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
from time import sleep
from datetime import datetime
from mthrottle import Throttle

import pandas as pd
import requests
from PKDevTools.classes.OutputControls import OutputControls

from PKNSETools.PKConstants import (_base_domain, _chart_data_index_open_url,
                                    _chart_data_index_preopen_url,
                                    _chart_data_open_url,
                                    _chart_data_preopen_url, _head,
                                    _quote_url_path_trade_info,
                                    _quote_url_path,
                                    _quote_url_path_html)

throttleConfig = {
    'default': {
        'rps': 3,
    },
}
MAX_PENALTY_COUNT = 1
MIN_PENALTY_WAIT_SECONDS = 10
th = Throttle(throttleConfig, MAX_PENALTY_COUNT)

class Intra_Day:
    baseNumber = None
    session = None
    ticker = None

    def __init__(self, ticker:str):
        self.baseNumber = 0
        self.session = requests.session()
        self.ticker = ticker if ticker.upper().endswith("EQN") else f"{ticker}EQN"
        self.symbol = self.ticker[0:-3]
        # self.session.get(f'{_base_domain}', headers=_head)
        if len(self.session.cookies.keys()) == 0:
            self.session.get(f'{_base_domain}{_quote_url_path_html}'.format(ticker), headers=_head, timeout=10)

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

    def order_trade_info(self):
        open_url = f'{_base_domain}{_quote_url_path_trade_info}'.format(self.symbol)
        tradeInfoDict = {
                            "Stock": self.symbol,
                            "BidQty": 0,
                            "AskQty": 0,
                            "DayVola": 0,
                            "YrVola": 0,
                            "MktCap(Cr)": 0,
                            "FFMCap(Cr)": 0,
                            "DelQty": 0,
                            "Del(%)": 0,
                        }
        trade_df = pd.DataFrame([tradeInfoDict])
        try:
            trade_info = self.session.get(url=open_url, headers=_head)
            if trade_info.status_code == 429 or trade_info.status_code == 403:
                OutputControls().printOutput(f"{trade_info.status_code}: {trade_info.text}")
                if (th.penalize()):
                    sleep(MIN_PENALTY_WAIT_SECONDS)
                    th.maxPenaltyCount += MAX_PENALTY_COUNT
            tradeInfoDict = trade_info.json()
            mCap = tradeInfoDict["marketDeptOrderBook"]["tradeInfo"]["totalMarketCap"]
            if mCap >= 1000000:
                mCap = f"{int(mCap/1000000)}M"
            elif mCap >= 1000:
                mCap = f"{int(mCap/1000)}k"
            ffmc = tradeInfoDict["marketDeptOrderBook"]["tradeInfo"]["ffmc"]
            if ffmc >= 1000000:
                ffmc = f"{int(ffmc/1000000)}M"
            elif ffmc >= 1000:
                ffmc = f"{int(ffmc/1000)}k"
            tradeInfoDict = {
                                "Stock": self.symbol,
                                "BidQty": tradeInfoDict["marketDeptOrderBook"]["totalBuyQuantity"],
                                "AskQty": tradeInfoDict["marketDeptOrderBook"]["totalSellQuantity"],
                                "DayVola": tradeInfoDict["marketDeptOrderBook"]["tradeInfo"]["cmDailyVolatility"],
                                "YrVola": tradeInfoDict["marketDeptOrderBook"]["tradeInfo"]["cmAnnualVolatility"],
                                "MktCap(Cr)": mCap,
                                "FFMCap(Cr)": ffmc,
                                "DelQty": tradeInfoDict["securityWiseDP"]["deliveryQuantity"],
                                "Del(%)": tradeInfoDict["securityWiseDP"]["deliveryToTradedQuantity"],
                            }
            trade_df = pd.DataFrame([tradeInfoDict])
        except:
            pass
        return trade_df

    def price_info(self):
        get_details = f'{_base_domain}{_quote_url_path}'
        priceInfoDict = {
                "Stock": self.symbol,
                "LTP": 0,
                "%Chng": 0,
                "VWAP": 0,
                "LwrCP": 0,
                "UprCP": 0,
            }
        trade_df = pd.DataFrame([priceInfoDict])
        try:
            info = self.session.get(url=get_details.format(self.symbol), headers=_head)
            if info.status_code == 429 or info.status_code == 403:
                OutputControls().printOutput(f"{info.status_code}: {info.text}")
                if (th.penalize()):
                    sleep(MIN_PENALTY_WAIT_SECONDS)
                    th.maxPenaltyCount += MAX_PENALTY_COUNT
            priceInfo = info.json()["priceInfo"]
            priceInfoDict = {
                "Stock": self.symbol,
                "LTP": priceInfo["lastPrice"],
                "%Chng": round(priceInfo["pChange"],2),
                "VWAP": priceInfo["vwap"],
                "LwrCP": priceInfo["lowerCP"],
                "UprCP": priceInfo["upperCP"],
            }
            trade_df = pd.DataFrame([priceInfoDict])
        except:
            pass
        return trade_df
    
    def price_order_info(self):
        th.check()
        priceOrder_df = None
        if th._penaltyCount >= MAX_PENALTY_COUNT:
            return None
        priceInfo = self.price_info()
        tradeInfo = self.order_trade_info()
        if priceInfo is not None:
            priceOrder_df = priceInfo.merge(tradeInfo, on='Stock', how='inner')
        elif tradeInfo is not None:
            priceOrder_df
        return priceOrder_df

# i = 0
# while i <= 100: 
#     ID = Intra_Day('SBINEQN')
#     ti = ID.price_order_info()
#     print(ti)
#     i += 1

# ID.symbol = "BANKINDIA"
# ti = ID.order_trade_info()
# print(ti)
# timeStamp, dataPoints,prices,ohlc = ID.nifty_intraDay()
# print(ID.ohlc(prices))

# import requests
# import lxml.html

# url = 'https://www.nseindia.com/get-quotes/equity?symbol=SBIN&series=EQ'

# r = requests.get(url,headers=_head)
# soup = lxml.html.fromstring(r.text)

# items = soup.xpath('/html/body/div[11]/div/div/section/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/i/span')
# #items = [x.text for x in items]
# print(items)