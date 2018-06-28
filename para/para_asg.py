import sys
import matplotlib
import ipy_lib
from scipy import stats
import numpy as np

ui = ipy_lib.StockMarketUserInterface(enable_cache=True)

def today_price(x):
    startDate = '2017-05-01'
    endDate = '2017-06-01'
    quotes = ui.get_stock_quotes(x, startDate, endDate)
    last_quote = quotes[0]
    adj_closing_price = float(last_quote['Adj_Close'])
    return adj_closing_price

def yesterday_price(x):
    startDate = '2017-05-01'
    endDate = '2017-05-31'
    quotes = ui.get_stock_quotes(x, startDate, endDate)
    last_quote = quotes[0]
    adj_closing_price = float(last_quote['Adj_Close'])
    return adj_closing_price


stock_list = 'MSFT AAPL IBM GE FB'.split(' ')

todayPrices = [today_price(stock) for stock in stock_list]
yesterdayPrices = [yesterday_price(stock) for stock in stock_list]
print todayPrices
print yesterdayPrices

# Calculating Returns
def returnToday(x,y):
    return (x-y)/y

returnMSFT = returnToday(todayPrices[0], yesterdayPrices[0])
returnAAPL = returnToday(todayPrices[1], yesterdayPrices[1])
returnIBM = returnToday(todayPrices[2], yesterdayPrices[2])
returnGE = returnToday(todayPrices[3], yesterdayPrices[3])
returnFB = returnToday(todayPrices[4], yesterdayPrices[4])

returnList = [returnToday(todayPrices[i], yesterdayPrices[i]) for i in range(len(todayPrices))]
print returnList

# Calculating Correlation Coefficients of Stocks

def correlationCoeff(stockOne,stockTwo):
    startDate = '2017-05-01'
    endDate = '2017-06-01'
    quote1 = ui.get_stock_quotes(stockOne, startDate, endDate)
    quote2 = ui.get_stock_quotes(stockTwo, startDate, endDate)
    last_quote1 = np.array(quote1[0].values())
    last_quote2 = np.array(quote2[0].values())
    r_value = np.corrcoef(last_quote1, last_quote2)
    return r_value[0][1]

print correlationCoeff('MSFT', 'AAPL')
