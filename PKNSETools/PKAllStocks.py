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
import csv
import os

import pandas as pd
import requests

from PKNSETools.PKConstants import (_base_domain, _daily_report_url_path,
                                    _headers)

session = requests.session()

def _makeDataset(url):
    with open("dataset.csv", "w") as f:
        f.write(session.get(url).text)

    with open("dataset.csv", "r") as f:
        dataset = csv.reader(f)
        niftyData = []
        top25Data = []
        top5Nifty50GainerData = []
        top5Nifty50LoserData = []
        stockPriceVolumeData = []
        NiftyLoaded = False
        top25Loaded = False
        top5GainerLoaded = False
        top5LoserLoaded = False
        shouldBeginLoad = False
        for idx, row in enumerate(dataset):
            if len(row) == 0:
                continue
            if 8 <= idx and not NiftyLoaded:
                if str(row[1]).startswith('ADVANCES'):
                    NiftyLoaded = True
                else:
                    niftyData.append(row)

            if NiftyLoaded and not top25Loaded:
                if not shouldBeginLoad and str(row[1]).startswith('SYMBOL'):
                    shouldBeginLoad = True
                if shouldBeginLoad:
                    if str(row[1]).endswith('Gainers:'):
                        top25Loaded = True
                        shouldBeginLoad = False
                    else:
                        top25Data.append(row)
            if NiftyLoaded and top25Loaded and not top5GainerLoaded:
                if not shouldBeginLoad and str(row[1]).startswith('SYMBOL'):
                    shouldBeginLoad = True
                if shouldBeginLoad:
                    if str(row[1]).endswith('Losers:'):
                        top5GainerLoaded = True
                        shouldBeginLoad = False
                    else:
                        top5Nifty50GainerData.append(row)
            if NiftyLoaded and top25Loaded and top5GainerLoaded and not top5LoserLoaded:
                if not shouldBeginLoad and str(row[1]).startswith('SYMBOL'):
                    shouldBeginLoad = True
                if shouldBeginLoad:
                    if str(row[1]).startswith('Securities'):
                        top5LoserLoaded = True
                        shouldBeginLoad = False
                    else:
                        top5Nifty50LoserData.append(row)
            if NiftyLoaded and top25Loaded and top5GainerLoaded and top5LoserLoaded:
                if not shouldBeginLoad and str(row[1]).startswith('SYMBOL'):
                    shouldBeginLoad = True
                if shouldBeginLoad:
                    stockPriceVolumeData.append(row)
    os.remove("dataset.csv")
    dfs = [pd.DataFrame(niftyData),pd.DataFrame(top25Data),pd.DataFrame(top5Nifty50GainerData),pd.DataFrame(top5Nifty50LoserData), pd.DataFrame(stockPriceVolumeData)]
    pos = 0
    for df in dfs:
        headers = df.iloc[0]
        df  = pd.DataFrame(df.values[1:], columns=headers)
        dfs[pos] = df
        pos += 1
    return dfs[0], dfs[1], dfs[2], dfs[3], dfs[4]

def get_Merged_Daily_Reports() -> object:
    webData = session.get(url=f'{_base_domain}{_daily_report_url_path}', headers=_headers)
    return _makeDataset(webData.json()[1]['link'])

# # use it likes this
# df_niftyData, df_top25Data, df_top5Nifty50GainerData, df_top5Nifty50LoserData, df_priceVolume_data = getTodayData()
# print(df_niftyData)
# print(df_top25Data)
# print(df_top5Nifty50GainerData)
# print(df_top5Nifty50LoserData)
# print(df_priceVolume_data)