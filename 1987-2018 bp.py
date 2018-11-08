import pandas as pd
import numpy as np
import matplotlib.pylab as plt
data = pd.read_csv('a.csv')# -*- coding: utf-8 -*-
dateparse = lambda dates: pd.datetime.strptime(dates, '%d.%m.%Y')
data = pd.read_csv('a.csv', parse_dates=['Date'],index_col='Date', date_parser=dateparse)
print (data.head)
print (data.dtypes)
data.index
ts = data
plt.plot(ts)
 
"""
Редактор Spyder

Это временный скриптовый файл.
"""

