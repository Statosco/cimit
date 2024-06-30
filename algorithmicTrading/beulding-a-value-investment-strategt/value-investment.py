import numpy as np
import pandas as pd
import xlsxwriter
import requests
from scipy import stats
import math

IEX_CLOUD_API_TOKEN = 'pk_d682a6e68e2143458a9a7eed913ba701'

stocks = pd.read_csv('diploma/algorithmicTrading/beulding-an-equal-weight-S&P-500-index-fund/sp_500_stocks.csv')
apiUrl = f'https://sandbox.iexapis.com/stable/stocks{stocks}/quote?Token={IEX_CLOUD_API_TOKEN}'

data= requests.ge(apiUrl).json()

price = data['latesPrice']
peRatio = data['peRatio']

def chunkc(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

symbolGroups = list(chunkc(stocks['Ticker'], 100))
symbolStr = []

for i in range(0, len(symbolGroups)):
    symbolStr.append(','.join(symbolGroups[i]))

myColumns = ['Ticker', 'Price', 'One Year Price Return', 'Numbers Of Shares To Buy']

dataFrame = pd.DataFrame(columns=myColumns)

for symbolString in symbolStr:
    batchApi = f'https://sandbox/cloud.iexapis.com/stable/stock/market/batch?symbols={symbolString}&types=quote&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batchApi).json()
    for symbol in symbolString.split(','):
        dataFrame = dataFrame.append(
            pd.Series(
                [
                    symbol,
                    data[symbol]['quotes']['latestPrice'],
                    data[symbol]['quotes']['peRatio'],
                    'N/A'
                ],
                index=myColumns
            ),
            ignore_index = True
        )

dataFrame.sort_values('Price-to-Earning Ratio', inplace=True)
dataFrame = dataFrame[dataFrame['Price-to-Earning Ratio'] > 0]
dataFrame = dataFrame[:50]
dataFrame.reindex(inplace=True)
dataFrame.drop('index',axis=1,inplace=True)

def portfolioSize():
    global portfoliosze
    portfoliosze = input("Enter portfolio size --->> ")

    try:
        float(portfoliosze)
    except ValueError:
        print("Please enter a number")

positionSize = float(portfoliosze)/len(dataFrame.index)

for row in dataFrame.index:
    dataFrame.loc[row, 'Number of Shares to Buy'] = math.floor(portfolioSize/dataFrame.loc[row, 'price'])

symbol = 'AApl'
batchApi = f'https://sandbox/cloud.iexapis.com/stable/stock/market/batch?symbols={symbol}&types=quote,advanved-stats&token={IEX_CLOUD_API_TOKEN}'
data = requests.get(batchApi).json()

peRatio = data[symbol]['quotes']['latestPrice'],

pbRatio = data['AAPL']['advanced-stats']['priceToBook']
psRatio =  data['AAPL']['advanced-stats']['priceToSales']
entVal =  data['AAPL']['advanced-stats']['enterpriseValue']
ebida =  data['AAPL']['advanced-stats']['EBIDA']
evtoebida = entVal/ebida
grossProf =  data['AAPL']['advanced-stats']['grossProfit']
evGross = entVal/grossProf

rvCols = [
    'Ticker',
    'Price',
    'Number of Shares to buy',
    'Price-toEarning Ratio',
    'PE percentile',
    'Price-to-Book Ratio',
    'PB Percentile',
    'Price-to-Sales Ratio',
    'PS Percentile',
    'Ev/EBIDA',
    'Ev/EBIDA Percentile',
    'EV/GP',
    'EV/GP Percentile',
    'RV Score'
]
rvdataf = pd.DataFrame(columns=rvCols)

for symbolst in symbolStr:
    batchApi = f'https://sandbox/cloud.iexapis.com/stable/stock/market/batch?symbols={symbolst}&types=quote,advanved-stats&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batchApi).json()
    for symbol in symbolst.split(','):
        evtoebida = entVal/ebida
        grossProf =  data[symbol]['advanced-stats']['grossProfit']
        evGross = entVal/grossProf

        try:
            evtoebda = entVal/ebida
        except TypeError:
            evtoebida = np.NaN
        try:
            evtogross = entVal/grossProf
        except TypeError:
            evtogross = np.NaN

        rvdataf = rvdataf.append(
            pd.Series([
                data[symbol]['quote']['latestPrice'],
                'N/A',
                data[symbol]['quote']['peRatio'],
                'N/A',
                data[symbol]['advanced-stats']['priceToBook'],
                'N/A',
                data[symbol]['advanced-stats']['priceToSales'],
                'N/A',
                evtoebida,
                'N/A',
                evtogross,
                'N/A',
                'N/A'
            ],index=rvCols),ignore_index=True
        )

rvdataf[rvdataf.isnull().any(axis=1)]

for cols in ['Price-toEarning Ratio', 'Price-to-Book Ratio', 'Price-to-Sales Ratio', 'Ev/EBIDA', 'EV/GP']:
    rvdataf[cols].fillna(rvdataf[cols].mean(), inplace=True)

metrics = {
    'Price-toEarning Ratio' : 'PE percentile',
    'Price-to-Book Ratio' : 'PB Percentile',
    'Price-to-Sales Ratio' : 'PS Percentile',
    'Ev/EBIDA' : 'Ev/EBIDA Percentile',
    'EV/GP' : 'EV/GP Percentile',
}

for metric in metrics.keys():
    for row in rvdataf.index:
        rvdataf.loc[row, metrics[metric]] = stats.percentileofscore(rvdataf[metric], rvdataf.loc[row, metrics[metric]])

from statistics import mean

for row in rvdataf.index:
    valuePer = []
    for metric in metrics.keys():
        valuePer.append(rvdataf.loc[row, metrics[metric]])
    rvdataf.loc[row, 'RV Score'] = mean(valuePer)

rvdataf.sort_values('RV Score', ascending=True, inplace=True)
rvdataf = rvdataf[:50]
rvdataf.reset_index(drop=True,inplace=True)

portfolioSize()

positionSize = float(portfoliosze/len(rvdataf.index))
for row in rvdataf.index:
    rvdataf.loc[row, 'Number of Shares to Buy']= math.floor(positionSize/rvdataf.loc[row, 'Price'])

writer = pd.ExcelWriter('Value_strategy.xlsx', engine='xlsxwriter')
rvdataf.to_excel(writer, sheet_name='Value_strategy', index=False)

backgroundColor = '#0a0a23'
fontColor = '#ffffff'

stringF = writer.book.add_format({'font_color':fontColor,'bg_color':backgroundColor,'border':1})
dollarF = writer.book.add_format({'num_format':'0','font_color':fontColor,'bg_colo':backgroundColor,'border':1})
intF = writer.book.add_format({'num_format':'0.0%','font_color':fontColor,'bg_colo':backgroundColor,'border':1})

columnFormat = {
    'A':['Ticker', stringF],
    'B':['Price', dollarF],
    'C':['Number of Shares to buy', dollarF],
    'D':['Price-toEarning Ratio', dollarF],
    'E':['PE percentile', intF],
    'F':['Price-to-Book Ratio', dollarF],
    'G':['PB Percentile', intF],
    'H':['Price-to-Sales Ratio', dollarF],
    'I':['PS Percentile', intF],
    'J':['Ev/EBIDA', stringF],
    'K':['Ev/EBIDA Percentile', intF],
    'L':['EV/GP', stringF],
    'M':['EV/GP Percentile', intF],
    'N':['RV Score', dollarF]
}
for cols in columnFormat.keys():
    writer.sheets['Value_strategy'].set_column(f'{cols}:{cols}',25, columnFormat[cols][1])
    writer.sheets['Value_strategy'].write(f'{cols}1', columnFormat[cols][0], columnFormat[cols][1])
writer.save()


