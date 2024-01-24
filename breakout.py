# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:44:37 2024

@author: hansd
"""
#%% Imports
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


#%% Downloading stock data from 10 major stocks over 3 year period
start_date = "2019-01-01"
end_date = "2022-01-01"

tesla = yf.download("TSLA", start_date,end_date)
apple = yf.download("AAPL",start_date,end_date)
amazon = yf.download("AMZN",start_date,end_date)
microsoft = yf.download("MSFT",start_date,end_date)
nvidia = yf.download("NVDA",start_date,end_date)
alphabet = yf.download("GOOGL",start_date,end_date)
meta = yf.download("META",start_date,end_date)
nio = yf.download("NIO",start_date,end_date)
coca = yf.download("KO",start_date,end_date)
mcdonalds = yf.download("MCD",start_date,end_date)

#%% Defining functiion to display stock data
def display_stockdata(stock_data,symbol):
    plt.figure(figsize=(10,6))
    plt.plot(stock_data["Close"],label="Closing Price")
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.title(f'{symbol} Stock Price USD From 2019 to 2022')
    plt.legend()
    plt.show()
    
display_stockdata(tesla,"TSLA")
display_stockdata(apple,"AAPL")
display_stockdata(amazon,"AMZN")
display_stockdata(microsoft,"MSFT")
display_stockdata(nvidia,"NVDA")
display_stockdata(alphabet,"GOOGL")
display_stockdata(meta,"META")
display_stockdata(nio,"NIO")
display_stockdata(coca,"KO")
display_stockdata(mcdonalds,"MCD")

#%% Calculating support and resistance levels

#Support: Price at which a stock tends to stop falling and might bounce back
#Resistance: Price at which an asset stop rising and may face difficulty rising higher

# Using moving averages

def moving_averages_simple(stock_data,symbol):
    stock_data["SMA_50"] = stock_data["Close"].rolling(window=50).mean()
    stock_data["SMA_200"] = stock_data["Close"].rolling(window=200).mean()
    
    plt.figure(figsize=(12,6))
    plt.plot(stock_data['SMA_50'], label='50-day SMA', linestyle='--', linewidth=1.5)
    plt.plot(stock_data['SMA_200'], label='200-day SMA', linestyle='--', linewidth=1.5)
    
    support_dates = stock_data.index[stock_data['SMA_50'] > stock_data['SMA_200']]   #Added to stop the error from missing data in closed column
    resistance_dates = stock_data.index[stock_data['SMA_50'] < stock_data['SMA_200']]
    plt.scatter(support_dates, stock_data['Close'].loc[support_dates], marker='^', color='g', label='Support (50-day > 200-day)')
    plt.scatter(resistance_dates, stock_data['Close'].loc[resistance_dates], marker='v', color='r', label='Resistance (50-day < 200-day)')
    
    plt.title(f'{symbol} Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    
moving_averages_simple(tesla,"TSLA")
#%%
def moving_averages_exponential(stock_data,symbol):
    stock_data['EMA_10'] = stock_data['Close'].ewm(span=10, adjust=False).mean()
    stock_data['EMA_20'] = stock_data['Close'].ewm(span=20, adjust=False).mean()
    
    plt.figure(figsize=(12,6))
    plt.plot(stock_data['EMA_10'], label='10-day EMA', linestyle='--', linewidth=1.5)
    plt.plot(stock_data['EMA_20'], label='20-day EMA', linestyle='--', linewidth=1.5)
    
    support_dates = stock_data.index[stock_data['EMA_10'] > stock_data['EMA_20']]   #Added to stop the error from missing data in closed column
    resistance_dates = stock_data.index[stock_data['EMA_10'] < stock_data['EMA_20']]
    plt.scatter(support_dates, stock_data['Close'].loc[support_dates], marker='^', color='g', label='Support (10-day > 20-day)')
    plt.scatter(resistance_dates, stock_data['Close'].loc[resistance_dates], marker='v', color='r', label='Resistance (10-day < 20-day)')
    
    plt.title(f'{symbol} Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

moving_averages_exponential(tesla,"TSLA")