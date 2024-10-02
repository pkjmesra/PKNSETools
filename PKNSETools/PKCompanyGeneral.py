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
import json
from time import sleep
from collections import namedtuple
from mthrottle import Throttle
from PKNSETools.Benny import NSE
import requests
from PKDevTools.classes import Archiver

from PKNSETools.PKConstants import (_autoComplete_url_path, _base_domain,
                                    _head, _quote_url_path)
from PKDevTools.classes.OutputControls import OutputControls

session = requests.session()

throttleConfig = {
    'default': {
        'rps': 3,
    },
}
MAX_PENALTY_COUNT = 1
MIN_PENALTY_WAIT_SECONDS = 10
th = Throttle(throttleConfig, MAX_PENALTY_COUNT)

def initialize():
    session = NSE(download_folder=Archiver.get_user_cookies_dir()).session
    
def _get_Tuple_From_JSON(companyDict):
    return namedtuple('X', companyDict.keys())(*companyDict.values())

def get_Id_By_Name(name):
    companyDetails = get_Company_Details_By_Name(name)
    return companyDetails.info.identifier

def get_Search_Results_By_Name(name):
    search_url = f'{_base_domain}{_autoComplete_url_path}'
    session.get(f'{_base_domain}', headers=_head)
    search_results = session.get(url=search_url.format(name), headers=_head)
    # {
    # "symbols":[
    #     {
    #         "symbol":"SBIN",
    #         "symbol_info":"State Bank of India",
    #         "symbol_suggest":[
    #             {
    #             "input":"SBIN",
    #             "weight":16
    #             },
    #             {
    #             "input":"State",
    #             "weight":8
    #             },
    #             {
    #             "input":"Bank",
    #             "weight":8
    #             },
    #             {
    #             "input":"of",
    #             "weight":8
    #             },
    #             {
    #             "input":"India",
    #             "weight":8
    #             }
    #         ],
    #         "result_type":"symbol",
    #         "result_sub_type":"equity",
    #         "activeSeries":[
    #             "EQ"
    #         ],
    #         "url":"/get-quotes/equity?symbol=SBIN"
    #     }
    # ],
    # "mfsymbols":[
        
    # ],
    # "search_content":[
    #     {
    #         "title":"अंडरलाइंग्स एंड इन्फ़ॉर्मेशन की लिस्ट",
    #         "content":"LIMITEDRELIANCE160SBI CARDS AND PAYMENT SERVICES LIMITEDSBICARD161SBI LIFE INSURANCE COMPANY\nLIMITEDSBILIFE162SHREE CEMENT LIMITEDSHREECEM163SHRIRAM TRANSPORT FINANCE COMPANY LIMITEDSRTRANSFIN164SIEMENS LIMITED\nSIEMENS165SRF LIMITEDSRF166STATE BANK OF <b>INDIASBIN167STEEL</b>",
    #         "url":"/products-services/equity-derivatives-list-underlyings-information-hindi",
    #         "result_type":"content",
    #         "result_sub_type":"content"
    #     },
    #     {
    #         "title":"List of Underlyings and Information",
    #         "content":"LIMITEDRECLTD150RELIANCE INDUSTRIES LIMITEDRELIANCE151SBI CARDS AND PAYMENT SERVICES LIMITEDSBICARD\n152SBI LIFE INSURANCE COMPANY LIMITEDSBILIFE153SHREE CEMENT LIMITEDSHREECEM154SHRIRAM FINANCE LIMITEDSHRIRAMFIN155\nSIEMENS LIMITEDSIEMENS156SRF LIMITEDSRF157STATE BANK OF <b>INDIASBIN158STEEL</b>",
    #         "url":"/products-services/equity-derivatives-list-underlyings-information",
    #         "result_type":"content",
    #         "result_sub_type":"content"
    #     },
    #     {
    #         "title":"અંડરલાયિંગ એન્ડ ઇન્ફોર્મેશન નું લિસ્ટ",
    #         "content":"INTERNATIONAL LIMITEDMOTHERSON151SBI CARDS AND PAYMENT SERVICES LIMITEDSBICARD152SBI LIFE INSURANCE COMPANY\nLIMITEDSBILIFE153SHREE CEMENT LIMITEDSHREECEM154SHRIRAM FINANCE LIMITEDSHRIRAMFIN155SIEMENS LIMITEDSIEMENS156SRF LIMITED\nSRF157STATE BANK OF <b>INDIASBIN158STEEL</b>",
    #         "url":"/products-services/equity-derivatives-list-underlyings-information-gujarati",
    #         "result_type":"content",
    #         "result_sub_type":"content"
    #     },
    #     {
    #         "title":"Press Releases - Archives",
    #         "content":"Security listed & admitted to dealings � GRAVITA\n * NSE completes its 2680th Normal Settlement\n\nNov 12, 2010\n * Market-wide Position Limit in NAGARFERT\n * NSE completes its 2679th Normal Settlement\n\nNov 11, 2010\n * Security listed & admitted to dealings � <b>SBIN</b>",
    #         "url":"/resources/exchange-communication-press-releases-archives",
    #         "result_type":"content",
    #         "result_sub_type":"content"
    #     }
    # ],
    # "sitemap":[
        
    # ]
    # }  
    search_result = json.loads(str(search_results.json()).replace("'","\""), object_hook=_get_Tuple_From_JSON)
    return search_result

def download(symbolOrTask, trialCount=0):
    get_details = f'{_base_domain}{_quote_url_path}'
    symbol = symbolOrTask
    if not isinstance(symbolOrTask, str):
        symbol = symbolOrTask.userData    
    company_details = NSE(download_folder=Archiver.get_user_cookies_dir()).session.get(url=get_details.format(symbol), headers=_head)
    if company_details.status_code == 401 and trialCount <=2:
        return download(symbolOrTask,trialCount=trialCount+1)
        
    if company_details.status_code == 429 or company_details.status_code == 403:
        OutputControls().printOutput(f"{company_details.status_code}: {company_details.text}")
        if (th.penalize()):
            sleep(MIN_PENALTY_WAIT_SECONDS)
            th.maxPenaltyCount += MAX_PENALTY_COUNT
    if company_details.status_code == 200:
        # try:
        #     # Let's try without any conversions first
        #     companyDetails = json.loads(company_details.text, object_hook=_get_Tuple_From_JSON)
        # except:
        text = str(company_details.json()).replace("'","\"").replace('True','true').replace('False','false').replace('None','null')
        companyDetails = json.loads(text, object_hook=_get_Tuple_From_JSON)
            # pass
    # '{"info": {
    #       "symbol": "SBIN", 
    #       "companyName": "State Bank of India", 
    #       "industry": "BANKS", 
    #       "activeSeries": ["EQ"], 
    #       "debtSeries": [], 
    #       "tempSuspendedSeries": ["IL", "N1", "N2", "N3", "N4", "N5", "N6"], 
    #       "isFNOSec": true, 
    #       "isCASec": false, 
    #       "isSLBSec": true, 
    #       "isDebtSec": false, 
    #       "isSuspended": false, 
    #       "isETFSec": false, 
    #       "isDelisted": false, 
    #       "isin": "INE062A08066", 
    #       "isTop10": false, 
    #       "identifier": "SBINEQN"
    #       }, 
    # "metadata": { "series": "EQ", 
    #               "symbol": "SBIN", 
    #               "isin": "INE062A01020", 
    #               "status": "Listed", 
    #               "listingDate": "01-Mar-1995", 
    #               "industry": "Public Sector Bank", 
    #               "lastUpdateTime": "11-Aug-2023 16:00:00", 
    #               "pdSectorPe": 16.6, 
    #               "pdSymbolPe": 8.39, 
    #               "pdSectorInd": "NIFTY BANK                                        "}, 
    #               "securityInfo": {
    #                   "boardStatus": "Main", 
    #                   "tradingStatus": "Active", 
    #                   "tradingSegment": "Normal Market", 
    #                   "sessionNo": "-", 
    #                   "slb": "Yes", 
    #                   "classOfShare": "Equity", 
    #                   "derivatives": "Yes", 
    #                   "surveillance": {"surv": null, "desc": null}, 
    #                   "faceValue": 1, 
    #                   "issuedSize": 8924611934}, 
    #               "sddDetails": {
    #                   "SDDAuditor": "-", 
    #                   "SDDStatus": "-"}, 
    #               "priceInfo": {
    #                   "lastPrice": 574.5, 
    #                   "change": 0.8500000000000227, 
    #                   "pChange": 0.14817397367733334, 
    #                   "previousClose": 573.65, 
    #                   "open": 575.45, 
    #                   "close": 574.15, 
    #                   "vwap": 575.36, 
    #                   "lowerCP": "516.30", 
    #                   "upperCP": "631.00", 
    #                   "pPriceBand": "No Band", 
    #                   "basePrice": 573.65, 
    #                   "intraDayHighLow": {"min": 572, "max": 579, "value": 574.5}, 
    #                   "weekHighLow": {"min": 499.35, "minDate": "01-Feb-2023", "max": 629.55, "maxDate": "15-Dec-2022", "value": 574.5}, 
    #                   "iNavValue": null, 
    #                   "checkINAV": false}, 
    #               "industryInfo": {"macro": "Financial Services", "sector": "Financial Services", "industry": "Banks", 
    #                   "basicIndustry": "Public Sector Bank"}, 
    #               "preOpenMarket": {"preopen": [{"price": 516.3, "buyQty": 0, "sellQty": 104},{"price": 544.95, "buyQty": 0, "sellQty": 1554}, {"price": 550, "buyQty": 0, "sellQty": 144}, {"price": 553.1, "buyQty": 0, "sellQty": 1}, {"price": 575.45, "buyQty": 0, "sellQty": 0, "iep": true}, {"price": 599.85, "buyQty": 6, "sellQty": 0}, {"price": 600, "buyQty": 5, "sellQty": 0}, {"price": 602.35, "buyQty": 654, "sellQty": 0}, {"price": 620, "buyQty": 101, "sellQty": 0}], 
    #                   "ato": {"buy": 10667, "sell": 1621}, 
    #                   "IEP": 575.45, 
    #                   "totalTradedVolume": 29301, 
    #                   "finalPrice": 575.45, 
    #                   "finalQuantity": 29301, 
    #                   "lastUpdateTime": "11-Aug-2023 09:07:49", 
    #                   "totalBuyQuantity": 286624, 
    #                   "totalSellQuantity": 603729, 
    #                   "atoBuyQty": 10667, 
    #                   "atoSellQty": 1621}
    # }'
    if not isinstance(symbolOrTask, str):
        result = company_details.text
        if symbolOrTask.taskId > 0:
            symbolOrTask.progressStatusDict[symbolOrTask.taskId] = {'progress': 0, 'total': 1}
            symbolOrTask.resultsDict[symbolOrTask.taskId] = result
            symbolOrTask.progressStatusDict[symbolOrTask.taskId] = {'progress': 1, 'total': 1}
        else:
            symbolOrTask.result = result
    return companyDetails

def get_Company_Details_By_Name(name):
    search_results = get_Search_Results_By_Name(name)
    symbol = search_results.symbols[0].symbol
    return download(symbol)
