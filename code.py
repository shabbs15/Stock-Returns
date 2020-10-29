import yfinance as yf
import os
import datetime
import sys

f = open('product.csv','w')
f.write("Ticker, Price, 1 Day, 1 week, 1 month, 3 month, 1 year")
f.write("\n")
f.close()

oneDay = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y-%m-%d')
oneWeek = (datetime.datetime.now() - datetime.timedelta(7)).strftime('%Y-%m-%d')

oneMonth = (datetime.datetime.now() - datetime.timedelta(30)).strftime('%Y-%m-%d')
oneMonthUp = (datetime.datetime.now() - datetime.timedelta(31)).strftime('%Y-%m-%d')

threeMonth = (datetime.datetime.now() - datetime.timedelta(90)).strftime('%Y-%m-%d')
threeMonthUp = (datetime.datetime.now() - datetime.timedelta(91)).strftime('%Y-%m-%d')

oneYear = (datetime.datetime.now() - datetime.timedelta(365)).strftime('%Y-%m-%d')
oneYearUp = (datetime.datetime.now() - datetime.timedelta(366)).strftime('%Y-%m-%d')


print("Paste Tickers")
tickers = sys.stdin.read()

print("Paste Prices")
prices = sys.stdin.read()

for index, itTicker in enumerate(tickers.split()):
    print(itTicker)
    realTicker = yf.Ticker(itTicker)

    priceToday = float(prices.split()[index])

    oneDayVal = realTicker.history(period = "2d",actions = False).values.tolist()[0][3]
    oneWeekVal = realTicker.history(period = "7d",actions = False).values.tolist()[1][3]

    oneMonthVal = realTicker.history(start = oneMonthUp, end = oneMonth, actions = False).values.tolist()
    threeMonthVal = realTicker.history(start = threeMonthUp, end = threeMonth, actions = False).values.tolist()
    oneYearVal = realTicker.history(start = oneYearUp, end = oneYear, actions = False).values.tolist()


    oneMonthVal = oneMonthVal[0][3]
    threeMonthVal = threeMonthVal[0][3]
    oneYearVal = oneYearVal[0][3]



    print(itTicker, oneDayVal, oneWeekVal, oneMonthVal, threeMonthVal, oneYearVal)

    tickerString = itTicker + ", " + str(priceToday) +", "+ str(priceToday/oneDayVal-1) + ", " + str(priceToday/oneWeekVal-1) + ", " + str(priceToday/oneMonthVal-1) + ", " + str(priceToday/threeMonthVal-1) + ", " + str(priceToday/oneYearVal-1)

    f = open('product.csv','a')

    f.write(tickerString)
    f.write("\n")
    f.close()


os.system('product.csv')
sys.exit()
