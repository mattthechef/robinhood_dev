#first install the robin-stocks in anaconda prompt
#open anaconda prompt
#paste in this: pip install robin-stocks
#click enter to install

#open up spyder and try running the following


#load up the robin_stocks
import robin_stocks as r 

#can skip this step if you just want to pull back prices, etc 
#the login would be used if you were to build functions that would sell/buy based on certain criteria
#enter in your email and password
login = r.login('austinschachtner@gmail.com','password')


#first example of pulling price by passing in string directly
acn_cur_price =r.stocks.get_latest_price('ACN', includeExtendedHours=True)

#only works when market is open? unable to pull the price of this, check documentation
dowjone_cur_price =r.stocks.get_latest_price('DJI', includeExtendedHours=True)

#example of creating a string variable
bpmx = 'BPMX'
#get current price
bpmx_cur_price =r.stocks.get_latest_price(bpmx, includeExtendedHours=True)


#initialize a list of stocks
dans_fav_stocks = ['ACN','BPMX','F','TELL','CRK']

#initalize a blank list to add prices to
stock_price=[]

#loop through the list of stocks to grab the price and append to a list object
for symbol in dans_fav_stocks:
    price = r.stocks.get_latest_price(symbol, includeExtendedHours=True)
    stock_price.append(price)


#similar loop but captures the latest price in a dictionary with the key = symbol and value = price
stock_dictionary={}
for symbol in dans_fav_stocks:
    price = r.stocks.get_latest_price(symbol, includeExtendedHours=True)
    stock_dictionary[symbol] = price

#next steps
#import pandas as pd
#start builing array of prices for stats


#pull back earnings
#list of dictionaries, pretty complex but could simplify
bpmx_earnings = r.stocks.get_earnings('BPMX', info=None)
dowjones_earnings = r.stocks.get_earnings('DJI', info=None)