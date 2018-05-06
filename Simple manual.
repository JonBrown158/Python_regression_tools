#Linear Regression and ARIMA analysis tools
## Simple users guide 
### Jonathan Brown

####1. Where to put data
There should be a folder in the repository called **Data**, any files that we are trying to preform regression should be placed into there. The python I have written pulls the data from that folder and loads it into itself from that folder. 

####2. How to use the tools that have been provided.
Once time series data from the deals website has been added, regression can be preformed by running the **Regression_tools.py** .

After that is completed you will be prompted for which row you would like  to prefom the string matches on, and preform basic checks that the intended row is not an advertisment.  

Then it will ask if you would like to run linear regression, or ARIMA analysis.
Pick 1 for linear or 2 for ARIMA.

####3. Linear regression.

If linear regression was chosen the python will take the data points from the data file, and create a best fit line, then plot it against the data for compairason and give the values for the slope and intercept of the line that was created. 

####4. ARIMA 

If ARIMA is chosen the next step in producing the analysis is to pick the paramaters you want for the regression. These are P which determines the amount of terms you want in the autoregressive portion of the equation, D the level of differencing you need to make the data stationary, and Q the amount of terms in the moving average part of the model. 

##### Choosing Approprate terms for P, D, and Q

The ARIMA model requires several assumptions to produce anything useful for modeling furture trends, The first of these things is that your data is stationary. 
**Stationality**  - The data does not have a significant trend in it. or that over time the mean of the data should remain the same. 
If this requirement is not met then the rest of the model will produce nothing useful. 
This is not saying that we cannot use non-stationary data, it means that we have to make our data stationary. The simplest way to accomplish this is to diffrence the data. 
By subtracting the current term by previous terms we can make the data stationary, and this is where the D term in the ARIMA(P, D, Q). 
The larger the D term is the more terms are diffrenced from the first term, generally either the term behind it or two terms behind it. This makes it so that we are predicting the change in our data which should be stationary. 

For P we are trying to find how the current terms are related to the previous ones, and to do this we make another assumption, that the current term is related to the last ones by a function resembling   
** xt = (xt-1)(a) + (xt-2)(a2) + (xt-3)(a3)  ...  + error **.  
These coefficents labeled by me as "a" are what we are focused on finding with this part of the Modling. These terms are selected by finding the coeffiects that lead to the smallest error when used to find existing values. This still leaves information in the model that can be extracted in other ways. Thats why there is moving average. 

For Q we are trying to deterimine if the error of the AutoRegressive part of this model may be modeled by a moving average function, and the number of terms we want to include in this model is what is denoted by Q. 

Selecting the proper values for each of these terms will increase the accuracy of the model and allow greater precision with forcasts made from them . 