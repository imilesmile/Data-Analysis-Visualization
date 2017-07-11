#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:46:02 2017

@author: miao
"""
# Render our plots inline
"""
%matplotlib inline是jupyter notebook里的命令, 
意思是将那些用matplotlib绘制的图显示在页面里而不是弹出一个窗口
"""

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)


"""
1.1 读取csv格式文件
用read_csv函数可以读取csv数据，默认数据之间是用逗号分隔开的。
有时候数据集并不是这样的啊，咱们看看比较完整的读数据参数设定。

"""
broken_df = pd.read_csv('./data/bikes.csv')
broken_df.info()
print broken_df[:3]

"""
一脸懵逼了，读得完全不对~~ read_csv有相应的参数需要我们设定一下，比如对于上面的数据，我们希望：

    数据分隔符设定为;
    编码格式设定为 'latin1' (默认 'utf8')
    解析一下 'Date' 字段
    按照 'Date' 字段(日期)排序

"""
fixed_df = pd.read_csv('./data/bikes.csv', sep=';', encoding='latin1',
                       parse_dates=['Date'],dayfirst=True, index_col = 'Date')
print fixed_df[:3]

"""
1.2 筛选某些列
用pandas读取完CSV文件呢, 我们会得到一个叫做DataFrame的对象，
由行和列组成类似上面的excel(说废话的感觉)。可以像下面这样通过列名取出其中的某一列。
"""
print fixed_df['Berri 1']


"""
1.3 画一下某一列？
直接在这一列尾部加上 .plot() 就可以了，就喜欢这么简单粗暴！！
比如按照时间绘个图，然后发现1，2，3月骑自行车的人最多了。
"""
fixed_df['Berri 1'].plot()

"""
如果想画多列怎么办？ 就像下面这样就可以啦，
你告诉我它，“我需要画整个dataframe的图！！！”
"""
fixed_df.plot(figsize=(15,10))

"""
1.4 一句话串读取和绘图

好吧，其实我的意思就是你可以直接一口气读完数据然后画出来，恩:

"""
df = pd.read_csv('./data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
df['Berri 1'].plot()
























