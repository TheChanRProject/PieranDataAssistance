import sys
import matplotlib
import ipy_lib
from scipy import stats
import numpy as np

ui = ipy_lib.StockMarketUserInterface(enable_cache=True)


startDate = '2017-05-01'
endDate = '2017-06-01'
quotes = ui.get_stock_quotes('MSFT', startDate, endDate)
stock = quotes[0].values()
print stock
