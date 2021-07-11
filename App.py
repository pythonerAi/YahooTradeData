from datetime import datetime as dt
import log
import time
import os

from dateutil.relativedelta import *


class App:
    Tickers = []

    def __init__(self):
        self.interval = ""
        self.max = False
        self.open = ""
        self.close = ""
        self.realtimeInterval=1000
        self.MyLog = log.Log()

    def config(self):
        with open("config.ini") as f:
            lines = f.read().splitlines()

        for line in lines:
            if "Interval" in line:
                self.interval = line.split("=", 1)[1].strip().lower()
                if self.interval in ["2s","5s", "15s", "30s"]:
                    self.realtimeInterval = int(self.interval[:-1].strip())
                continue
            if "Max" in line:
                ismax = line.split("=", 1)[1].strip().lower()
                if ismax == "true":
                    self.max = True
                continue

            if "Open" in line:
                opentime = line.split("=", 1)[1].strip().lower()
                date_time_str = dt.now().strftime("%Y-%m-%d") + " " + opentime
                self.open = dt.strptime(date_time_str, "%Y-%m-%d %H:%M:%S.%f")
                continue

            if "Close" in line:
                close = line.split("=", 1)[1].strip().lower()
                date_time_str = dt.now().strftime("%Y-%m-%d") + " " + close
                self.close = dt.strptime(date_time_str, "%Y-%m-%d %H:%M:%S.%f")
                continue
            if "##############" in line:
                break

    def copyleft(self):
        print("")
        print("")
        print("#############################--YahooTradeData--################################")
        print("##  YahooTradeData created and supported by Pythoner AI 2021-2025")
        print("##  Version 0.90.002")
        print("##  Email: Pythoner.AI@Gmail.com")
        print("###############################################################################")
        print("")
        print("###############################################################################")
        print("##  The application is for personal use only!!!")
        print("##  It was designed for downloading stock market data via Yahoo Finance API.")
        print("##  There is limitation for using the Public API (without authentication), ")
        print("##  You are limited to 2,000 requests per hour per IP or up to a total of 48,000 requests a day per IP")
        print("##  We do not guarantee the data is accurate and no delay.")
        print("###############################################################################")
        print("Jul 10, 2021   Version 0.90.002      Upgrade yfinance ver: 0.1.63")
        print("###############################################################################")
        print("")
        print("")

        #https://towardsdatascience.com/free-stock-data-for-python-using-yahoo-finance-api-9dafd96cad2e

    def tickers(self):
        f = open("EquityList.txt", "r")
        tickers = []
        while True:
            ticker = ''.join(f.readline().splitlines())
            if len(ticker.strip()) == 0:
                break
            tickers.append(''.join(ticker))
        if len(tickers) < 2:
            self.MyLog.error("The number of equities in EquityList.txt must be at least 2. please add more.\
                            The app will close soon...")
            time.sleep(100)
        return tickers

    def tickerstring(self):
        tickers = self.tickers()
        str_tickers = ' '.join(tickers)
        return str_tickers


    def make_dir(self):
        if not os.path.exists(".\\Data"):
            os.mkdir(".\\Data")



