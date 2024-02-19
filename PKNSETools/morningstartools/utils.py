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
import random

APIKEY = 'lstzFDEOhfFNMLikKa0am9mgEKLBl49T'

ASSET_TYPE = ['etf', 'fund', 'stock']

EXCHANGE = {
            "NYSE": {
                    "name": "exchanges_equity_nyse",
                    "id": "E0EXG$XNYS"
                    },

            "NASDAQ" : {
                    "name": "exchanges_equity_nasdaq",
                    "id": "E0EXG$XNAS"
                        },

            "LSE" : {
                    "name": "exchanges_london_stock_exchange",
                    "id": "E0EXG$XLON"
                    },

            "AMSTERDAM" : {
                    "name": "exchanges_equity_nyse_euronext_amsterdam",
                    "id": "E0EXG$XAMS"
                        },
 
            "ATHENS" : {
                    "name": "exchanges_equity_athens_stock_exchange",
                    "id": "E0EXG$XATH"
                        },

            "BOLSA_DE_VALORES" : {
                    "name": "exchanges_equity_bolsa_de_valores",
                    "id": "E0EXG$XMEX"
                        },

            "BOMBAY" : {
                    "name": "exchanges_equity_bombay_stock_exchange",
                    "id": "E0EXG$XBOM"
                        },

            "BORSA_ITALIANA" : {
                    "name": "exchanges_equity_borsa_italiana",
                    "id": "E0EXG$XMIL"
                        },

            "BRUSSELS" : {
                    "name": "exchanges_equity_nyse_brussels",
                    "id": "E0EXG$XBRU"
                        },

            "COPENHAGEN" : {
                    "name": "exchanges_equity_omx_exchange_copenhagen",
                    "id": "E0EXG$XCSE"
                            },

            "HELSINKI" : {
                    "name": "exchanges_equity_omx_exchange_helsinki",
                    "id": "E0EXG$XHEL"
                        },

                "HONG-KONG" : {
                    "name": "exchanges_HONG_KONG",
                    "id": "E0EXG$XHKG"
                        },
            "ICELAND" : {
                    "name": "exchanges_equity_omx_exchange_iceland",
                    "id": "E0EXG$XICE"
                        },

            "INDIA" : {
                    "name": "exchanges_equity_india_stock_exchange",
                    "id": "E0EXG$XNSE"
                        },

            "IPSX" : {
                    "name": "exchanges_equity_exchange_IPSX",
                    "id": "E0EXG$IPSX"
                        },

            "IRELAND" : {
                    "name": "exchanges_equity_irish_stock_exchange",
                    "id": "E0EXG$XDUB"
                        },

            "ISTANBUL" : {
                    "name": "exchanges_equity_istanbul_stock_exchange",
                    "id": "E0EXG$XIST"
                        },

            "LISBON" : {
                    "name": "exchanges_equity_nyse_euronext_lisbon",
                    "id": "E0EXG$XLIS"
                        },

            "LUXEMBOURG" : {
                    "name": "exchanges_equity_luxembourg_stock_exchange",
                    "id": "E0EXG$XLUX"
                        },

            "OSLO_BORS" : {
                    "name": "exchanges_equity_oslo_bors",
                    "id": "E0EXG$XOSL"
                        },

            "PARIS" : {
                    "name": "exchanges_equity_nyse_paris",
                    "id": "E0EXG$XPAR"
                        },

            "RIGA" : {
                    "name": "exchanges_equity_omx_exchange_riga",
                    "id": "E0EXG$XRIS"
                        },

            "SHANGAI" : {
                    "name": "exchanges_equity_shanghai_stock_exchange",
                    "id": "E0EXG$XSHG"
                        },

            "SHENZHEN" : {
                    "name": "exchanges_equity_shenzhen_stock_exchange",
                    "id": "E0EXG$XSHE"
                        },

            "SINGAPORE" : {
                    "name": "exchanges_equity_singapore",
                    "id": "E0EXG$XSES"
                        },
        
            "STOCKHOLM" : {
                    "name": "exchanges_equity_nasdaq_omx_stockholm",
                    "id": "E0EXG$XSTO"
                        },

            "SWISS" : {
                    "name": "exchanges_equity_six__swiss_exchange",
                    "id": "E0EXG$XSWX"
                    },

            "TAIWAN" : {
                    "name": "exchanges_equity_taiwan_stock_exchange",
                    "id": "E0EXG$XTAI"
                        },

            "TALLIN" : {
                    "name": "exchanges_equity_tallin_stock_exchange",
                    "id": "E0EXG$XTAL"
                        },

            "THAILAND" : {
                    "name": "exchanges_equity_thailand_stock_exchange",
                    "id": "E0EXG$XBKK"
                        },

            "TOKYO" : {
                    "name": "exchanges_equity_tokyo_stock_exchange",
                    "id": "E0EXG$XTKS"
                        },

            "VILNIUS" : {
                    "name": "exchanges_equity_omx_exchange_vilnius",
                    "id": "E0EXG$XLIT"
                        },
                                                                                
            "WARSAW" :{
                    "name": "exchanges_equity_warsaw_stock_exchange",
                    "id": "E0EXG$XWAR"
                        },

            "WIENER_BOERSE" : {
                    "name": "exchanges_equity_wiener_boerse",
                    "id": "E0EXG$XWBO"
                        },

        "WORLDWIDE_EQUITY" : {
                    "name": "exchanges_worldwide_equity",
                    "id": "E0WWE$$ALL"
                        },
            }


FIELDS = [
    'AdministratorCompanyId',
    'AlphaM36',
    'AnalystRatingScale',
    'AverageCreditQualityCode',
    'AverageMarketCapital',
    'BetaM36',
    'BondStyleBox',
    'brandingCompanyId',
    'categoryId',
    'CategoryName',
    'ClosePrice',
    'currency',
    'DebtEquityRatio',
    'distribution',
    'DividendYield',
    'EBTMarginYear1',
    'EffectiveDuration',
    'EPSGrowth3YYear1',
    'equityStyle',
    'EquityStyleBox',
    'exchangeCode',
    'ExchangeId',
    'ExpertiseAdvanced',
    'ExpertiseBasic',
    'ExpertiseInformed',
    'FeeLevel',
    'fundShareClassId',
    'fundSize',
    'fundStyle',
    'FundTNAV',
    'GBRReturnD1',
    'GBRReturnM0',
    'GBRReturnM1',
    'GBRReturnM12',
    'GBRReturnM120',
    'GBRReturnM3',
    'GBRReturnM36',
    'GBRReturnM6',
    'GBRReturnM60',
    'GBRReturnW1',
    'geoRegion',
    'globalAssetClassId',
    'globalCategoryId',
    'iMASectorId',
    'IndustryName',
    'InitialPurchase',
    'instrumentName',
    'investment',
    'investmentExpertise',
    'investmentObjective',
    'investmentType',
    'investorType',
    'InvestorTypeEligibleCounterparty',
    'InvestorTypeProfessional',
    'InvestorTypeRetail',
    'LargestSector',
    'LegalName',
    'managementStyle',
    'ManagerTenure',
    'MarketCap',
    'MarketCountryName',
    'MaxDeferredLoad',
    'MaxFrontEndLoad',
    'MaximumExitCostAcquired',
    'MorningstarRiskM255',
    'Name',
    'NetMargin',
    'ongoingCharge',
    'OngoingCostActual',
    'PEGRatio',
    'PERatio',
    'PerformanceFeeActual',
    'PriceCurrency',
    'QuantitativeRating',
    'R2M36',
    'ReturnD1',
    'ReturnM0',
    'ReturnM1',
    'ReturnM12',
    'ReturnM120',
    'ReturnM3',
    'ReturnM36',
    'ReturnM6',
    'ReturnM60',
    'ReturnProfileGrowth',
    'ReturnProfileHedging',
    'ReturnProfileIncome',
    'ReturnProfileOther',
    'ReturnProfilePreservation',
    'ReturnW1',
    'RevenueGrowth3Y',
    'riskSrri',
    'ROATTM',
    'ROETTM',
    'ROEYear1',
    'ROICYear1',
    'SecId',
    'SectorName',
    'shareClassType',
    'SharpeM36',
    'StandardDeviationM36',
    'starRating',
    'StarRatingM255',
    'SustainabilityRank',
    'sustainabilityRating',
    'TenforeId',
    'Ticker',
    'totalReturn',
    'totalReturnTimeFrame',
    'TrackRecordExtension',
    'TransactionFeeActual',
    'umbrellaCompanyId',
    'Universe',
    'Yield_M12',
    'yieldPercent',

]


FILTER_FUND = [  
    'AdministratorCompanyId',
    'AnalystRatingScale',
    'BondStyleBox',
    'BrandingCompanyId',
    'CategoryId',
    'CollectedSRRI',
    'distribution',
    'EquityStyleBox',
    'ExpertiseInformed',
    'FeeLevel',
    'FundTNAV',
    'GBRReturnM0',
    'GBRReturnM12',
    'GBRReturnM120',
    'GBRReturnM36',
    'GBRReturnM60',
    'GlobalAssetClassId',
    'GlobalCategoryId',
    'IMASectorID',
    'IndexFund',
    'InvestorTypeProfessional',
    'LargestRegion',
    'LargestSector',
    'OngoingCharge',
    'QuantitativeRating',
    'ReturnProfilePreservation',
    'ShareClassTypeId',
    'starRating',
    'SustainabilityRank',
    'UmbrellaCompanyId',
    'Yield_M12',

        ]

FILTER_STOCK = [  
    'debtEquityRatio',
    'DividendYield',
    'epsGrowth3YYear1',
    'EquityStyleBox',
    'GBRReturnM0',
    'GBRReturnM12',
    'GBRReturnM36',
    'GBRReturnM60',
    'GBRReturnM120',
    'IndustryId',
    'MarketCap',
    'netMargin',
    'PBRatio',
    'PEGRatio',
    'PERatio',
    'PSRatio',
    'revenueGrowth3Y',
    'roattm',
    'roettm',
    'SectorId',
        ]



SITE = {
        
        'af' : {'iso3' : 'AFG', 'site' : ''},
        'ax' : {'iso3' : 'ALA', 'site' : ''},
        'al' : {'iso3' : 'ALB', 'site' : ''},
        'dz' : {'iso3' : 'DZA', 'site' : ''},
        'as' : {'iso3' : 'ASM', 'site' : ''},
        'ad' : {'iso3' : 'AND', 'site' : ''},
        'ao' : {'iso3' : 'AGO', 'site' : ''},
        'ai' : {'iso3' : 'AIA', 'site' : ''},
        'aq' : {'iso3' : 'ATA', 'site' : ''},
        'ag' : {'iso3' : 'ATG', 'site' : ''},
        'ar' : {'iso3' : 'ARG', 'site' : ''},
        'am' : {'iso3' : 'ARM', 'site' : ''},
        'aw' : {'iso3' : 'ABW', 'site' : ''},
        'au' : {'iso3' : 'AUS', 'site' : ''},
        'at' : {'iso3' : 'AUT', 'site' : ''},
        'az' : {'iso3' : 'AZE', 'site' : ''},
        'bs' : {'iso3' : 'BHS', 'site' : ''},
        'bh' : {'iso3' : 'BHR', 'site' : ''},
        'bd' : {'iso3' : 'BGD', 'site' : ''},
        'bb' : {'iso3' : 'BRB', 'site' : ''},
        'by' : {'iso3' : 'BLR', 'site' : ''},
        'be' : {'iso3' : 'BEL', 'site' : 'https://www.morningstar.be/be/'},
        'bz' : {'iso3' : 'BLZ', 'site' : ''},
        'bj' : {'iso3' : 'BEN', 'site' : ''},
        'bm' : {'iso3' : 'BMU', 'site' : ''},
        'bt' : {'iso3' : 'BTN', 'site' : ''},
        'bo' : {'iso3' : 'BOL', 'site' : ''},
        'bq' : {'iso3' : 'BES', 'site' : ''},
        'ba' : {'iso3' : 'BIH', 'site' : ''},
        'bw' : {'iso3' : 'BWA', 'site' : ''},
        'bv' : {'iso3' : 'BVT', 'site' : ''},
        'br' : {'iso3' : 'BRA', 'site' : 'https://www.morningstarbr.com/br/'},
        'io' : {'iso3' : 'IOT', 'site' : ''},
        'bn' : {'iso3' : 'BRN', 'site' : ''},
        'bg' : {'iso3' : 'BGR', 'site' : ''},
        'bf' : {'iso3' : 'BFA', 'site' : ''},
        'bi' : {'iso3' : 'BDI', 'site' : ''},
        'cv' : {'iso3' : 'CPV', 'site' : ''},
        'kh' : {'iso3' : 'KHM', 'site' : ''},
        'cm' : {'iso3' : 'CMR', 'site' : ''},
        'ca' : {'iso3' : 'CAN', 'site' : 'https://www.morningstar.ca/ca/'},
        'ky' : {'iso3' : 'CYM', 'site' : ''},
        'cf' : {'iso3' : 'CAF', 'site' : ''},
        'td' : {'iso3' : 'TCD', 'site' : ''},
        'cl' : {'iso3' : 'CHL', 'site' : 'https://www.morningstar.cl/cl/'},
        'cn' : {'iso3' : 'CHN', 'site' : ''},
        'cx' : {'iso3' : 'CXR', 'site' : ''},
        'cc' : {'iso3' : 'CCK', 'site' : ''},
        'co' : {'iso3' : 'COL', 'site' : ''},
        'km' : {'iso3' : 'COM', 'site' : ''},
        'cd' : {'iso3' : 'COD', 'site' : ''},
        'cg' : {'iso3' : 'COG', 'site' : ''},
        'ck' : {'iso3' : 'COK', 'site' : ''},
        'cr' : {'iso3' : 'CRI', 'site' : ''},
        'ci' : {'iso3' : 'CIV', 'site' : ''},
        'hr' : {'iso3' : 'HRV', 'site' : ''},
        'cu' : {'iso3' : 'CUB', 'site' : ''},
        'cw' : {'iso3' : 'CUW', 'site' : ''},
        'cy' : {'iso3' : 'CYP', 'site' : ''},
        'cz' : {'iso3' : 'CZE', 'site' : ''},
        'dk' : {'iso3' : 'DNK', 'site' : 'https://www.morningstar.dk/dk/'},
        'dj' : {'iso3' : 'DJI', 'site' : ''},
        'dm' : {'iso3' : 'DMA', 'site' : ''},
        'do' : {'iso3' : 'DOM', 'site' : ''},
        'ec' : {'iso3' : 'ECU', 'site' : ''},
        'eg' : {'iso3' : 'EGY', 'site' : ''},
        'sv' : {'iso3' : 'SLV', 'site' : ''},
        'gq' : {'iso3' : 'GNQ', 'site' : ''},
        'er' : {'iso3' : 'ERI', 'site' : ''},
        'ee' : {'iso3' : 'EST', 'site' : ''},
        'sz' : {'iso3' : 'SWZ', 'site' : ''},
        'et' : {'iso3' : 'ETH', 'site' : ''},
        'fk' : {'iso3' : 'FLK', 'site' : ''},
        'fo' : {'iso3' : 'FRO', 'site' : ''},
        'fj' : {'iso3' : 'FJI', 'site' : ''},
        'fi' : {'iso3' : 'FIN', 'site' : 'https://www.morningstar.fi/fi/'},
        'fr' : {'iso3' : 'FRA', 'site' : 'https://www.morningstar.fr/fr/'},
        'gf' : {'iso3' : 'GUF', 'site' : ''},
        'pf' : {'iso3' : 'PYF', 'site' : ''},
        'tf' : {'iso3' : 'ATF', 'site' : ''},
        'ga' : {'iso3' : 'GAB', 'site' : ''},
        'gm' : {'iso3' : 'GMB', 'site' : ''},
        'ge' : {'iso3' : 'GEO', 'site' : ''},
        'de' : {'iso3' : 'DEU', 'site' : 'https://www.morningstar.de/de/'},
        'gh' : {'iso3' : 'GHA', 'site' : ''},
        'gi' : {'iso3' : 'GIB', 'site' : ''},
        'gr' : {'iso3' : 'GRC', 'site' : ''},
        'gl' : {'iso3' : 'GRL', 'site' : ''},
        'gd' : {'iso3' : 'GRD', 'site' : ''},
        'gp' : {'iso3' : 'GLP', 'site' : ''},
        'gu' : {'iso3' : 'GUM', 'site' : ''},
        'gt' : {'iso3' : 'GTM', 'site' : ''},
        'gg' : {'iso3' : 'GGY', 'site' : ''},
        'gn' : {'iso3' : 'GIN', 'site' : ''},
        'gw' : {'iso3' : 'GNB', 'site' : ''},
        'gy' : {'iso3' : 'GUY', 'site' : ''},
        'ht' : {'iso3' : 'HTI', 'site' : ''},
        'hm' : {'iso3' : 'HMD', 'site' : ''},
        'va' : {'iso3' : 'VAT', 'site' : ''},
        'hn' : {'iso3' : 'HND', 'site' : ''},
        'hk' : {'iso3' : 'HKG', 'site' : 'https://www.morningstar.hk/hk/'},
        'hu' : {'iso3' : 'HUN', 'site' : ''},
        'is' : {'iso3' : 'ISL', 'site' : ''},
        'in' : {'iso3' : 'IND', 'site' : ''},
        'id' : {'iso3' : 'IDN', 'site' : ''},
        'ir' : {'iso3' : 'IRN', 'site' : ''},
        'iq' : {'iso3' : 'IRQ', 'site' : ''},
        'ie' : {'iso3' : 'IRL', 'site' : 'https://www.morningstarfunds.ie/ie/'},
        'im' : {'iso3' : 'IMN', 'site' : ''},
        'il' : {'iso3' : 'ISR', 'site' : ''},
        'it' : {'iso3' : 'ITA', 'site' : 'https://www.morningstar.it/it/'},
        'jm' : {'iso3' : 'JAM', 'site' : ''},
        'jp' : {'iso3' : 'JPN', 'site' : ''},
        'je' : {'iso3' : 'JEY', 'site' : ''},
        'jo' : {'iso3' : 'JOR', 'site' : ''},
        'kz' : {'iso3' : 'KAZ', 'site' : ''},
        'ke' : {'iso3' : 'KEN', 'site' : ''},
        'ki' : {'iso3' : 'KIR', 'site' : ''},
        'kp' : {'iso3' : 'PRK', 'site' : ''},
        'kr' : {'iso3' : 'KOR', 'site' : ''},
        'kw' : {'iso3' : 'KWT', 'site' : ''},
        'kg' : {'iso3' : 'KGZ', 'site' : ''},
        'la' : {'iso3' : 'LAO', 'site' : ''},
        'lv' : {'iso3' : 'LVA', 'site' : ''},
        'lb' : {'iso3' : 'LBN', 'site' : ''},
        'ls' : {'iso3' : 'LSO', 'site' : ''},
        'lr' : {'iso3' : 'LBR', 'site' : ''},
        'ly' : {'iso3' : 'LBY', 'site' : ''},
        'li' : {'iso3' : 'LIE', 'site' : ''},
        'lt' : {'iso3' : 'LTU', 'site' : ''},
        'lu' : {'iso3' : 'LUX', 'site' : ''},
        'mo' : {'iso3' : 'MAC', 'site' : ''},
        'mk' : {'iso3' : 'MKD', 'site' : ''},
        'mg' : {'iso3' : 'MDG', 'site' : ''},
        'mw' : {'iso3' : 'MWI', 'site' : ''},
        'my' : {'iso3' : 'MYS', 'site' : ''},
        'mv' : {'iso3' : 'MDV', 'site' : ''},
        'ml' : {'iso3' : 'MLI', 'site' : ''},
        'mt' : {'iso3' : 'MLT', 'site' : ''},
        'mh' : {'iso3' : 'MHL', 'site' : ''},
        'mq' : {'iso3' : 'MTQ', 'site' : ''},
        'mr' : {'iso3' : 'MRT', 'site' : ''},
        'mu' : {'iso3' : 'MUS', 'site' : ''},
        'yt' : {'iso3' : 'MYT', 'site' : ''},
        'mx' : {'iso3' : 'MEX', 'site' : 'https://www.morningstar.com.mx/mx/'},
        'fm' : {'iso3' : 'FSM', 'site' : ''},
        'md' : {'iso3' : 'MDA', 'site' : ''},
        'mc' : {'iso3' : 'MCO', 'site' : ''},
        'mn' : {'iso3' : 'MNG', 'site' : ''},
        'me' : {'iso3' : 'MNE', 'site' : ''},
        'ms' : {'iso3' : 'MSR', 'site' : ''},
        'ma' : {'iso3' : 'MAR', 'site' : ''},
        'mz' : {'iso3' : 'MOZ', 'site' : ''},
        'mm' : {'iso3' : 'MMR', 'site' : ''},
        'na' : {'iso3' : 'NAM', 'site' : ''},
        'nr' : {'iso3' : 'NRU', 'site' : ''},
        'np' : {'iso3' : 'NPL', 'site' : ''},
        'nl' : {'iso3' : 'NLD', 'site' : 'https://www.morningstar.nl/nl/'},
        'nc' : {'iso3' : 'NCL', 'site' : ''},
        'nz' : {'iso3' : 'NZL', 'site' : ''},
        'ni' : {'iso3' : 'NIC', 'site' : ''},
        'ne' : {'iso3' : 'NER', 'site' : ''},
        'ng' : {'iso3' : 'NGA', 'site' : ''},
        'nu' : {'iso3' : 'NIU', 'site' : ''},
        'nf' : {'iso3' : 'NFK', 'site' : ''},
        'mp' : {'iso3' : 'MNP', 'site' : ''},
        'no' : {'iso3' : 'NOR', 'site' : 'https://www.morningstar.no/no/'},
        'om' : {'iso3' : 'OMN', 'site' : ''},
        'pk' : {'iso3' : 'PAK', 'site' : ''},
        'pw' : {'iso3' : 'PLW', 'site' : ''},
        'ps' : {'iso3' : 'PSE', 'site' : ''},
        'pa' : {'iso3' : 'PAN', 'site' : ''},
        'pg' : {'iso3' : 'PNG', 'site' : ''},
        'py' : {'iso3' : 'PRY', 'site' : ''},
        'pe' : {'iso3' : 'PER', 'site' : ''},
        'ph' : {'iso3' : 'PHL', 'site' : ''},
        'pn' : {'iso3' : 'PCN', 'site' : ''},
        'pl' : {'iso3' : 'POL', 'site' : ''},
        'pt' : {'iso3' : 'PRT', 'site' : 'https://www.morningstar.pt/pt/'},
        'pr' : {'iso3' : 'PRI', 'site' : ''},
        'qa' : {'iso3' : 'QAT', 'site' : ''},
        're' : {'iso3' : 'REU', 'site' : ''},
        'ro' : {'iso3' : 'ROU', 'site' : ''},
        'ru' : {'iso3' : 'RUS', 'site' : ''},
        'rw' : {'iso3' : 'RWA', 'site' : ''},
        'bl' : {'iso3' : 'BLM', 'site' : ''},
        'sh' : {'iso3' : 'SHN', 'site' : ''},
        'kn' : {'iso3' : 'KNA', 'site' : ''},
        'lc' : {'iso3' : 'LCA', 'site' : ''},
        'mf' : {'iso3' : 'MAF', 'site' : ''},
        'pm' : {'iso3' : 'SPM', 'site' : ''},
        'vc' : {'iso3' : 'VCT', 'site' : ''},
        'ws' : {'iso3' : 'WSM', 'site' : ''},
        'sm' : {'iso3' : 'SMR', 'site' : ''},
        'st' : {'iso3' : 'STP', 'site' : ''},
        'sa' : {'iso3' : 'SAU', 'site' : ''},
        'sn' : {'iso3' : 'SEN', 'site' : ''},
        'rs' : {'iso3' : 'SRB', 'site' : ''},
        'sc' : {'iso3' : 'SYC', 'site' : ''},
        'sl' : {'iso3' : 'SLE', 'site' : ''},
        'sg' : {'iso3' : 'SGP', 'site' : 'https://sg.morningstar.com/sg/'},
        'sx' : {'iso3' : 'SXM', 'site' : ''},
        'sk' : {'iso3' : 'SVK', 'site' : ''},
        'si' : {'iso3' : 'SVN', 'site' : ''},
        'sb' : {'iso3' : 'SLB', 'site' : ''},
        'so' : {'iso3' : 'SOM', 'site' : ''},
        'za' : {'iso3' : 'ZAF', 'site' : ''},
        'gs' : {'iso3' : 'SGS', 'site' : ''},
        'ss' : {'iso3' : 'SSD', 'site' : ''},
        'es' : {'iso3' : 'ESP', 'site' : 'https://www.morningstar.es/es/'},
        'lk' : {'iso3' : 'LKA', 'site' : ''},
        'sd' : {'iso3' : 'SDN', 'site' : ''},
        'sr' : {'iso3' : 'SUR', 'site' : ''},
        'sj' : {'iso3' : 'SJM', 'site' : ''},
        'se' : {'iso3' : 'SWE', 'site' : 'https://www.morningstar.se/se/'},
        'ch' : {'iso3' : 'CHE', 'site' : 'https://www.morningstar.ch/ch/'},
        'sy' : {'iso3' : 'SYR', 'site' : ''},
        'tw' : {'iso3' : 'TWN', 'site' : ''},
        'tj' : {'iso3' : 'TJK', 'site' : ''},
        'tz' : {'iso3' : 'TZA', 'site' : ''},
        'th' : {'iso3' : 'THA', 'site' : ''},
        'tl' : {'iso3' : 'TLS', 'site' : ''},
        'tg' : {'iso3' : 'TGO', 'site' : ''},
        'tk' : {'iso3' : 'TKL', 'site' : ''},
        'to' : {'iso3' : 'TON', 'site' : ''},
        'tt' : {'iso3' : 'TTO', 'site' : ''},
        'tn' : {'iso3' : 'TUN', 'site' : ''},
        'tr' : {'iso3' : 'TUR', 'site' : ''},
        'tm' : {'iso3' : 'TKM', 'site' : ''},
        'tc' : {'iso3' : 'TCA', 'site' : ''},
        'tv' : {'iso3' : 'TUV', 'site' : ''},
        'ug' : {'iso3' : 'UGA', 'site' : ''},
        'ua' : {'iso3' : 'UKR', 'site' : ''},
        'ae' : {'iso3' : 'ARE', 'site' : ''},
        'gb' : {'iso3' : 'GBR', 'site' : ''},
        'um' : {'iso3' : 'UMI', 'site' : ''},
        'us' : {'iso3' : 'USA', 'site' : 'https://www.morningstar.com/'},
        'uy' : {'iso3' : 'URY', 'site' : ''},
        'uz' : {'iso3' : 'UZB', 'site' : ''},
        'vu' : {'iso3' : 'VUT', 'site' : ''},
        've' : {'iso3' : 'VEN', 'site' : ''},
        'vn' : {'iso3' : 'VNM', 'site' : ''},
        'vg' : {'iso3' : 'VGB', 'site' : ''},
        'vi' : {'iso3' : 'VIR', 'site' : ''},
        'wf' : {'iso3' : 'WLF', 'site' : ''},
        'eh' : {'iso3' : 'ESH', 'site' : ''},
        'ye' : {'iso3' : 'YEM', 'site' : ''},
        'zm' : {'iso3' : 'ZMB', 'site' : ''},
        'zw' : {'iso3' : 'ZWE', 'site' : ''},

 }



