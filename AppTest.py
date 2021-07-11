import App
from datetime import datetime as dt
import pytz
import time
#import gmtime, strftime

# newApp = App.App()
#
# newApp.config()
#
# print(newApp.interval, newApp.max, newApp.open, newApp.close)
#
# print("gvredyte6"[:-1])

a = '2021-01-11 00:00:00+08:00'
b = dt.strptime(a,'%Y-%m-%d %H:%M:%S%z')
c = b.strftime('%Y-%m-%d %H:%M:%S')
d = dt.strptime(c,'%Y-%m-%d %H:%M:%S%z')
# a = '2021-01-11 00:00:00'
# b = dt.strptime(a,'%Y-%m-%d %H:%M:%S').timetz() #.astimezone(pytz.utc)
# c = pytz.utc.localize()
print(time.strftime("%z", time.gmtime()), type(time.gmtime()))

print(d, type(d))
print(d, type(d))
