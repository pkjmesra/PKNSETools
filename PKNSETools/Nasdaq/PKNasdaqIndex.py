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
import pandas as pd

from PKDevTools.classes import Archiver
from PKDevTools.classes.log import default_logger
from PKDevTools.classes.Fetcher import fetcher
from PKDevTools.classes.Utils import random_user_agent
from PKDevTools.classes.CookieHelper import CookieHelper

class PKNasdaqIndexFetcher(fetcher):
    def __init__(self, configManager=None):
         super().__init__(configManager=configManager)
         self.cookieHelper = None
         self.defaultCookies = None
         self.defaultHeaders = {'user-agent' : random_user_agent()}
         self.refreshTokens()

    def fetchNasdaqIndexConstituents(self):
        listStockCodes = []
        
        url = "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=0&download=true"
        res = self.fetchURL(url, headers=self.defaultHeaders)
        df = None
        if res is None or res.status_code != 200:
            return listStockCodes
        try:
            json = res.json()
            if json is not None:
                 data = json["data"]
                 if data is not None:
                    rows = data["rows"]
                    if len(rows) > 0:
                        df = pd.DataFrame(rows)
                        return list(df["symbol"].values), df
        except Exception as e:
            default_logger().debug(e, exc_info=True)
        return listStockCodes,df

    def refreshTokens(self):
            if self.cookieHelper is None:
                self.cookieHelper = CookieHelper(download_folder=Archiver.get_user_cookies_dir(),
                                                    baseCookieUrl="https://www.nasdaq.com/market-activity/stocks/screener",
                                                    cookieStoreName="nda",
                                                    baseHtmlUrl="https://www.nasdaq.com/market-activity/stocks/screener",
                                                    htmlStoreName="nda")
            else:
                self.cookieHelper.resetCookies()
                self.cookieHelper.resetMetas()
            self.session.cookies.update(self.cookieHelper.cookies)
            self.defaultCookies = self.cookieHelper.cookies
