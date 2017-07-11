#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:04:54 2017

@author: miao
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

weather_2012 = pd.read_csv('./data/weather_2012.csv', parse_dates=True, index_col='Date/Time')
print weather_2012[:5]

"""
5.1字符串操作
从上面的数据里面可以看到，有 'Weather' 这一列。我们这里假定包含 "Snow" 的才是下雪天。
pandas的str类型提供了一系列方便的函数，比如这里的contains，
"""
weather_description = weather_2012['Weather']
is_snowing = weather_description.str.contains('Snow')
print is_snowing[:5]
is_snowing.plot()

"""
5.2 平均气温
如果我们想知道每个月的温度值中位数，有一个很有用的函数可以调用哈，叫 resample()
"""
weather_2012['Temp (C)'].resample('M',how=np.median).plot(kind='bar')

"""
布尔型的 True 和 False其实是不便于运算的，当然，其实他们就是0和1了，所以我们转成float型去做做运算可好？
"""
print is_snowing.astype(float)[:10]

"""
用 resample 去找到每个月下雪的比例状况
"""
print is_snowing.astype(float).resample('M', how=np.mean)
is_snowing.astype(float).resample('M', how=np.mean).plot(kind='bar')

"""
5.3 画一下温度和雪期
我们把温度和下雪概率放到一起，组成dataframe的2列，然后画个图
"""
temperature = weather_2012['Temp (C)'].resample('M', how=np.median)
is_snowing = weather_2012['Weather'].str.contains('Snow')
snowiness = is_snowing.astype(float).resample('M', how=np.mean)

# 给列取个名字
temperature.name = "Temperature"
snowiness.name = "Snowiness"

#用 concat 把这两列拼接到一列中，组成一个新的dataframe
stats = pd.concat([temperature,snowiness], axis=1)
print stats
stats.plot(kind='bar')

"""
这2个维度的幅度是不一样的，所以要分开画哦。
"""
stats.plot(kind='bar', subplots=True, figsize=(15,10))

































