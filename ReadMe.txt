#############################--YahooTradeData--################################
##  YahooTradeData created and supported by Pythoner AI 2021-2025
##  Version 0.90.001
##  Email: Pythoner.AI@Gmail.com
##  YouTube channel: https://www.youtube.com/channel/UC8z9vw_iuWU1N6UgGSZlFHA
##  YouTube channel short url: http://gestyy.com/etvyUe
###############################################################################

###############################################################################
##  The application is for personal use only!!!")
##  It was designed for downloading stock market data via Yahoo Finance API.")
##  There is limitation for using the Public API (without authentication), ")
##  You are limited to 2,000 requests per hour per IP or up to a total of 48,000 requests a day per IP")
##  We do not guarantee the data is accurate and no delay.")
###############################################################################


#########################Config.ini###########################
Interval could be: 1d, 1h, 2m, 1m, 2s,5s,15s
Max period:
1d: all history data for each day
1h: last 2 year's data for every one hour
2m: last 60 days data for every 2 mins
1m: last 7 days data for every one min
2s, 5s, 15s, 30s: retrieve data every 2,5,15 second keep running until manual stop it or market close.

Stock market open and close time in your local time.

#########################EquityList.txt###########################
yahoo stock id, max 40 stocks, min 2 stocks
Canada stock suffix is .TO, such as SHOP.TO, WELL.TO
Shanhai stock suffix is .SS such as 600660.SS (Fuyao Glass Industry Group Co., Ltd. )
Shengzhen stock suffix is .SZ such as 000002.SZ (China Vanke Co., Ltd.)
###################################################################

#################$###########--App--###############################
Date format:
Equity,Date(time),Open,high,low,adjustclose,close(most recent price),volume

when retrieve date by 2s, 5s, 15s, 30s, the volumne may not reflect actual value
Stock markets of China may delay 15 mins

