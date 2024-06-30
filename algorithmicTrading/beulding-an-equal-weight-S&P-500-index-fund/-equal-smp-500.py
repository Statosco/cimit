import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math


stocks = pd.read_csv('forex\\beulding-an-equal-weight-S&P-500-index-fund\\sp_500_stocks.csv')

from secretstoken import IEX_CLOUD_API_TOKEN

symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url)

price = data['latest price']
marketCap = data['marketCap']
print(marketCap/ 1000000000000)


myColumn = ['Ticker', 'Stock Price', 'Market Capitalization', 'Number Of Shares To Buy']
fDataF = pd.DataFrame(columns= myColumn)

fDataF.append(pd.Series([
    symbol, 
    price, 
    marketCap, 
    'N/A'
],index=myColumn),

ignore_index = True)

fDataF = pd.DataFrame(columns=myColumn)
for stock in stocks['Ticker']:
    api_url = f'https://sandbox.iexapis.com/stable/stock/{stock}/quote/?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url)
    fDataF = fDataF.append(pd.Series([stock,data['latest price'],data['marketCap'],'N/A'],index=myColumn),ignore_index = True)
def chunkc(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

symbolGroups = list(chunkc(stocks['Ticker'], 100))
symbolStr = []
for i in range(0, len(symbolGroups)):
    symbolStr.append(','.join(symbolGroups[i]))
fDataF = pd.DataFrame(columns=myColumn)
for symbolStrs in symbolStr:
    batchApiCallUrl = f''
    data = requests.get(batchApiCallUrl).json()
    for symbol in symbolStr.split(','):
        fDataF = fDataF.append(pd.Series([symbol,data[symbol]['quote']['latestPrice'],data[symbol]['quote']['marketCap'],],index=myColumn),ignore_index=True)

portforlioSize = input('enter the value of your portforlio -->> ')
try:
    val = float(portforlioSize)
except ValueError:
    print("please enter an integer -->> ")
    portforlioSize = input('enter the value of your portforlio -->> ')
    val = float(portforlioSize)


positionSize = val/len(fDataF)
for i in range(0, len(fDataF.index)):
    fDataF.loc[i, 'Number Of Shares To Buy'] = math.floor(positionSize/fDataF.loc[i, 'Stock Price'])

writer = pd.ExcelWriter('recommended trades.xlsx', engine='xlsxwriter')
fDataF.to_excel(writer, 'recommended Trades', index=False)

backgroundColor = '#0a0a23'
fontColor = '#ffffff'

stringF = writer.book.add_format({'font_color':fontColor,'bg_color':backgroundColor,'border':1})
dollarF = writer.book.add_format({'num_format':'$0.00','font_color':fontColor,'bg_colo':backgroundColor,'border':1})
intF = writer.book.add_format({'num_format':'$0.00','font_color':fontColor,'bg_colo':backgroundColor,'border':1})

writer.sheets['Recomended Trades'].set_column('A:A', 18, stringF)
writer.sheets['Recomended Trades'].set_column('B:B', 18, stringF)
writer.sheets['Recomended Trades'].set_column('C:C', 18, stringF)
writer.sheets['Recomended Trades'].set_column('D:D', 18, stringF)

writer.sheets['Recomendend Trade'].write('A1','Ticker',stringF)
writer.sheets['Recomendend Trade'].write('B1','Stock Price',dollarF)
writer.sheets['Recomendend Trade'].write('C1','Market Capitalication',dollarF)
writer.sheets['Recomendend Trade'].write('E1','No Of Shares To Buy',intF)

column_format = {
    'A': ['Ticker', stringF],
    'B': ['Stock Price', dollarF],
    'C': ['Market Capitalization', dollarF],
    'D': ['Number Of Shares To Buy', intF]
}

for column in column_format.keys():
    writer.sheets['Recomended Trades'].set_column(f'{column}:{column}',18, column_format[column][1])
    writer.sheets['Recomended Trades'].write(f'{column}1',column_format[column][0],column_format[column][1])
writer.save()