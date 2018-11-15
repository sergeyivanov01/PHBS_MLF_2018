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

The goal of this project is to estimate the price for Brent using Machine Learning. In order to predict the prices in the given dataset, I plan to use time series regression (ARIMA). The price estimation is planned to predict Brent oil price from October 15, 2018 to November 15, 2018. The reason why I only make a prediction for one month is because to realistically estimate the price, it is important to account for unpredictable events such as new oil field discoveries, geopolitical situation and etc.

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
ARIMA model has computed the following output:


predicted=77.654031, expected=75.350000

predicted=75.850825, expected=72.110000

predicted=72.271320, expected=74.110000

predicted=74.294124, expected=71.030000

predicted=71.046181, expected=70.870000

predicted=71.658132, expected=70.520000

predicted=70.520835, expected=71.940000

predicted=71.853183, expected=71.990000

predicted=72.225880, expected=73.450000

predicted=73.492727, expected=73.530000

predicted=73.497259, expected=73.670000

predicted=73.608196, expected=74.510000

predicted=74.455843, expected=74.840000

predicted=74.709107, expected=74.990000

predicted=75.053395, expected=74.160000

predicted=74.224997, expected=72.280000

predicted=72.356481, expected=72.950000

predicted=72.979091, expected=72.480000

predicted=72.483628, expected=72.510000

predicted=72.762705, expected=72.310000

predicted=72.500376, expected=70.710000

predicted=70.799820, expected=70.550000

predicted=70.677324, expected=71.000000

predicted=70.961975, expected=70.620000

predicted=70.732725, expected=70.770000

predicted=70.964294, expected=68.380000

predicted=68.488951, expected=69.210000

predicted=69.255603, expected=70.140000

predicted=70.008162, expected=71.110000

predicted=71.162192, expected=71.650000

predicted=71.759266, expected=72.960000

predicted=72.844012, expected=73.730000

predicted=73.612559, expected=74.410000

predicted=74.371852, expected=74.410000

predicted=74.384940, expected=75.910000

predicted=75.828210, expected=76.070000

predicted=76.021459, expected=77.050000

predicted=77.097996, expected=76.940000

predicted=76.963726, expected=77.810000

predicted=77.791225, expected=77.510000

predicted=77.545106, expected=76.680000

predicted=76.755879, expected=75.670000

predicted=75.751125, expected=75.550000

predicted=75.537767, expected=76.770000

predicted=76.797472, expected=78.220000

predicted=78.308519, expected=80.020000

predicted=80.162134, expected=77.660000

predicted=77.752504, expected=77.870000

predicted=77.892225, expected=78.220000

predicted=78.079958, expected=79.250000

predicted=79.244055, expected=79.430000

predicted=79.597936, expected=79.030000

predicted=79.101299, expected=78.900000

predicted=78.945849, expected=80.890000

predicted=80.851428, expected=82.210000

predicted=82.197763, expected=81.870000

predicted=81.950940, expected=81.540000

predicted=81.619249, expected=82.720000

predicted=82.690943, expected=84.940000

predicted=84.913017, expected=85.630000

predicted=85.650590, expected=85.450000

predicted=85.541825, expected=86.070000

predicted=86.154719, expected=85.120000

predicted=85.149747, expected=84.220000

predicted=84.352182, expected=85.160000

predicted=85.278720, expected=83.820000

predicted=83.888123, expected=81.350000

predicted=81.568624, expected=80.710000

predicted=80.887699, expected=80.910000

![ARIMA Prediction](https://github.com/sergeyivanov01/PHBS_MLF_2018/blob/master/ARIMA%20prediction.png)
