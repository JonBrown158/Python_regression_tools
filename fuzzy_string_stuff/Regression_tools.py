from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from data_table import Data_table
from Duplex import Duplex
from Duplex import Loader
from scipy import stats
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import itertools
import warnings
import numpy as np
import csv 

plt.style.use('fivethirtyeight')

## initialize table bring in information from deals folder 
titles = Data_table('data',',')

print("number of rows {}".format(titles.num_rows))

Names = titles.get_column('title')
UUID = titles.get_column('uuid')
Price = titles.get_column('price')
Description = titles.get_column('description')
Date = titles.get_column('time_published')
print(titles.order, '\n')

print("\n\n\n")

## set these to determine which row you want to use, and  to what sensitivity you want the 
## string compairason done to 
PriceCheck = True
while(PriceCheck):
	row = int(input('Pick the row you would like to run regression on. '))
	sensitivity = int(input('Pick the percent you would like the strings to match. '))

	if(titles.rows[row][Price][0] != '$'):
		print('Entry does not have a vaild price.\nIt must be an advertisment. \nEnter a diffrent row and try again.\n')
	else:
		PriceCheck = False

target = titles.rows[row][Names]
print("matches for {} are".format(target))
prices = []
index = []
lastUUid = 0
lastPrice = 'na'


i = 0
j = 1
while(i < titles.num_rows):
    if(fuzz.token_sort_ratio(titles.rows[i][Names], target) > sensitivity):
        if(lastUUid != titles.rows[i][UUID] or lastPrice != titles.rows[i][Price]):
            print(titles.rows[i][Names], 'uuid {}'.format(titles.rows[i][UUID]),'price {}'.format(titles.rows[i][Price]), i)
            lastPrice = titles.rows[i][Price]
            titles.rows[i][Price] = titles.rows[i][Price].replace("$", "")
            titles.rows[i][Price] = titles.rows[i][Price].replace(",","")
            prices.append(float(titles.rows[i][Price]))
            index.append(j)
            lastUUid = titles.rows[i][UUID]
            
            j += 1
    i +=1

x = np.array(index)
y = np.array(prices)
	
linearRegression = int(input('Do you want to run linear regression '))

if(linearRegression == 1):
    
    	
    slope, intercept, r_value, p_value, std_err = stats.linregress(index, prices)

    print("r-squared:", r_value**2)


    plt.plot(x, y, 'o', label='original data')
    plt.plot(x, intercept + slope * x, 'r', label="fitted line")
    plt.legend()
    plt.show()	

if(linearRegression == 2):

    p = int(input('enter a value for p '))
    d = int(input('enter a value for d '))
    q = int(input('enter a value for q '))
        
    #fit model
    model = ARIMA(y, order=(p,d,q))
    model_fit = model.fit(disp= 0)
    print(model_fit.summary())
    #plot residual errors
    residuals = DataFrame(model_fit.resid)
    residuals.plot()
    plt.show()
    residuals.plot(kind = 'kde')
    plt.show()
    print(residuals.describe())

    X = y
    size = int(len(X) * 0.66)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
    	model = ARIMA(history, order=(p,d,q))
    	model_fit = model.fit(disp=0)
    	output = model_fit.forecast()
    	yhat = output[0]
    	predictions.append(yhat)
    	obs = test[t]
    	history.append(obs)
    	print('predicted=%f, expected=%f' % (yhat, obs))
    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)
    # plot
    plt.plot(test)
    plt.plot(predictions, color='red')
    plt.show()


