import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

#method that stores the s&p 500 csv into pandas data frame
stocks = pd.read_csv('sp_500_stocks.csv')


#import IEX_CLOUD_API_TOKEN
#nick mcculum messed up so couldn't download the secrets file


#making api call to iex cloud
symbol=stocks['Ticker'][0]
api_url=f'https://cloud.iexapis.com/stable/stock/{symbol}/quote/?token=pk_0c3ce561962d44188076a4128787fe86'
data=requests.get(api_url).json()


#parsing api call to get price and market cap from the data
price = data['latestPrice']
marketcap = data['marketCap']

#adding stocks data to pandas dataframe(sth like a spreadsheet that stores tabular data)
impt_details = ['Ticker','Stock Price','Market Cap','No of shares to buy']
info=[symbol,price,marketcap,'N/A']
df = pd.DataFrame({'Ticker':[symbol],'Stock Price':[price],'Market Cap':[marketcap],'No of shares to buy':['N/A']})
print(df)




#loop through all the tickers in stocks variable
for stock in stocks['Ticker'][1:]:

    #making api call to iex cloud
    symbol=stock
    api_url=f'https://cloud.iexapis.com/stable/stock/{symbol}/quote/?token=pk_0c3ce561962d44188076a4128787fe86'
    data=requests.get(api_url).json()


    #parsing api call to get price and market cap from the data
    price = data['latestPrice']
    marketcap = data['marketCap']

    #adding stocks data to pandas dataframe(sth like a spreadsheet that stores tabular data)
    dataframe = pd.DataFrame({'Ticker':[symbol],'Stock Price':[price],'Market Cap':[marketcap],'No of shares to buy':['N/A']})
    df = pd.concat([df,dataframe])

print(df)









