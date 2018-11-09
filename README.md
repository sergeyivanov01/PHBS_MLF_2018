# PHBS_MLF_2018
**Brent Oil Price Prediction**

Sergey Ivanov 1701213211

sergeyivanov01


**Motivation**

The oil market influences nearly all aspects of our lives. At large, nearly every industry, if not all depend on it in some way. Oil is not only used to power vehicles, but it is also used in production of many goods, such as plastic, including nylon and polyester clothing, rubber, and hundreds of other intermediate and end-user goods. In 2017, U.S. consumed 19.96 million barrels per day on average. Since oil is not a renewable source of energy, it will run out someday. Since the demand for it is increasing, while supply is diminishing, it is likely that the oil prices will rise.


**Description of data**

The chosen dataset presents Brent oil price per barrel since May 1987 to October 2018. The overall trend is showing that oil prices are rising. I decided to choose Brent oil because it is one of the most recognizable brands, which is why it is reasonable to assume that this sector is the most reflective in terms of oil prices. The dataset is taken from United States Energy Information Administration, which is why this data may be considered accurate.


![1987-2018 BP](https://github.com/sergeyivanov01/PHBS_MLF_2018/blob/master/1987-2018%20price.png)


 As you can see from this graph, there are a lot of fluctuations caused by external factors. In this case it is 2008 financial crisis and fracking boom. This is why it is better to limit the dataset to recent market price:
 
 
![2018 Brent Oil Price](https://github.com/sergeyivanov01/PHBS_MLF_2018/blob/master/2018%20price.png)
 
 
**Goal of the project**

The goal of this project is to estimate the price for Brent using Machine Learning. In order to predict the prices in the given dataset, I plan to use time series regression (ARIMA). The price estimation is planned to predict Brent oil price from October 15, 2018 to November 15, 2018. It would be interesting to compare the estimation from the model with the actual data from EIA, which I will recover closer to the date of the course project presentation. The reason why I only make a prediction for one month is because to realistically estimate the price, it is important to account for unpredictable events such as new oil field discoveries, geopolitical situation and etc.

**Time Series Forecast**
Time Series forecast is dependent on time, which is why in order to make a forecast it is important to link it to time. It is assumed that Time series is stationary, meaning that it has constant mean, variance and autocovariance. Due to that, it is possible to make a forecast in the future. In order to check for stationary points, I plotted rolling statistics and conducted Dickey-Fuller test.

Results of Dickey-Fuller Test:
Test Statistic                  -1.797204
p-value                          0.381851
#Lags Used                      13.000000
Number of Observations Used    176.000000
Critical Value (1%)             -3.468062
Critical Value (5%)             -2.878106
Critical Value (10%)            -2.575602
dtype: float64


However, practical data is rarely perfectly stationary, but there is a way to make it as stationary as possible. There are 2 reasons for non-stationary time series:

1) trend
2) seasonality

I decided to use decomposing in order to make this TS data more stationary. Decomposition – modeling both trend and seasonality and removing them from the model.

**ARIMA Model**

ARIMA stands for Auto-Regressive Integrated Moving Averages. 
The ARIMA forecasting for a stationary time series is nothing but a linear (like a linear regression) equation. The predictors depend on the parameters (p,d,q) of the ARIMA model:

Number of AR (Auto-Regressive) terms (p): AR terms are just lags of dependent variable. For instance if p is 5, the predictors for x(t) will be x(t-1)….x(t-5).

Number of MA (Moving Average) terms (q): MA terms are lagged forecast errors in prediction equation. For instance if q is 5, the predictors for x(t) will be e(t-1)….e(t-5) where e(i) is the difference between the moving average at ith instant and actual value.

Number of Differences (d): These are the number of nonseasonal differences, i.e. in this case we took the first order difference. So either we can pass that variable and put d=0 or pass the original variable and put d=1. Both will generate same results.


An importance concern here is how to determine the value of ‘p’ and ‘q’. We use two plots to determine these numbers. 

![Autocorrelation and Partial Autocorrelation Function](https://github.com/sergeyivanov01/PHBS_MLF_2018/blob/master/2018%20autocorr.png)

**Conclusion**
At the current time, I am still trying to debug the code that I wrote. I tried a lot of things and searched a lot online for a possible solution, but I couldnt find anything helpful for my case. I am getting this error:

ValueError: view limit minimum -36849.1 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units

Sadly, this error is the last step required to make a forecast and I did not get it to work yet. I will find out why I got this error within a week, and if you have any suggestions, please let me know what you think.


