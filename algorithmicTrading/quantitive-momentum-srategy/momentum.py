import numpy as np
import pandas as pd
import requests
import math
from scipy import stats
import xlsxwriter

stock = pd.read_csv('beulding-an-equal-weight-S&P-500-index-fund/sp_500_stocks.csv')

from secrets import IEX_CLOUD_API_TOKEN

symbol = 'AAPL'
apiUrl = f'https://sandbox.iexapis.com/stable/stock{symbol}/stats?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(apiUrl).json()

data = []

def chunkc(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

symbolGroups = list(chunkc(stock['Ticker'], 100))
symbolStr = []

for i in range(0, len(symbolGroups)):
    symbolStr.append(','.join(symbolGroups[i]))

myColumns = ['Ticker', 'Price', 'One Year Price Return', 'Numbers Of Shares To Buy']

fdtaframe = pd.DataFrame(columns=myColumns)

for symbolStrs in symbolStr:
    batchApiCallUrl = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbolStr},fb&types=quote.news.chart&token={IEX_CLOUD_API_TOKEN}'
    data.requests.get(batchApiCallUrl).json()

    for symbol in symbolStr.split(','):
        fdtaframe = fdtaframe.append(
            pd.Series(
                [
                    symbol,
                    data[symbol]['price'],
                    data[symbol]['stats']['yearlChangePercent'],
                    'N/A'
                ],
            index=myColumns),
            ignore_index = True
        )


fdtaframe.sort_values("One Year Price Return", ascending=False, inplace=True)
fdtaframe = len(fdtaframe[:50])
fdtaframe.reset_index(drop=True, inplace=True)


def portfolioSize():
    global portfolioSze
    portfolioSze = input("Enter portfolio size --->> ")

    try:
        float(portfolioSze)
    except ValueError:
        print("Please enter a number")

positionize = float(portfolioSze)/len(fdtaframe.index)
for i in range(0, len(fdtaframe)):
    fdtaframe.loc[i, "Number of Shares to Buy"] = math.floor(positionize/fdtaframe.loc[i, 'Price'])

hqmCols = [
    "Ticker",
    "Price",
    "Number of Share to Buy",
    "One-Year Price Return",
    "One-Year Return Percentle",
    "Six-Months Price Return",
    "Six-Month Return Percentile",
    "Three-Month Price Return"
    "Three-Month Return percentile",
    "One-Month Price Return",
    "One-Month Return Percentile",
    "Hqm Score"
]
hqmDta = pd.DataFrame(columns=hqmCols)

for symbolStrs in symbolStr:
    batchApiCallUrl = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbolStr},fb&types=quote.news.chart&token={IEX_CLOUD_API_TOKEN}'
    data.requests.get(batchApiCallUrl).json()
    for symbol in symbolStrs.split(','):
        hqmDta = hqmDta.append(
            pd.Series(
                [
                    symbol,
                    data[symbol]["price"],
                    "N/A",
                    data[symbol]["stats"]["yearlChangePercent"],
                    "N/A",
                    data[symbol]["stats"]["month6ChangePercent"],
                    "N/A",
                    data[symbol]["stats"] ["month3ChangePercent"],
                    "N/A",
                    data[symbol]["stats"] ["month1ChangePercent"],
                    "N/A",
                    "N/A"
                ],
            index=hqmCols),
            ignore_index =True
        )

timePeriod = [
    "One-Year",
    "Six-Months",
    "Three-Month",
    "One-Month",
]
for row in hqmDta.index:
    for timeperiod in timePeriod:
        changeCol =f'{timePeriod} Price Return'
        percentilCol = f"{timePeriod} Return Percentle"
        hqmDta.loc[row, percentilCol] = stats.percentileofscore(hqmDta[changeCol] ,hqmDta.loc[row, changeCol]/100)



from statistics import mean

for row in hqmDta.index:
    momentumPec = []
    for timeperiod in timePeriod:
        momentumPec.append(hqmDta.loc[row, f"{timePeriod} Return Percentile"])
    hqmDta.loc[row, 'Hqm Score'] = mean(momentumPec)

hqmDta.sort_values('Hqm Score', ascending=False, inplace=True)
hqmDta = hqmDta[:50]
hqmDta.reset_index(drop=True,inplace=True )

portfolioSize()

portfolioSze = float(portfolioSze)/len(hqmDta.index)
for i in hqmDta.index:
    hqmDta.loc[1, "Number of Share to Buy"] = math.floor(positionize/hqmDta.loc[1, "Price"])


write = pd.ExcelWriter("momentumStrategy.xlsx", engine='xlsxwriter')

hqmDta.to_excel(write, sheet_name='momentumSrategy',index=False)

backgroundColor = '#0a0a23'
fontColor = '#ffffff'

stringF = write.book.add_format({'font_color':fontColor,'bg_color':backgroundColor,'border':1})
dollarF = write.book.add_format({'num_format':'0','font_color':fontColor,'bg_colo':backgroundColor,'border':1})
intF = write.book.add_format({'num_format':'0.0%','font_color':fontColor,'bg_colo':backgroundColor,'border':1})

colFormats={
    'A': ["Ticker", stringF],
    'B': ["Price", dollarF],
    'C': ["One-Year Price Return", intF],
    'D': ["Number of Share to Buy",intF],
    'E': ["One-Year Return Percentle",intF],
    'F': ["Six-Months Price Return",intF],
    'G': ["Six-Month Return Percentile",intF],
    'H': ["Three-Month Price Return",intF], 
    'I': ["Three-Month Return percentile",intF],
    'k': ["One-Month Price Return",intF],
    'K': ["One-Month Return Percentile",intF],
    'L': ["Hqm Score",intF]
}
for col in colFormats.keys():
    write.sheets['momentumStrategy'].set_column(f'{col}:{col}', 25, stringF[col][1])
    write.sheets['momentumStrategy'].write(f'{col}',colFormats[col][0], colFormats[col][1])

write.save()