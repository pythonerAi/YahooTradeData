from datetime import datetime as dt
import datetime
import time
import TradeData as TD
import App
import log


def realtime():
    tickers = MyApp.tickers()
    messaged = False
    MyTD.interval = MyApp.interval
    while True:
        if dt.now() > MyApp.close:
            print("The market is closing, this app will be closed soon...")
            time.sleep(50)
            break
        if dt.now() >= MyApp.open:

            MyTD.get_realtime(tickers, dt.now() + datetime.timedelta(seconds=-150))
            time.sleep(MyApp.realtimeInterval)
        else:
            if not messaged:
                print("The stock market is not start yet, please waiting...")
            time.sleep(2)


def historical():
    tickers = MyApp.tickers()
    MyTD.get_new(tickers, MyApp.interval)

MyLog = log.Log()
MyApp = App.App()
MyTD = TD.TradeData()
MyApp.config()
MyApp.copyleft()
MyTD.start = MyApp.open
# print(MyApp.open)

#check now in trading tim
if MyApp.interval in ["2s", "5s", "15s", "30s"]:

    if dt.now() > MyApp.open + datetime.timedelta(minutes=-15) and dt.now() < MyApp.close \
            and dt.today().weekday() < 5:
        # run realtime
        realtime()
        time.sleep(MyApp.realtimeInterval)

    else:
        MyLog.warning("Please run YahooTradeData for realtime downloading after 15 minutes before stock market starts. ")
        time.sleep(40)
elif MyApp.interval in ["2m", "1m", "1h", "1d"]:
    historical()

    MyLog.infor("This task has been completed, the application will be closed soon...")
    time.sleep(30)
else:
    MyLog.error("Please check config.ini file, set up valid interval.")
    time.sleep(100)





# historical download


