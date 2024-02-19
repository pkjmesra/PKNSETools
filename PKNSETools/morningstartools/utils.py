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


USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.6",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.2",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.4",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.",
    "Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/604.",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.",
    "Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.119 Mobile/15E148 Safari/604.",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.6167.66 Mobile/15E148 Safari/604.",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/300.0.598994205 Mobile/15E148 Safari/604.",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (Linux; Android 10; YAL-L21; HMSCore 6.13.0.302; GMSCore 24.02.13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.2.311 Mobile Safari/537.3",
    "Mozilla/5.0 (Linux; Android 11; moto e20 Build/RONS31.267-94-14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.3",
    "Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G990B2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.119 Mobile/15E148 Safari/604.",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/120.0.2210.144",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edge/44.18363.8131",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/120.0.2210.144",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.3; rv:109.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.3; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:109.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (X11; Linux i686; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.6167.66 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 EdgiOS/120.2210.150 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/122.0 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPod; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/121.0.6167.66 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPod touch; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/122.0 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (iPod touch; CPU iPhone 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/122.0 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (iPad; CPU OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 EdgA/120.0.2210.141",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 EdgA/120.0.2210.141",
    "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 EdgA/120.0.2210.141",
    "Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 EdgA/120.0.2210.141",
    "Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 Edge/40.15254.603",
    "Mozilla/5.0 (Android 14; Mobile; rv:109.0) Gecko/122.0 Firefox/122.0",
    "Mozilla/5.0 (Android 14; Mobile; LG-M255; rv:122.0) Gecko/122.0 Firefox/122.0",
    "Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 OPR/76.2.4027.73374",
    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 OPR/76.2.4027.73374",
    "Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 OPR/76.2.4027.73374",
    "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A536U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Google Pixel 6
    "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Google Pixel 6a
    "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Google Pixel 6 Pro
    "Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Google Pixel 7
    "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Google Pixel 7 Pro
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Motorola Moto G Pure
    "Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Motorola Moto G Stylus 5G
    "Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36v",
    #Motorola Moto G Stylus 5G (2022)
    "Mozilla/5.0 (Linux; Android 12; moto g stylus 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Motorola Moto G 5G (2022)
    "Mozilla/5.0 (Linux; Android 12; moto g 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Motorola Moto G Power (2022)
    "Mozilla/5.0 (Linux; Android 12; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Motorola Moto G Power (2021)
    "Mozilla/5.0 (Linux; Android 11; moto g power (2021)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Various popular Android models
    #Redmi Note 9 Pro
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Redmi Note 8 Pro
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Huawei P30 Pro
    "Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Huawei P30 lite",
    "Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Redmi Note 10 Pro",
    "Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Xiaomi Poco X3 Pro",
    "Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Redmi Note 11 Pro 5G",
    "Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #OnePlus Nord N200 5G",
    "Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    #Apple iPhone SE (3rd generation)",
    "Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1",
    #iPhone 13 Pro Max",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
    #iPhone 12",
    "Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1 ",
    #iPhone 11",
    "Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1 ",
    #iPhone 11",
    "Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1 ",
    #Apple iPhone XR (Safari)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
    #Apple iPhone XS (Chrome)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",
    #Apple iPhone XS Max (Firefox)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15",
    #Apple iPhone X",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    #Apple iPhone 8",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
    #Apple iPhone 8 Plus",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1",
    #Apple iPhone 7",
    "Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1",
    #Apple iPhone 7 Plus",
    "Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1",
    #Apple iPhone 6",
    "Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3",
    #MS Windows Phone User Agents",
    #Microsoft Lumia 650",
    "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
    #Microsoft Lumia 550",
    "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
    #Microsoft Lumia 950",
    "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
    #Tablet User Agents
    #Samsung Galaxy Tab S8 Ultra",
    "Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
    #Lenovo Yoga Tab 11",
    "Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    #Google Pixel C"
    "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36", 
    #Sony Xperia Z4 Tablet",
    "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
    #Nvidia Shield Tablet K1",
    "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
    #Samsung Galaxy Tab S3",
    "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
    #Samsung Galaxy Tab A",
    "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
    #Amazon Kindle Fire HDX 7",
    "Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36",
    #LG G Pad 7.0",
    "Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36",
    #Desktop User Agents
    #Windows 10-based PC using Edge browser",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    #Chrome OS-based laptop using Chrome browser (Chromebook)",
    "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
    #Mac OS X-based computer using a Safari browser",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
    #Windows 7-based PC using a Chrome browser",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    #Linux-based PC using a Firefox browser",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    #Bring device intelligence to your web applications in minutes.
    #Bots and Crawlers User Agents
    #Google bot",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    #Bing bot",
    "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    #Yahoo! bot",
    "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
    #E Readers User Agents
    #Amazon Kindle 4",
    "Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+",
    #Amazon Kindle 3",
    "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)"
]




def random_user_agent():
    """
    This function selects a random User-Agent from the User-Agent list, . User-Agents are used in
    order to avoid the limitations of the requests to morningstar.com. The User-Agent is
    specified on the headers of the requests and is different for every request.

   

    Returns:
        :obj:`str` - user_agent:
            The returned :obj:`str` is the name of a random User-Agent, which will be passed on the 
            headers of a request so to avoid restrictions due to the use of multiple requests from the 
            same User-Agent.
    
    """

    return random.choice(USER_AGENTS)





