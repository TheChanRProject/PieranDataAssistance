import sys
import matplotlib
import ipy_lib

ui = ipy_lib.StockMarketUserInterface(enable_cache=True)

def get_price(x):
    startDate = '2017-05-01'
    endDate = '2017-06-01'
    quotes = ui.get_stock_quotes(x, startDate, endDate)
    last_quote = quotes[0]
    adj_closing_price = float(last_quote['Adj_Close'])
    print adj_closing_price
get_price('MSFT')
get_price('AAPL')
get_price('IBM')
get_price('GE')
get_price('FB')
