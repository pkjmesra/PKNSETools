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
from PKNSETools.morningstartools.security import Security, DUMMY_SECURITY
import pandas as pd
from PKDevTools.classes.CookieHelper import CookieHelper
from PKDevTools.classes import Archiver
from PKDevTools.classes.Fetcher import session
from PKDevTools.classes.log import default_logger
from PKNSETools.morningstartools.NSEStockMFIDB import NSEStockMFIDB
from PKNSETools.morningstartools.NSEStockFairValueDB import NSEStockFairValueDB
from PKDevTools.classes.PKDateUtilities import PKDateUtilities

class Stock(Security):
    """
    Main class to access data about stocks, inherit from Security class
    Args:
        term (str): text to find a stock, can be a name, part of a name or the isin of the stocks
        pageSize (int): number of stocks to return
        itemRange (int) : index of stocks to return (must be inferior to PageSize)
        proxies = (dict) : set the proxy if needed , example : {"http": "http://host:port","https": "https://host:port"}

    Examples:
        >>> Stocks('0P0000712R', 9, 0)
        >>> Stocks('visa')

    Raises:
        TypeError: raised whenever the parameter type is not the type expected
        ValueError : raised whenever the parameter is not valid or no stock found

    """

    def __init__(self, term = None, exchange: str = "INDIA", pageSize : int =1, itemRange: int = 0, filters: dict = {}, proxies: dict = {}):
        
        super().__init__(term=term,asset_type='stock',exchange=exchange,pageSize=pageSize,itemRange=itemRange,filters=filters,proxies=proxies)
        self.cookieHelper = None
        self.defaultHeaders = Stock.morningstarDefaultHeaders()
        self.defaultParams = Stock.morningstarDefaultParams()
        self.defaultCookies = None
        self.refreshMorningstarTokens(self.defaultParams, self.defaultHeaders)

    @staticmethod
    def morningstarDefaultParams():
        params = {
            "secExchangeList": "",
            "locale" :"en",
            "languageId": "en",
            "clientId":"RSIN_SAL",
            "version":"4.13.0",
            "access_token":"OAg7sEUU8PQ1V8pyXApDCAyzuxqr",
            }
        return params
    
    @staticmethod
    def morningstarDefaultHeaders():
        headers = {
            "X-Api-Realtime-E": "ew0KICAiYWxnIjogIlJTQS1PQUVQIiwNCiAgImVuYyI6ICJBMTI4R0NNIg0KfQ.W4pGZbjPWyUkcwcaGY39TU2293P-E7Sy_LYI_8-h-HFUFEDSbM1Li7c4D880QOw-jQPxXdOirJIMn1bj6px4kd3Bsij5jal16cFJjtwLbCdZ_ONVUywlZLhfKHeOfaXlZCQrN6HAi9l49-iYHWAfryiAVrYTm5WIseP1inRkopg.1fPJ5lD9xM0wnRSM.8NzTksDBHjQpQMFIbImiQz6HAVLhqNNIm8rKFQ3LojEEOyB8Q9vTbMQy3bABMRv4rnahT1uI51cJlg9Fv2rilCUsBskNTDRkAh02TVHCE4z7PKOCWWWdzlNt-Yh195MhQq1Vras4_PCmkCBdEKkY8ooF5-D8kEUWl_LXy6dUj4ytvy7wGMLxMp6pgWAHMLBPW9PxAlKGWZAHs0x7qm1TIlF4M5WAdKBE4d69hyaMFqIEoNmqjnx_1sMdnTNgVK2KBgHdn007.pW2CchSpaWFh95YttagfLg",
            "X-Sal-Contenttype": "nNsGdN3REOnPMlKDShOYjlk6VYiEVLSdpfpXAm7o2Tk="
        }
        return headers

    def needsNetworkRequest(self, dbClass:None):
        # Let's check when the last network call was made. If it was today, there's no point going again!
        latestCheckedOnDate = dbClass.searchCache(ticker=DUMMY_SECURITY)
        tradingDate = PKDateUtilities.tradingDate().strftime("%Y-%m-%d")
        if latestCheckedOnDate is not None and len(latestCheckedOnDate) > 0 and DUMMY_SECURITY in latestCheckedOnDate.keys():
            latestDate = latestCheckedOnDate[DUMMY_SECURITY]
            if latestDate == tradingDate:
                return False
        if self.term == DUMMY_SECURITY or self.ticker == DUMMY_SECURITY:
            # The caller wants us to save the LatestCheckedOnDate. This should be done at the end after 
            # all the rest of the stock searches has been made.
            dbClass.saveCache(ticker=DUMMY_SECURITY, stockDict={DUMMY_SECURITY:tradingDate})
            return False
        return True
    
    def analysisData(self):
        """
        This function retrieves general data about the stock.

        Returns:
            dict with general data about stock

        Examples:
            >>> Stock("visa", exchange="nyse").analysisData()

        """
        return self.GetData("morningstarTake/v3",url_suffixe='analysisData')
    
    def analysisReport(self):
        """
        This function retrieves the analysis of the stock.

        Returns:
            dict with analyst overview

        Examples:
            >>> Stock("visa", exchange="nyse").analysisReport()

        """
        return self.GetData("morningstarTake/v4",url_suffixe='analysisReport')
    
    def balanceSheet(self, period='annual', reportType='original'):
        """
        This function retrieves the balance sheet.

        Args:
            period (str) : possible values are annual, quarterly
            reportType (str) : possible values are original, restated

        Returns:
            dict with balance sheet

        Examples:
            >>> Stock("visa", exchange="nyse").balanceSheet('quarterly', 'original')
            >>> Stock("visa", exchange="nyse").balanceSheet('annual', 'restated')

        """

        return self.financialStatement("balancesheet",period=period, reportType=reportType)
    
    def boardOfDirectors(self):
        """
        This function retrieves information about the board of directors.

        Returns:
            dict with board of directors information

        Examples:
            >>> Stock("Alphabet Inc Class A").boardOfDirectors()
    
        """
        return self.GetData("insiders/boardOfDirectors")

    def cashFlow(self, period='annual', reportType='original'):
        """
        This function retrieves the cash flow.

        Args:
            period (str) : possible values are annual, quarterly
            reportType (str) : possible values are original, restated

        Returns:
            dict with cash flow

        Examples:
            >>> Stock("visa", exchange="nyse").cashFlow('annual', 'restated')
            >>> Stock("visa", exchange="nyse").cashFlow('quarterly', 'restated')

        """

        return self.financialStatement("cashflow",period=period, reportType=reportType)
    
    def dividends(self):
        """
        This function retrieves the dividends of the stock.

        Returns:
            dict with dividends

        Examples:
            >>> Stock("visa", exchange="nyse").dividends()

        """
        return self.GetData("dividends/v4")
    
    def esgRisk(self):
        """
        This function retrieves the esg risk of the stock.

        Returns:
            dict with esg risk

        Examples:
            >>> Stock("visa", exchange="nyse").esgRisk()

        """
        return self.GetData("esgRisk")
    
    def financialHealth(self):
        """
        This function retrieves the financial health of the stock.

        Returns:
            dict with financial health

        Examples:
            >>> Stock("visa", exchange="nyse").financialHealth()

        """
        return self.GetData("keyStats/financialHealth", url_suffixe='')
    
    def financialStatement(self,statement ='summary', period='annual', reportType='original'):
        """
        This function retrieves the financial statement.

        Args:
            statement (str) : possible values are balancesheet, cashflow, incomestatement, summary
            period (str) : possible values are annual, quarterly
            reportType (str) : possible values are original, restated

        Returns:
            dict with financial statement 

        Examples:
            >>> Stock("visa", exchange="nyse").financialStatement('summary', 'quarterly', 'original')
            >>> Stock("visa", exchange="nyse").financialStatement('cashflow', 'annual', 'restated')
            >>> Stock("visa", exchange="nyse").financialStatement('balancesheet', 'annual', 'restated')
            >>> Stock("visa", exchange="nyse").financialStatement('incomestatement', 'annual', 'restated')

        """

        if not isinstance(statement, str):
            raise TypeError('statement parameter should be a string')
        
        if not isinstance(period, str):
            raise TypeError('period parameter should be a string')
        
        if not isinstance(reportType, str):
            raise TypeError('reportType parameter should be a string')
        
        statement_choice = {"balancesheet" : "balanceSheet", "cashflow" : "cashFlow", "incomestatement" : "incomeStatement", "summary" : "summary"}
        
        period_choice = {"annual" : "A", "quarterly" : "Q"}

        reportType_choice = {"original" : "A", "restated" : "R"}

        if statement not in statement_choice:
            raise ValueError(f"statement parameter must take one of the following value : { ', '.join(statement_choice)}")

        if period not in period_choice:
            raise ValueError(f"period parameter must take one of the following value : { ', '.join(period_choice)}")

        if reportType not in reportType_choice:
            raise ValueError(f"reportType parameter must take one of the following value : { ', '.join(reportType_choice.keys())}")
        
        params = {"reportType" : reportType_choice[reportType]}
        if statement == "summary":
            return self.GetData("newfinancials",params=params, url_suffixe=f"{period}/summary")
        
        params["dataType"] = period_choice[period]

        return self.GetData("newfinancials",params=params, url_suffixe=f"{statement_choice[statement]}/detail")
    
    def financialSummary(self, period='annual', reportType='original'):
        """
        This function retrieves the financial statement summary.

        Args:
            period (str) : possible values are annual, quarterly
            reportType (str) : possible values are original, restated

        Returns:
            dict with financial statement summary

        Examples:
            >>> Stock("visa", exchange="nyse").financialSummary('quarterly', 'original')
            >>> Stock("visa", exchange="nyse").financialSummary('annual', 'restated')

        """

        return self.financialStatement("summary",period=period, reportType=reportType)
    
    def freeCashFlow(self):
        """
        This function retrieves the free cash flow.

        Returns:
            dict with free cash flow

        Examples:
            >>> Stock("visa", exchange="nyse").freeCashFlow()
  
        """
        return self.GetData("keyStats/cashFlow", url_suffixe='')
    
    def historical(self, start_date,end_date,frequency="daily"):
        """
        This function retrieves the historical price, volume and divide of the stock.

        Args:
            start_date (datetime) : start date to get history
            end_date (datetime) : end date to get history
            frequency (str) : can be daily, weekly, monthly

        Returns:
            list of dict with price, volume and dividend

        Examples:
            >>> Stock("visa", exchange="nyse").history(datetime.datetime.today()- datetime.timedelta(30),datetime.datetime.today())

        """
        return self.TimeSeries(["open","high","low","close",
                                "volume","previousClose","dividend"],
                                start_date=start_date,end_date=end_date,frequency=frequency)
    def incomeStatement(self, period='annual', reportType='original'):
        """
        This function retrieves the income statement.

        Args:
            period (str) : possible values are annual, quarterly
            reportType (str) : possible values are original, restated

        Returns:
            dict with income statement

        Examples:
            >>> Stock("visa", exchange="nyse").incomeStatement('quarterly', 'original')
            >>> Stock("visa", exchange="nyse").incomeStatement('annual', 'restated')

        """
        
        return self.financialStatement("incomestatement",period=period, reportType=reportType)
    
    def institutionBuyers(self, top=50):
        """
        This function retrieves the institutions which buy the stock.

        Args:
            top (int) : number of institutions to return
        Returns:
            dict with the buyers

        Examples:
            >>> Stock("visa", exchange="nyse").institutionBuyers(top=50)
  
        """
        
        if not isinstance(top, int):
            raise TypeError('top parameter should be an integer')
        
        return self.GetData("ownership/v1", url_suffixe= f"Buyers/institution/{top}/data")
    
    def institutionConcentratedOwners(self, top=50):
        """
        This function retrieves the institutions which are concentrated on the stock.

        Args:
            top (int) : number of institutions to return
        Returns:
            dict with the concentarted owners

        Examples:
            >>> Stock("visa", exchange="nyse").institutionConcentratedOwners(top=50)

        """
        
        if not isinstance(top, int):
            raise TypeError('top parameter should be an integer')
        
        return self.GetData("ownership/v1", url_suffixe= f"ConcentratedOwners/institution/{top}/data")
    
    def institutionOwnership(self, top=5):
        """
        This function retrieves the main institutions which own the stock.

        Args:
            top (int) : number of institutions to return
        Returns:
            dict with the main owners

        Examples:
            >>> Stock("visa", exchange="nyse").institutionOwnership(top=50)
   
        """
        
        if not isinstance(top, int):
            raise TypeError('top parameter should be an integer')
        r_saved = None
        r = NSEStockMFIDB().searchCache(ticker=self.ticker)
        if r is not None and len(r) > 0 and "FII" in r.keys():
            r_saved = r["FII"]
            # Give the opportunity for the first 2 days to fetch latest end-of-last-month MFI data
            if PKDateUtilities.currentDateTime().day not in [1,2]:
                return r_saved
        elif PKDateUtilities.isTradingTime():
            # Let's not make new requests to update the values during trading hours.
            return None
        elif not self.needsNetworkRequest(NSEStockMFIDB()):
            return None
        
        params = {"component":"sal-ownership"}
        params = self.defaultParams | params
        try:
            r = self.GetData("ownership/v1", url_suffixe= f"OwnershipData/institution/{top}/data", params=params, headers=self.defaultHeaders)
        except ConnectionError as e:
            default_logger().debug(f"{e}:\n{self.term}:Going to retrieve/reset the cookies and meta tags!",exc_info=True)
            self.refreshMorningstarTokens(self.defaultParams, self.defaultHeaders)
            params = {"component":"sal-ownership"}
            params = self.defaultParams | params
            r = self.GetData("ownership/v1", url_suffixe= f"OwnershipData/institution/{top}/data", params=self.defaultParams, headers=self.defaultHeaders)
        if r is not None and len(r) > 0 and len(r["rows"]) > 0:
            NSEStockMFIDB().saveCache(ticker=self.ticker, stockDict={"FII":r})
            r_saved = r
        return r_saved
    
    def institutionSellers(self, top=50):
        """
        This function retrieves the institutions which sell on the stock.

        Args:
            top (int) : number of institutions to return
        Returns:
            dict with sellers

        Examples:
            >>> Stock("visa", exchange="nyse").institutionSellers(top=50)
  
        """
        if not isinstance(top, int):
            raise TypeError('top parameter should be an integer')
        
        return self.GetData("ownership/v1", url_suffixe= f"Sellers/institution/{top}/data")
    
    def keyExecutives(self):
        """
        This function retrieves information oabout key excutives of the company.

        Returns:
            dict with key executives information

        Examples:
            >>> Stock("visa", exchange="nyse").keyExecutives()

        """
        return self.GetData("insiders/keyExecutives")
    def keyRatio(self):
        """
        This function retrieves the key ratio of the stock.

        Returns:
            dict with key ratio

        Examples:
            >>> Stock("visa", exchange="nyse").keyRatio()

        """
        return self.GetData("keyratios")
    
    def mutualFundBuyers(self, top=50):
        """
        This function retrieves the mutual funds which buy the stock.

        Args:
            top (int) : number of mutual funds to return
        Returns:
            dict with the buyers

        Examples:
            >>> Stock("visa", exchange="nyse").mutualFundBuyers(top=50)

        """
        
        if not isinstance(top, int):
            raise TypeError('top parameter should be an integer')
        
        return self.GetData("ownership/v1", url_suffixe= f"Buyers/mutualfund/{top}/data")
    
    def mutualFundConcentratedOwners(self, top=50):
        """
        This function retrieves the mutual funds which are concentrated on the stock.

        Args:
            top (int) : number of mutual funds to return
        Returns:
            dict with the concentarted owners

        Examples:
            >>> Stock("visa", exchange="nyse").mutualFundConcentratedOwners(top=50)
 
        """
        
        if not isinstance(top, int):
            raise TypeError('top parameter should be an integer')
        
        return self.GetData("ownership/v1", url_suffixe= f"ConcentratedOwners/mutualfund/{top}/data")
    
    def mutualFundOwnership(self, top=5):
        """
        This function retrieves the main mutual funds which own the stock.

        Args:
            top (int) : number of mutual funds to return
        Returns:
            dict with the main owners

        Examples:
            >>> Stock("visa", exchange="nyse").mutualFundOwnership(top=50)
  
        """
        
        if not isinstance(top, int):
            raise TypeError('top parameter should be an integer')
        r_saved = None
        r = NSEStockMFIDB().searchCache(ticker=self.ticker)
        if r is not None and len(r) > 0 and "MF" in r.keys():
            r_saved = r["MF"]
            # Give the opportunity for the first 2 days to fetch latest end-of-last-month MFI data
            if PKDateUtilities.currentDateTime().day not in [1,2]:
                return r_saved
        elif PKDateUtilities.isTradingTime():
            # Let's not make new requests to update the values during trading hours.
            return None
        elif not self.needsNetworkRequest(NSEStockMFIDB()):
            return None
        
        params = {"component":"sal-ownership"}
        params = self.defaultParams | params
        try:
            r = self.GetData("ownership/v1", url_suffixe= f"OwnershipData/mutualfund/{top}/data", params=params, headers=self.defaultHeaders)
        except ConnectionError as e:
            default_logger().debug(f"{e}:\n{self.term}:Going to retrieve/reset the cookies and meta tags!",exc_info=True)
            self.refreshMorningstarTokens(self.defaultParams, self.defaultHeaders)
            params = {"component":"sal-ownership"}
            params = self.defaultParams | params
            r = self.GetData("ownership/v1", url_suffixe= f"OwnershipData/mutualfund/{top}/data", params=self.defaultParams, headers=self.defaultHeaders)
        if r is not None and len(r) > 0 and len(r["rows"]) > 0:
            NSEStockMFIDB().saveCache(ticker=self.ticker, stockDict={"MF":r})
            r_saved = r
        return r_saved
    
    def mutualFundSellers(self, top=50):
        """
        This function retrieves the mutual funds which sell on the stock.

        Args:
            top (int) : number of mutual funds to return
        Returns:
            dict with sellers

        Examples:
            >>> Stock("visa", exchange="nyse").mutualFundSellers(top=50)
   
        """
        
        if not isinstance(top, int):
            raise TypeError('top parameter should be an integer')
        
        return self.GetData("ownership/v1", url_suffixe= f"Sellers/mutualfund/{top}/data")
    
    def operatingGrowth(self):
        """
        This function retrieves the operating growth of the stock.

        Returns:
            dict with operating growth

        Examples:
            >>> Stock("visa", exchange="nyse").operatingGrowth()

        """
        return self.GetData("keyStats/growthTable", url_suffixe='')
    
    def operatingMargin(self):
        """
        This function retrieves the operating margin of the stock.

        Returns:
            dict with operating margin

        Examples:
            >>> Stock("visa", exchange="nyse").operatingMargin()
    
        """
        return self.GetData("keyStats/OperatingAndEfficiency", url_suffixe='')
    
    def operatingPerformance(self):
        """
        This function retrieves the operating performance the stock.

        Returns:
            dict with voperating performance

        Examples:
            >>> Stock("visa", exchange="nyse").operatingPerformance()

        """
        return self.GetData("operatingPerformance/v2", url_suffixe='')
    
    def split(self):
        """
        This function retrieves the split history of the stock.

        Returns:
            dict with split history

        Examples:
            >>> Stock("visa", exchange="nyse").split()
        
        """
        return self.GetData("split")
    
    def trailingTotalReturn(self):
        """
        This function retrieves the performance of the stock and its index.

        Returns:
            dict with performance

        Examples:
            >>> Stock("visa", exchange="nyse").trailingTotalReturn()
      
        """
        return self.GetData("trailingTotalReturns")
    
    def transactionHistory(self):
        """
        This function retrieves the transaction of key people.

        Returns:
            list o dict of transaction of key people

        Examples:
            >>> Stock("visa", exchange="nyse").transactionHistory()

        """
        return self.GetData("insiders/transactionHistory")
    
    
    def transactionSummary(self):
        """
        This function retrieves the summuary of transactions of key people.

        Returns:
            list of dict with transactions

        Examples:
            >>> Stock("visa", exchange="nyse").transactionSummary()
   
        """
        return self.GetData("insiders/transactionChart")
    
    def valuation(self):
        """
        This function retrieves the valution of the stock.

        Returns:
            dict with valuation

        Examples:
            >>> Stock("visa", exchange="nyse").valuation()
    
        """
        return self.GetData("valuation", url_suffixe='')

    def fairValue(self):
        """
        This function retrieves the fair value of the stock.

        Args:
            top (int) : number of mutual funds to return
        Returns:
            dict with the fair value

        Examples:
            >>> Stock("visa", exchange="nyse").fairValue()
  
        """
        r = NSEStockFairValueDB().searchCache(ticker=self.ticker)
        if r is not None and len(r) > 0:
            return r
        elif PKDateUtilities.isTradingTime():
            # Let's not make new requests to update the values during trading hours.
            return None
        elif not self.needsNetworkRequest(NSEStockFairValueDB()):
            return None
        params = {"component":"sal-price-fairvalue"}
        params = self.defaultParams | params
        headers = self.defaultHeaders
        try:
            r = self.GetData("priceFairValue/v3", params=params, url_suffixe= f"data", headers=headers)
            # fv["chart"]["chartDatums"]["recent"]["latestFairValue"]
        except ConnectionError as e:
            default_logger().debug(f"{e}:\n{self.term}:Going to retrieve/reset the cookies and meta tags!",exc_info=True)
            self.refreshMorningstarTokens(params, headers)
            params = {"component":"sal-price-fairvalue"}
            params = self.defaultParams | params
            r = self.GetData("priceFairValue/v3", params=params, url_suffixe= f"data", headers=headers)
        fv = None
        if r is not None and len(r) > 0:
            try:
                fv = r["chart"]["chartDatums"]["recent"]["latestFairValue"]
                NSEStockFairValueDB().saveCache(ticker=self.ticker, stockDict={"latestFairValue":fv})
            except Exception as e:
                default_logger().debug(f"{e}:\n{self.term}:{r}",exc_info=True)
                pass
        return {"latestFairValue":fv} if fv is not None else fv

    def refreshMorningstarTokens(self, params, headers):
        if self.cookieHelper is None:
            self.cookieHelper = CookieHelper(download_folder=Archiver.get_user_cookies_dir(),
                                                 baseCookieUrl="https://morningstar.in/stocks/0p0000c3nz/nse-hdfc-bank-ltd/overview.aspx",
                                                 cookieStoreName="msta",
                                                 baseHtmlUrl="https://morningstar.in/stocks/0p0000c3nz/nse-hdfc-bank-ltd/overview.aspx",
                                                 htmlStoreName="msta")
        else:
            self.cookieHelper.resetCookies()
            self.cookieHelper.resetMetas()
        params["access_token"] = self.cookieHelper.html_metas["accessToken"]
        headers["X-Api-Realtime-E"] = self.cookieHelper.html_metas["realTimeToken"]
        self.fetcher.session.cookies.update(self.cookieHelper.cookies)
        self.defaultCookies = self.cookieHelper.cookies
        self.defaultHeaders = headers
        self.defaultParams = params
        
    def mutualFundFIIChangeData(self, rows=None, sortKey="date"):
        if rows is None or len(rows) < 1 or len(rows["rows"]) < 1:
            return None
        d = pd.DataFrame(rows["rows"])
        d = d[["name","currentShares", "date","changeAmount","changePercentage"]]
        if (d is not None and len(d) > 0):
            d.sort_values(by=[sortKey], ascending=False, inplace=True)
        return d

# # stk = Stock("CTE")
# stocks =[DUMMY_SECURITY, "RELIANCE","SBIN"]
# for stockName in stocks:
#     stk = Stock(stockName)
#     R = stk.mutualFundOwnership(top=5)
#     # d = stk.changeData(R)
# #     # print(f"mutualFundOwnership:\n{d}")
# #     R = stk.institutionOwnership(top=5)
# #     # d = stk.changeData(R)
# #     # print(f"institutionOwnership:\n{d}")

#     fv = stk.fairValue()
#     print(fv["latestFairValue"])
# print("done")
# R = stk.mutualFundSellers(top=50)
# d = stk.changeData(R)
# print(f"mutualFundSellers:\n{d}")
# d.to_csv("mutualFundSellers.csv")
# R = stk.mutualFundConcentratedOwners(top=50)
# d = stk.changeData(R)
# combined_pd = pd.concat([combined_pd, d], axis=0)
# print(f"mutualFundConcentratedOwners:\n{d}")
# d.to_csv("mutualFundConcentratedOwners.csv")
# R = stk.mutualFundBuyers(top=50)
# d = stk.changeData(R)
# combined_pd = pd.concat([combined_pd, d], axis=0)
# print(f"mutualFundBuyers:\n{d}")
# d.to_csv("mutualFundBuyers.csv")
# combined_pd = pd.concat([combined_pd, d], axis=0)
# R = stk.institutionSellers(top=50)
# d = stk.changeData(R)
# combined_pd = pd.concat([combined_pd, d], axis=0)
# print(f"institutionSellers:\n{d}")
# d.to_csv("institutionSellers.csv")
# R = stk.institutionConcentratedOwners(top=50)
# d = stk.changeData(R)
# combined_pd = pd.concat([combined_pd, d], axis=0)
# print(f"institutionConcentratedOwners:\n{d}")
# d.to_csv("institutionConcentratedOwners.csv")
# R = stk.institutionBuyers(top=50)
# d = stk.changeData(R)
# combined_pd = pd.concat([combined_pd, d], axis=0)
# print(f"institutionBuyers:\n{d}")
# d.to_csv("institutionBuyers.csv")
# combined_pd.sort_values(by=["date"], ascending=False, inplace=True)
# combined_pd.drop_duplicates(inplace=True)
# combined_pd.to_csv("combined.csv")

