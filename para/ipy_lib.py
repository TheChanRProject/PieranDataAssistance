"""
Created on 30 Jan. 2012
Finished on 6 Feb. 2012 (its still not finished though)

Improvements:
 - 1 Mar. 2012 to 2 Mar. 2012: fixed a rare threading related crash
 - 3 Mar. 2012 to 5 Mar. 2012: fixed a bug in showing names of the barchart
 - 17 Mar. 2012 to 18 Mar. 2012: fixed not running on Linux
 - 31 Jul. 2012 to 31 Jul. 2012: added UserInput and 'privatised' most classes and imports
 - 1 Aug. 2012 to 2 Aug. 2012: fixed another bug with showing names of the barchart and a bug with displaying text in othello
 - 4 Aug. 2012 to 4 Aug. 2012: fixed bug with opening a file and fixed functionality of closing the window
 - 6 Aug. 2012 to 7 Aug. 2012: fixed multiple windows crashing the UI, reverted change to UserInput with this change
 - 21 Aug. 2012 to 21 Aug. 2012: adjusted naming from JAVA to Python convention, changed UserInput to a function that returns all input, added Life interface
 - 22 Aug. 2012 to 22 Aug. 2012: added scrollbar to othello, snake and life interfaces, added type checking and exceptions for all input
 - 2 Sep. 2012 to 2 Sep. 2012: fixed another bug with names of the barchart, allowed ints to be given to floats, fixed spelling
 - 13 Sep. 2012 to 13 Sep. 2012: fixed more spelling, added functionality for multiple answers per question
 - 27 Sep. 2012 to 27 Sep. 2012: changed multiple answers from array to arbitrary arguments list, added exception if argument list is empty
 - 6 Dec. 2012 to 6. Dec. 2012: fixed resets of auto alarm speed by adding a timer
 - 2 Oct. 2013 to 3. Oct. 2013: fixed ranged errors, fixed closing bug in Windows and Linux when only calling ask_user or file_input,
                                fixed typos, added Escape as window closer, fixed window not getting focus when started, added Mac support (!)
 - 9 Oct. 2013 to 9. Oct. 2013: fixed get_event (Mac version) to properly give refresh events
 - 12 Nov. 2014 to 12. Nov. 2014: fixed OS X to not use PIL anymore and instead of images draw some simple shapes
 - 21 Nov. 2014 to 21. Nov. 2014: fixed OS X BarChartUI to properly show bar names without calling show
 - 15 May. 2015 to 15 May. 2015: added user interfaces for programming for economy -- Sebastian
 - 22 Jun. 2015 to 22 Jun. 2015: fixed asking twice for file_input on Windows -- Gerben
 - 17 Jun. 2016 to 17 Jun. 2016: Major cleanup
@author: Gerben Rozie
@author: Sebastian Osterlund
"""

import sys as _sys
import time as _time
import datetime as _datetime
import pickle as _pickle
import urllib2
import urllib
import json

have_mpl = False
try:
    import matplotlib as mpl

    if _sys.platform == 'linux' or _sys.platform == 'linux2':
        mpl.rcParams['backend'] = 'QT4Agg'
    import pylab as plt

    if _sys.platform == 'linux' or _sys.platform == 'linux2':
        plt.switch_backend('QT4Agg')  # Use QT4 for linux. Bug in TK.
    have_mpl = True
except ImportError:
    print "Could not import matplotlib. HouseMarketUserInterface and StockMarketUserInterface have been disabled."

YAHOO_URL = 'https://query.yahooapis.com/v1/public/yql'
ALPHA_VANTAGE_URL = 'http://www.alphavantage.co/query'


class StockMarketUserInterface(object):
    def __init__(self, enable_cache=True):
        """
        User interface for the stocks assignment.

        Variables:
            enable_cache: if set to True retrieved data will be cached.
        """
        if not have_mpl:
            raise Exception('Use of HouseMarketUserInterface has been disabled.')
        self._enable_cache = enable_cache
        pass

    def _yql_query(self, q, _format, env):
        req = {
            'q': q,
            'format': _format,
            'env': env
        }

        data = urllib.urlencode(req)
        whole_url = YAHOO_URL + '?' + data
        request = urllib2.Request(whole_url)
        handler = urllib2.urlopen(request)
        response = json.loads(handler.read())
        return response

    def _av_query(self, symbol):
        whole_url = ALPHA_VANTAGE_URL + "?function=TIME_SERIES_DAILY&apikey=Z2YF&symbol=%s&outputsize=full" % symbol
        request = urllib2.Request(whole_url)
        handler = urllib2.urlopen(request)
        response = json.loads(handler.read())
        if 'Error Message' in response:  # retry once... AV fails... decently often
            request = urllib2.Request(whole_url)
            handler = urllib2.urlopen(request)
            response = json.loads(handler.read())
        return response

    def _check_time_interval(self, start, end):
        st = _time.strptime(start, "%Y-%m-%d")
        en = _time.strptime(end, "%Y-%m-%d")
        ds = _datetime.datetime.fromtimestamp(_time.mktime(st))
        de = _datetime.datetime.fromtimestamp(_time.mktime(en))
        # ddays = (de - ds).days
        #
        # if ddays > 365:
        #     raise Exception("The largest time interval the API can handle is 365 days.")

    def _load_cache(self, key):
        try:
            fp = open(".stock_cache", "rb")
            db = _pickle.load(fp)
            return db.get(key, None)
        except Exception:
            return None

    def _store_cache(self, key, value):
        db = {}
        try:
            with open(".stock_cache", "rb") as fp:
                try:
                    db = _pickle.load(fp)
                except Exception:
                    pass
        except Exception:
            pass

        with open(".stock_cache", "wb+") as fp:
            db[key] = value
            _pickle.dump(db, fp)

    def _cache_hash(self, symbol, start, end):
        return symbol + start + end

    def _av_rekey(self, dictionary):
        rekey = {
            'Adj_Close': '4. close',  # for the original assignment
            'open': '1. open',
            'high': '2. high',
            'low': '3. low',
            'close': '4. close',
            'volume': '5. volume'
        }
        new = {}
        for v, k in rekey.iteritems():
            if k in dictionary:
                new[v] = float(dictionary[k])
        return new

    def get_stock_quotes(self, symbol, start, end):
        """
        Returns a list of dictionaries containing Yahoo historical stock quotes for variable 'symbol'.

        Variables:
        - symbol: (stock symbol e.g. AAPL, IBM, MSFT)
        - start: start date of historical interval. Format: yyyy-mm-dd
        - end: end date of historical interval. Format: yyyy-mm-dd

        The Yahoo API supports a max time interval of 365 day, thus an exception is raised if
        the interval between start and end > 365 days.

        """
        self._check_time_interval(start, end)

        if self._enable_cache:
            cached = self._load_cache(self._cache_hash(symbol, start, end))
            if cached:
                return cached

        response = self._av_query(symbol)
        if 'Error Message' in response:
            raise Exception("No data available for quote symbol %s." % symbol)

        results = response['Time Series (Daily)']  # type: dict
        # fuck its not sorted
        st = _time.strptime(start, "%Y-%m-%d")
        sp = _time.strptime(end, "%Y-%m-%d")
        quotes = filter(lambda t: sp >= t[0] >= st, [(_time.strptime(x[0].split()[0], "%Y-%m-%d"), x[1]) for x in results.items()])
        formatted_quotes = map(lambda x: self._av_rekey(x[1]), sorted(quotes,key=lambda x: x[0], reverse=True))
        if self._enable_cache:
            self._store_cache(self._cache_hash(symbol, start, end), formatted_quotes)
        return formatted_quotes

    def plot(self, prices, color, **kwargs):
        """
        Plots the list of prices. With the color specified by the string 'color'.

        Possible colors: 'b', 'g', 'r'
        Use show() to display the plotted data.

        Variables:
            prices: list of floats with prices to be plotted.
            **kwargs: (optional) additional kwargs.
        """
        t = plt.arange(0, len(prices), 1)
        lines = plt.plot(t, prices, c=color)
        kwargs['linewidth'] = 2.0
        plt.setp(lines, **kwargs)
        return lines

    def show(self):
        """
        Draw the current state of the ui.
        """
        plt.ylabel('Returns')
        plt.xlabel('Day')
        plt.show()


class HouseMarketUserInterface(object):
    def __init__(self):
        if not have_mpl:
            raise Exception('Use of HouseMarketUserInterface has been disabled.')
        self.max_x = 0  # Keep track of max observer x-value

    def plot_dot(self, x, y, color, **kwargs):
        """
        Plot the point (x,y) in the ui. With the color specified by the string 'color'.
        Possible colors: 'b', 'g', 'r'

        Arguments:
            x: float
            y: float

        Advanced functionality: a list of floats may be supplied to both x and y to draw many points in one step.

        """
        if isinstance(x, list):
            self.max_x = max(max(x), self.max_x)
        else:
            self.max_x = max(x, self.max_x)
        plt.plot(x, y, 'o', c=color, **kwargs)

    def plot_line(self, *args, **kwargs):
        """
        Plot the polynomial represented by the coefficients provided.

        E.g. plot_line(2,1) would plot the function '2 + 1 * x'
             plot_line(3,4,5) plots '5*x^2 + 4*x + 3'
        """
        t = plt.arange(0.0, self.max_x, 0.01)
        func = lambda x: sum([args[i] * (x ** i) for i in range(len(args))])
        return plt.plot(t, func(t), **kwargs)

    def show(self):
        """
        Draw the current state of the ui.
        """
        plt.ylabel('House Price')
        plt.xlabel('House Size (m^2)')
        orig_limit_x = plt.xlim()
        orig_limit_y = plt.ylim()
        a = plt.xlim(orig_limit_x[0], self.max_x + 0.1 * self.max_x)
        a = plt.ylim(orig_limit_y[0] - 0.1 * orig_limit_y[0], orig_limit_y[1])
        plt.show()


class BarChartUserInterface(object):
    def __init__(self, bar_count):
        self._bars = [[str(x), 0] for x in range(bar_count)]
        self._show_names = False

    def raise_bar(self, bar_index):
        self._bars[bar_index][1] += 1

    def set_bar_name(self, bar_index, name):
        self._bars[bar_index][0] = name

    def close(self):
        _sys.exit(0)

    def show(self):
        size_ratio = 20.0 / max(1, max([x[1] for x in self._bars]))
        for i in range(len(self._bars)):
            name, count = self._bars[i]
            hashes = '#' * int(count * size_ratio)
            if not self._show_names:
                name = str(i)

            print '%10s: %-20s (%d)' % (name, hashes, count)

    def show_names(self):
        self._show_names = True

    def show_values(self, bool):
        pass

    def wait(self, ms):
        pass

    def stay_open(self):
        pass
