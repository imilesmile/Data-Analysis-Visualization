#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:20:44 2017

@author: miao
"""
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

"""
这一部分我们做点时间维度相关的分析，比如看看到底这个城市的人周末骑自行车出行多，
还是工作日多也就是咱们看看大家都是骑车出去玩，还是去工作。
4.1 区分工作日和周末
加载数据
"""
bikes = pd.read_csv('./data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
bikes['Berri 1'].plot()

"""
咱们先随便选一列出来吧，比如选'Berri 1'单独成一个berri_bikes的dataframe
"""
berri_bikes = bikes[['Berri 1']].copy()
print berri_bikes[:5]

"""
然后为了区分工作日和周末，我们加一列'weekday'。
对了，这里要提到一个概念，叫做index，也就是大家在数据库里面熟知的索引，
在dataframe里面也有，比如我们刚才的数据，index就是日期。
"""
print berri_bikes.index

"""
如果仔细观察，你会发现里面有些天的数据丢失了。（牛逼的数据分析师真的一眼能看出来，咳咳，反正我也没一眼看出来）
我们通过.day可以直接看到是一个月的第几天。
"""
print berri_bikes.index.day

"""
其实dataframe对于日期类型的数据，可以直接知道是星期几！！！
"""
print berri_bikes.index.weekday

"""
其中0是星期一，1是星期二，以此类推。所以我们可以直接生成一列，指明是星期几啦。
"""
berri_bikes.loc[:, 'weekday'] = berri_bikes.index.weekday
print berri_bikes[:5]

"""
4.2 分组+排序+聚合统计
用过SQL里面的groupby吗，恰巧pandas的dataframe也有一个.groupby()函数，而且好用得一塌糊涂。
比如呢，下面这句 berri_bikes.groupby('weekday').aggregate(sum) 的意思就是说，
“把数据按照星期几分一下组，然后给我加和一下，结果！！！”

"""
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
print weekday_counts


"""
0, 1, 2, 3, 4, 5, 6，像我这种智商欠费的同学，根本对应不上星期几，所以取个名字好了，然后加上去
"""
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print weekday_counts
weekday_counts.plot(kind='bar')

"""
4.3 把刚才学的放一块儿
把刚才学到的东西串一块儿，能看到很神奇pandas处理结果啦。
你可以试试把sum 换做 max或者numpy.median，求最大和平均，也可以试试更多的函数！！
"""















