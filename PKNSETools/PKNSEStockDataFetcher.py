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
import csv
import datetime
import pytz
import random
import warnings
from io import StringIO

warnings.simplefilter("ignore", DeprecationWarning)
warnings.simplefilter("ignore", FutureWarning)
import pandas as pd
import yfinance as yf
from PKDevTools.classes import Archiver
from PKDevTools.classes.ColorText import colorText
from PKDevTools.classes.PKDateUtilities import PKDateUtilities
from PKDevTools.classes.Fetcher import fetcher
from PKDevTools.classes.log import default_logger

from PKNSETools.Benny.NSE import NSE
from PKDevTools.classes.Utils import random_user_agent

# This Class Handles Fetching of Stock Data over the internet from NSE/BSE

class nseStockDataFetcher(fetcher):

    def fetchNiftyCodes(self, tickerOption):
        listStockCodes = []
        if tickerOption == 12:
            url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
            res = self.fetchURL(url)
            if res is None or res.status_code != 200:
                return listStockCodes
            try:
                data = pd.read_csv(StringIO(res.text))
                return list(data["SYMBOL"].values)
            except Exception as e:
                default_logger().debug(e, exc_info=True)
                return listStockCodes
            
        tickerMapping = {
            1: "https://archives.nseindia.com/content/indices/ind_nifty50list.csv",
            2: "https://archives.nseindia.com/content/indices/ind_niftynext50list.csv",
            3: "https://archives.nseindia.com/content/indices/ind_nifty100list.csv",
            4: "https://archives.nseindia.com/content/indices/ind_nifty200list.csv",
            5: "https://archives.nseindia.com/content/indices/ind_nifty500list.csv",
            6: "https://archives.nseindia.com/content/indices/ind_niftysmallcap50list.csv",
            7: "https://archives.nseindia.com/content/indices/ind_niftysmallcap100list.csv",
            8: "https://archives.nseindia.com/content/indices/ind_niftysmallcap250list.csv",
            9: "https://archives.nseindia.com/content/indices/ind_niftymidcap50list.csv",
            10: "https://archives.nseindia.com/content/indices/ind_niftymidcap100list.csv",
            11: "https://archives.nseindia.com/content/indices/ind_niftymidcap150list.csv",
            14: "https://archives.nseindia.com/content/fo/fo_mktlots.csv",
        }

        url = tickerMapping.get(tickerOption)

        try:
            res = self.fetchURL(url)
            if res is None or res.status_code != 200:
                return listStockCodes
            cr = csv.reader(res.text.strip().split("\n"))

            if tickerOption == 14:
                for i in range(5):
                    next(cr)  # skipping first line
                for row in cr:
                    listStockCodes.append(row[1])
            else:
                next(cr)  # skipping first line
                for row in cr:
                    listStockCodes.append(row[2])
        except Exception as e:
            default_logger().debug(e, exc_info=True)

        return listStockCodes

    # Fetch all stock codes from NSE
    def fetchStockCodes(self, tickerOption, stockCode=None):
        listStockCodes = []
        if tickerOption == 0:
            stockCode = None
            while stockCode is None or stockCode == "":
                stockCode = str(
                    input(
                        colorText.BOLD
                        + colorText.FAIL
                        + "[+] Enter Stock Code(s) for screening (Multiple codes should be seperated by ,): "
                    )
                ).upper()
            stockCode = stockCode.replace(" ", "")
            listStockCodes = stockCode.split(",")
        else:
            print(colorText.BOLD + "[+] Getting Stock Codes From NSE... ", end="")
            listStockCodes = self.fetchNiftyCodes(tickerOption)
            if len(listStockCodes) > 10:
                print(
                    colorText.GREEN
                    + ("=> Done! Fetched %d stock codes." % len(listStockCodes))
                    + colorText.END
                )
                if self.configManager.shuffleEnabled:
                    random.shuffle(listStockCodes)
                    print(
                        colorText.BLUE
                        + "[+] Stock shuffling is active."
                        + colorText.END
                    )
                else:
                    print(
                        colorText.FAIL
                        + "[+] Stock shuffling is inactive."
                        + colorText.END
                    )
                if self.configManager.stageTwo:
                    print(
                        colorText.BLUE
                        + "[+] Screening only for the stocks in Stage-2! Edit User Config to change this."
                        + colorText.END
                    )
                else:
                    print(
                        colorText.FAIL
                        + "[+] Screening only for the stocks in all Stages! Edit User Config to change this."
                        + colorText.END
                    )

            else:
                print(
                    colorText.FAIL
                    + "=> Error getting stock codes from NSE!"
                    + colorText.END
                )

        return listStockCodes

    def savedholidaysRaw(self, exchange="NSE"):
        url = "https://raw.githubusercontent.com/pkjmesra/PKScreener/main/.github/dependencies/nse-holidays.json"
        headers = {"user-agent": random_user_agent()}
        res = self.fetchURL(url,headers=headers)
        if res is None or res.status_code != 200:
            return [], []
        try:
            cm = res.json()['CM'] # CM = Capital Markets
            lastYear = int(datetime.datetime.today().year) - 1
            cm_lastyear = res.json()[f'CM{lastYear}']
            return cm, cm_lastyear, res.json()
        except Exception as e:
            default_logger().debug(e, exc_info=True)
            return [], []
        
    def holidayList(self, exchange="NSE"):
        try:
            cm = self.savedholidaysRaw()[0]
            df = pd.DataFrame(cm)
            df = df[['tradingDate', 'weekDay', 'description']]
            df.loc[:, 'description'] = df.loc[:, 'description'].apply(
                    lambda x: x.replace('\r','')
                )
            return df
        except Exception as e:
            default_logger().debug(e, exc_info=True)
            return None
    
    def isTodayHoliday(self,exchange="NSE",today=None):
        """
        today must be in "%d-%b-%Y" format
        """
        holidays = self.holidayList()
        if holidays is None:
            return False, None
        
        if today is None:
            today = PKDateUtilities.currentDateTime().strftime("%d-%b-%Y")
        occasion = None
        for holiday in holidays['tradingDate']:
            if today in holiday:
                occasion = holidays[holidays['tradingDate']==holiday]['description'].iloc[0]
                break
        return occasion is not None, occasion

    def updatedHolidays(self):
        cm_holidays = None
        cm = None
        try:
            cm,cm_lastyear,raw = self.savedholidaysRaw()
            nse  = NSE(Archiver.get_user_outputs_dir())
            holidays = nse.holidays()
            cm_holidays = holidays["CM"]
        except Exception as e:
            default_logger().debug(e, exc_info=True)
            if cm_holidays is None or len(cm_holidays) < 1:
                cm_holidays = cm
            pass
        cm_holidays.extend(cm_lastyear)
        raw["CM"] = cm_holidays
        return cm_holidays, raw

    def capitalMarketStatus(self, exchange="^NSEI"):
        # nse  = NSE(Archiver.get_user_outputs_dir())
        ticker = yf.Ticker(exchange) # ^IXIC
        info = ticker.info
        md = ticker.get_history_metadata()
        ltd = md["regularMarketTime"]
        ctp = md["currentTradingPeriod"]
        tzName = md["exchangeTimezoneName"]
        lastTradeDate = pd.to_datetime(ltd, unit='s', utc=True).tz_convert(tzName)
        basicInfo = ticker.get_fast_info()
        todayClose = pd.to_datetime(ctp["regular"]["end"], unit='s', utc=True).tz_convert(tzName)
        todayOpen = pd.to_datetime(ctp["regular"]["start"], unit='s', utc=True).tz_convert(tzName)
        now = PKDateUtilities.currentDateTime().astimezone(tz=pytz.timezone(tzName))
        ts = datetime.datetime.timestamp(now)
        now = pd.to_datetime(ts, unit='s', utc=True).tz_convert(tzName)
        # isClosed = now < todayOpen and now < todayClose
        isOpen = now >= todayOpen and todayClose >= now
        status = "Open" if isOpen else "Closed"
        lastPrice = round(basicInfo["last_price"],2)
        prevClose = round(basicInfo["previous_close"],2)
        change = round(lastPrice - prevClose,2)
        pctChange = round(100*change/prevClose,2)
        tradeDate = lastTradeDate.strftime("%Y-%m-%d")
        
        if len(status) > 0:
            change = ((colorText.GREEN +"▲")if change >=0 else colorText.FAIL+"▼") + str(change) + colorText.END
            pctChange = (colorText.GREEN if pctChange >=0 else colorText.FAIL) + str(pctChange) + colorText.END
            marketStatusLong = f'{info["longName"]} | {status} | {tradeDate} | {lastPrice} | {change} ({pctChange}%)'
        return status, marketStatusLong,tradeDate

# f = nseStockDataFetcher()
# f.capitalMarketStatus(exchange="^NSEI")


# from yfinhanced import YFClient
# import pandas as pd
# import numpy as np
# import json

# yf = YFClient()
# # await yf.connect()

# # x = await yf.get_quote('AAPL')


# x = yf.get_price_history('SPY', start=pd.to_datetime('2021-01-01', utc=True), 
#         end=pd.to_datetime('today', utc=True), interval='1d', adjust=True)

# from yfinhanced import YFWSClient
# import aiohttp
# from google.protobuf.json_format import MessageToDict
# import asyncio
# import signal


# data = {}
# async def on_message(msg):
#     # with lock:
#     if msg['symbol'] not in data.keys():
#         data[msg['symbol']] = []
#     data[msg['symbol']] += [msg]
#     print(msg)

# yfws = YFWSClient()
# loop = asyncio.get_event_loop()
# # loop.create_task(yfws.start())
# # loop.create_task(yfws.subscribe('BTC-USD'))
# loop.create_task(yf.connect())
# loop.create_task(yf.get_price_history('^NSEI', start=PKDateUtilities.currentDateTime(), 
#         end=PKDateUtilities.currentDateTime(), interval='1d', adjust=False))

# async def sub2(cb):# {{{
#     await asyncio.sleep(5)
#     await yfws.disconnect()
#     await asyncio.sleep(3)
#     loop = asyncio.get_event_loop()
#     await asyncio.gather(yfws.start(), yfws.subscribe('AAPL'))# }}}

# yfws.on_message = on_message

# for s in [signal.SIGHUP, signal.SIGTERM, signal.SIGINT]:
#     loop.add_signal_handler(s, lambda s=s: asyncio.create_task(yfws.shutdown()))

# try:
#     loop.run_forever()
# finally:
#     loop.close()
