#!/usr/bin/env python

"""
StockPortfolioSuggestionEngine.py

This program accepts a ticker-symbol as input, and will output the most recent closing price and one-day price change.

HW #2
CMPE 285-01
Spring 2018
San Jose State University

Author: Vincent Chao
"""

# Modules
from datetime import datetime as dt
import pandas_datareader.data as pdr


def retrieve_stock_data(symbol):
    """
    Implements pandas_datareader to extract data from RobinHood's API into a pandas DataFrame.
    :param symbol: String, ticker-symbol of the stock who's data is to be retrieved.
    :return: pandas DataFrame object of stock data
    """
    data = pdr.DataReader(symbol, 'robinhood')
    nasdaq = pdr.get_nasdaq_symbols()
    name = nasdaq["Security Name"][symbol]
    return data, name


def calc_price_changes(data):
    """
    Takes a pandas dataframe object and calculated the price changes.
    :param data: pandas DataFrame object of stock data
    :return: floats for current closing price, the change in value, and the percent change in value.
    """
    old_price = float(data["close_price"][-2])
    current_price = float(data["close_price"][-1])

    value_change = current_price - old_price
    percent_change = (current_price - old_price) / old_price

    return current_price, value_change, percent_change


def main():
    while True:
        symbol = input("Please enter a symbol (or enter 'stop' to exit):\n")

        if symbol == 'stop':
            break

        try:
            data, name = retrieve_stock_data(symbol)
            stock_price, value_change, percent_change = calc_price_changes(data)

            print("\nOutput:")
            print("{:%a %b %d %H:%M:%S %Y}".format(dt.now()))
            print(name)
            print("{0:.2f} {1:+.2f} ({2:+.2f}%)".format(stock_price, value_change, percent_change))
            print()

        except KeyError:
            "Error: Invalid symbol."
            continue


if __name__ == "__main__":
    main()
