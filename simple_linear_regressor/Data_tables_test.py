from data_table import Data_table
import csv
import os


path = r"/home/jonathan/Desktop/python junk/stockPrices/AAPL.csv"

stock_data = Data_table(path)


print(stock_data.rows[0])
print(stock_data.rows[1])
print(stock_data.lables)
print(stock_data.num_rows)
print(stock_data.num_col)
print(stock_data.rows[1][4])
