import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime as dt
import datetime
from dateutil.relativedelta import *
import math
import time
import os.path
from os import path
import pytz as tz
import log


class TradeData:
    def __init__(self):
        self.interval = ""
        self.maximum = False
        self.start = dt.now() #this actual value set by YahooTradeData.py
        self.realtimedata = []
        self.Log = log.Log()
        self.showMessage = True
        self.logMessage = True

        print(yf.__version__)
        return

    def get_new(self, tickers, interval):
        for ticker in tickers:
            # check if file exists
            filename = ".\\Data\\" + ticker + "_" + interval + ".csv"
            lasttime = None
            if os.path.exists(filename):
                #get last day
                f = open(filename, "r")
                lines = f.readlines()
                validtime = self.get_validstart(interval)
                if len(lines) > 0:
                    lastline = lines[-1]
                    if lastline == "\n":
                        lastline = lines[-2]
                    if interval == "1d":
                        lasttime = dt.strptime(lastline.split(",")[1], "%Y-%m-%d %H:%M:%S")
                        starttime = dt.strptime(lastline.split(",")[1], "%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=1)
                    elif interval == "1h":
                        starttime = dt.strptime(lastline.split(",")[1], "%Y-%m-%d %H:%M:%S") + datetime.timedelta(seconds=50)
                    else:
                        starttime = dt.strptime(lastline.split(",")[1], "%Y-%m-%d %H:%M:%S%z") + datetime.timedelta(seconds=50)
                        starttime = dt.strptime(dt.strftime(starttime, "%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                    validtime = max(starttime, validtime)
                f.close()

                if interval == "1d":
                    if not lasttime:
                        data = yf.download(ticker)
                    else:
                        data = yf.download(ticker, start=validtime)
                else:
                    data = yf.download(ticker, interval=interval, start=validtime)
            else:
                validtime = self.get_validstart(interval)
                if interval == "1d":
                    data = yf.download(ticker, start=datetime.date(1770, 1, 1))
                else:
                    data = yf.download(ticker, interval=interval, start=validtime)

            if len(data) > 0:
                os.makedirs(".\\Data", exist_ok=True)
                f = open(filename, "a+")
                f.write('Ticker, Date(time), close, high, low, Open, volume' + "\n")
                cnt = len(data)
                before = dt.now().replace(hour=0, minute=0, second=0, microsecond=0)
                seq = 0
                for tradetime, market in data.iterrows():
                    #set formated tradetime

                    if interval == "1h":
                        if tradetime == before:
                            seq = seq + 1
                        else:
                            before = tradetime
                            seq = 0
                        tradetime = self.sethour(tradetime, seq)
                    if lasttime is not None:
                        if tradetime <= lasttime:
                            continue

                    if self.roundmarket(market) < 0:
                        continue
                    row = []
                    row.append(ticker)
                    a = str(tradetime)
                    row.append(a)
                    strings = [str(value) for value in market]
                    row = row + strings
                    f.write(",".join(row) + "\n")
                    self.Log.infor(",".join(row))

                f.close()
            else:
                self.Log.infor("No new trading data for " + ticker + " after " + lastline.split(",")[0])

        return

    def get_realtime(self, tickers, start):

        if start >= dt.now() + relativedelta(seconds=-1100):
            start = dt.now() + relativedelta(seconds=-1100)

        str_tickers = ' '.join(tickers)
        data = yf.download(str_tickers, interval="1m", start=start, group_by="ticker")

        for ticker in tickers:
            os.makedirs(".\\Data", exist_ok=True)
            f = open(".\\Data\\" + ticker + "_" + self.interval + ".csv", "a")
            f.write('Ticker, Date(time), close, high, low, Open, volume' + "\n")

            if len(data[ticker]) > 0:
                for time_, market in data[ticker].iterrows():

                    if self.roundmarket(market) < 0:
                        continue
                    row = []
                    row.append(ticker)

                    #a = time.strftime("%Y-%m-%d, %H:%M:%S")
                    a = time_.strftime("%Y-%m-%d, %H:%M:%S%z")
                    row.append(a)
                    strings = [str(value) for value in market]
                    row = row + strings
                    if row in self.realtimedata:
                        self.Log.infor("found duplicate for row: " + ' '.join(row))
                        continue
                    self.realtimedata.append(row)
                    f.write(",".join(row) + "\n")
                    self.Log.infor(",".join(row))
                    #break
            f.close()
        return

    def get_validstart(self, interval):
        if interval == "1d":
            validtime = dt.now() + relativedelta(years=-50)
        elif interval == "1h":
            validtime = dt.now() + relativedelta(days=-720)
        elif interval == "2m":
            validtime = dt.now() + relativedelta(days=-59)
        else:
            validtime = dt.now() + relativedelta(days=-6)


        return validtime

    def roundmarket(self, market):
        if math.isnan(market[0]):
            return -1
        else:
            market[0] = round(market[0], 3)

        if math.isnan(market[1]):
            return -1
        else:
            market[1] = round(market[1], 3)
        if math.isnan(market[2]):
            return -1
        else:
            market[2] = round(market[2], 3)
        if math.isnan(market[3]):
            return -1
        else:
            market[3] = round(market[3], 3)
        if math.isnan(market[4]):
            return -1
        else:
            market[4] = round(market[4])

        return 1

    def sethour(self, date, seq):
        today = dt.today().replace(hour=0, minute=0, second=0, microsecond=0)
        date = date.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds = (self.start - today).total_seconds()
        hour = date + datetime.timedelta(seconds=seconds + seq * 3600)
        return hour








