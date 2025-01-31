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
import os
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
from PKDevTools.classes.OutputControls import OutputControls

from PKNSETools.Benny.NSE import NSE
from PKDevTools.classes.Utils import random_user_agent

NSE_INDEX_MAP = {
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
    12: "https://archives.nseindia.com/content/equities/EQUITY_L.csv",
    14: "https://nsearchives.nseindia.com/content/fo/NSE_FO_SosScheme.csv",
}
REPO_INDEX_MAP = {
    1: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/ind_nifty50list.csv",
    2: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/ind_niftynext50list.csv",
    3: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/ind_nifty100list.csv",
    4: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/ind_nifty200list.csv",
    5: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/ind_nifty500list.csv",
    6: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/ind_niftysmallcap50list.csv",
    7: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/ind_niftysmallcap100list.csv",
    8: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/ind_niftysmallcap250list.csv",
    9: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/ind_niftymidcap50list.csv",
    10: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/ind_niftymidcap100list.csv",
    11: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/ind_niftymidcap150list.csv",
    12: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/EQUITY_L.csv",
    14: "https://raw.githubusercontent.com/pkjmesra/PKScreener/actions-data-download/results/Indices/NSE_FO_SosScheme.csv",
}

# This Class Handles Fetching of Stock Data over the internet from NSE/BSE

class nseStockDataFetcher(fetcher):

    def saveAllNSEIndices(self):
        for tickerOption in NSE_INDEX_MAP.keys():
            try:
                url = NSE_INDEX_MAP.get(tickerOption)
                fileName = url.split("/")[-1]
                filePath = os.path.join(Archiver.get_user_indices_dir(),fileName)
                self.fetchFileFromHostServer(filePath,tickerOption,"")
            except:
                continue

    def savedFileContents(self, fileName=None):
        data, filePath, modifiedDateTime = Archiver.findFileInAppResultsDirectory(directory=Archiver.get_user_indices_dir(), fileName=fileName)
        return data, filePath, modifiedDateTime

    def fetchFileFromHostServer(self,filePath,tickerOption,fileContents,indexMap=NSE_INDEX_MAP):
        try:
            url = indexMap.get(tickerOption)
            fileName = url.split("/")[-1]
            headers = {"user-agent": random_user_agent()}
            res = self.fetchURL(url,headers=headers,timeout=10)
            if res is None or res.status_code != 200:
                default_logger().debug(f"Response for tickerOption:{tickerOption}, file:{fileName}: {res}")
            else:
                fileContents = res.text
                with open(filePath, "w") as f:
                    f.write(fileContents)
        except:
            pass
        return fileContents

    def fetchNiftyCodes(self, tickerOption):
        listStockCodes = []
        url = NSE_INDEX_MAP.get(tickerOption)
        fileName = url.split("/")[-1]
        fileContents, filePath, modifiedDateTime = self.savedFileContents(fileName)
        shouldFetch = fileContents is None or (fileContents is not None and PKDateUtilities.currentDateTime().date() > modifiedDateTime.date())
        OutputControls().printOutput(colorText.BOLD + f"[+] {(len(fileContents.splitlines())-1) if fileContents is not None else 0} stocks loaded from local cache. {'Getting Stock Codes From NSE...' if shouldFetch else ''}")
        if shouldFetch:
            fileContents = self.fetchFileFromHostServer(filePath,tickerOption,fileContents)
        if fileContents is None:
            # Try and get it from our own repo
            fileContents = self.fetchFileFromHostServer(filePath,tickerOption,fileContents,REPO_INDEX_MAP)
            if fileContents is None:
                return listStockCodes

        if tickerOption == 12:
            try:
                data = pd.read_csv(StringIO(fileContents))
                return list(data["SYMBOL"].values)
            except Exception as e:
                default_logger().debug(e, exc_info=True)
                return listStockCodes
        try:
            cr = csv.reader(fileContents.strip().split("\n"))
            if tickerOption == 14:
                for i in range(2):
                    next(cr)  # skipping first two lines
                for row in cr:
                    listStockCodes.append(row[0])
                listStockCodes = sorted(list(filter(None,list(set(listStockCodes)))))
            else:
                next(cr)  # skipping first line
                for row in cr:
                    listStockCodes.append(row[2])
        except Exception as e:
            default_logger().debug(e, exc_info=True)
            pass

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
            listStockCodes = self.fetchNiftyCodes(tickerOption)
            if len(listStockCodes) > 10:
                OutputControls().printOutput(
                    colorText.GREEN
                    + ("=> Done! Fetched %d stock codes." % len(listStockCodes))
                    + colorText.END
                )
                if self.configManager.shuffleEnabled:
                    random.shuffle(listStockCodes)
                    OutputControls().printOutput(
                        colorText.BLUE
                        + "[+] Stock shuffling is active."
                        + colorText.END
                    )
                else:
                    OutputControls().printOutput(
                        colorText.FAIL
                        + "[+] Stock shuffling is inactive."
                        + colorText.END
                    )
                if self.configManager.stageTwo:
                    OutputControls().printOutput(
                        colorText.BLUE
                        + "[+] Screening only for the stocks in Stage-2! Edit User Config to change this."
                        + colorText.END
                    )
                else:
                    OutputControls().printOutput(
                        colorText.FAIL
                        + "[+] Screening only for the stocks in all Stages! Edit User Config to change this."
                        + colorText.END
                    )

            else:
                OutputControls().printOutput(
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
            nse  = NSE(Archiver.get_user_cookies_dir())
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
        # nse  = NSE(Archiver.get_user_cookies_dir())
        ticker = yf.Ticker(exchange) # ^IXIC
        try:
            info = ticker.info
        except Exception as e:
            default_logger().debug(e, exc_info=True)
            try:
                info = ticker.get_history_metadata()
            except:
                info = {"longName":exchange}
                pass
            pass
        try:
            history = ticker._lazy_load_price_history()
            if history is not None:
                history.history(period="1d",interval="1d",prepost=True, proxy=None)
            if history._history_metadata is not None:
                history._history_metadata["period"] = '5d' # Ignore the yfinance exception for period being 1wk.
        except:
            pass
        try:
            md = ticker.get_history_metadata()
            ltd = md["regularMarketTime"]
            ctp = md["currentTradingPeriod"]
            tzName = md["exchangeTimezoneName"]
            lastTradeDate = pd.to_datetime(ltd, unit='s', utc=True).tz_convert(tzName)
        except:
            tzName = "Asia/Kolkata"
            lastTradeDate = PKDateUtilities.currentDateTime()
            pass
        try:
            basicInfo = ticker.get_fast_info()
        except:
            basicInfo = {"last_price":0,"regular_market_previous_close":0}
            pass
        try:
            todayClose = pd.to_datetime(ctp["regular"]["end"], unit='s', utc=True).tz_convert(tzName)
            todayOpen = pd.to_datetime(ctp["regular"]["start"], unit='s', utc=True).tz_convert(tzName)
        except:
            todayClose = PKDateUtilities.currentDateTime()
            todayOpen = PKDateUtilities.currentDateTime()
            pass
        now = PKDateUtilities.currentDateTime().astimezone(tz=pytz.timezone(tzName))
        ts = datetime.datetime.timestamp(now)
        now = pd.to_datetime(ts, unit='s', utc=True).tz_convert(tzName)
        # isClosed = now < todayOpen and now < todayClose
        isOpen = now >= todayOpen and todayClose >= now
        status = "Open" if isOpen else "Closed"
        marketStatusLong = ""
        tradeDate = ""
        try:
            lastPrice = round(basicInfo["last_price"],2)
            prevClose = round(basicInfo["regular_market_previous_close"],2)
            if not pd.notna(prevClose):
                prevClose = md["previousClose"] if "previousClose" in md.keys() else prevClose
                if not pd.notna(prevClose):
                    prevClose = info["previousClose"] if "previousClose" in info.keys() else prevClose
                    if not pd.notna(prevClose):
                        prevClose = info["regularMarketPreviousClose"] if "regularMarketPreviousClose" in info.keys() else prevClose
            change = round(lastPrice - prevClose,2)
            pctChange = round(100*change/prevClose,2)
            tradeDate = lastTradeDate.strftime("%Y-%m-%d")
            
            if len(status) > 0:
                change = ((colorText.GREEN +colorText.UPARROW)if change >=0 else colorText.FAIL+colorText.DOWNARROW) + str(change if pd.notna(change) else "?") + colorText.END
                pctChange = (colorText.GREEN if pctChange >=0 else colorText.FAIL) + str(pctChange if pd.notna(pctChange) else "?") + colorText.END
                marketStatusLong = f'{info["longName"]} | {status} | {tradeDate} | {lastPrice} | {change} ({pctChange}%)'
        except:
            pass
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
