from datetime import datetime
import requests
import pandas as pd
# from general import *

head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36 "
}


class Intra_Day:
    baseNumber = None
    session = None
    ticker = None

    def __init__(self, ticker):
        self.baseNumber = 0
        self.session = requests.session()
        self.ticker = ticker
        self.session.get("https://www.nseindia.com", headers=head)
        self.session.get("https://www.nseindia.com/get-quotes/equity?symbol=" + ticker, headers=head)

    def secondsTotime(self, seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return hour, minutes, seconds

    def dateCalculator(self, num):
        if self.baseNumber == 0:
            self.baseNumber = (num // 100000) * 100000
        num = abs(num - self.baseNumber)
        num = num / 1000
        num = int(num)
        today = datetime.today()
        (h, m, s) = self.secondsTotime(num)
        return datetime(today.year, today.month, today.day, 9 + h, m, s)

    def intraDay(self,):
        preopen_url = "https://www.nseindia.com/api/chart-databyindex?index=" + self.ticker + "&preopen=true"
        open_url = "https://www.nseindia.com/api/chart-databyindex?index=" + self.ticker
        preopen_webdata = self.session.get(url=preopen_url, headers=head)
        opened_webdata = self.session.get(url=open_url, headers=head)
        timestamp = []
        data = []

        for (i, j) in preopen_webdata.json()['grapthData']:
            timestamp.append(self.dateCalculator(i))
            data.append(j)

        for (i, j) in opened_webdata.json()['grapthData']:
            timestamp.append(self.dateCalculator(i))
            data.append(j)
        return timestamp, data

    def nifty_intraDay(self):
        varient = self.ticker
        varient = varient.upper()
        varient = varient.replace(' ', '%20')
        varient = varient.replace('-', '%20')
        preopen_url = "https://www.nseindia.com/api/chart-databyindex?index={}&indices=true&preopen=true".format(
            varient)
        open_url = "https://www.nseindia.com/api/chart-databyindex?index={}&indices=true".format(varient)

        preopen_webdata = self.session.get(url=preopen_url, headers=head)
        open_webdata = self.session.get(url=open_url, headers=head)
        data = []
        timestamp = []
        ticks_list = []
        for (i, j) in preopen_webdata.json()['grapthData']:
            data.append(j)
            t = self.dateCalculator(i)
            timestamp.append(t)
            ticks_list.append({'Date':t,'LTP':j})

        for (i, j) in open_webdata.json()['grapthData']:
            data.append(j)
            t = self.dateCalculator(i)
            timestamp.append(t)
            ticks_list.append({'Date':t,'LTP':j})

        return timestamp, data, ticks_list

    def ohlc(self,prices,interval='1Min'):
        # Convert the index to datetime
        df = pd.DataFrame(prices, columns = ['Date', 'LTP'])
        # df["Date"] = df["Date"].apply(lambda x: datetime.utcfromtimestamp(x/1000))
        df.set_index('Date', inplace=True)
        # Resample LTP column to interval bars using resample function from pandas
        resample_LTP = df.resample(interval).ohlc()['LTP']
        resample_LTP = resample_LTP.reset_index(drop=False)
        return resample_LTP

# ID = Intra_Day(getId('SBIN'))
# timeStamp, dataPoints,prices = ID.nifty_intraDay()
# print(ID.ohlc(prices))
