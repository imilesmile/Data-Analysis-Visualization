#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:34:09 2017

@author: miao
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Make the graphs a bit prettier, and bigger
pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

#requests = pd.read_csv('./data/311-service-requests.csv')

"""
6.1 怎么找到脏数据？
其实也没有特别好的办法，还是得先拿点数据出来看看。比如说我们这里观察到邮政编码可能有问题的字段。
需要提到的一点是 .unique() 函数有很巧的用处，我们把所有出现过的邮政编码列出来（之后再看看分布？），也许会有一些想法。
下面我们就把unique()用起来，然后你会发现，确确实实是存在一些问题的，比如：
    为什么大部分被解析出数值，而有些被解析出字符串了？
    好多缺省值（nan）
    格式不一样，有些是29616-0759，有些是83
    有一些pandas不认的，比如'N/A'或者'NO CLUE'
那我们能做什么呢？
    规整'N/A'和'NO CLUE'到缺省值的“队列”里
    看看83是什么鬼，然后再决定怎么处理
    统一一下，全处理成字符串好啦
"""
#print requests['Incident Zip'].unique()


"""
6.3 处理缺省值和字符串/浮点混乱
我们可以在pd.read_csv读数据的时候，传一个na_values给它，
清理掉一部分的脏数据，我们还可以指明说，我们就要保证邮政编码是字符串型的，
不要给我整些数值型出来！！
"""
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('./data/311-service-requests.csv', na_values=na_values, dtype = {'Incident Zip': str})
#print requests['Incident Zip'].unique()


"""
6.4 那些用“-”连接的邮编是什么鬼？
"""
row_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
#print len(requests[row_with_dashes])

"""
真心是很烦人啊，其实只有5个，输出来看看是什么
"""
#print requests[row_with_dashes]

"""
本来就5个，打算直接把这些都设置成缺省值(nan)的：requests['Incident Zip'][rows_with_dashes] = np.nan 
后来查了查，发现可能前5位置是真实的邮编，所以干脆截取一下好了。
"""
long_zip_codes = requests['Incident Zip'].str.len()>5
#print requests['Incident Zip'][long_zip_codes].unique()

requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)

"""
妈蛋查了下00000，发现根本不是什么美国加拿大的邮编，所以这个是不能这么处理的，还真得重新设为缺省值。
"""
#requests[requests['Incident Zip'] == '00000']

#zero_zips = requests['Incident Zip'] == '00000'
#requests.loc[zero_zips, 'Incident Zip'] = np.nan

#unique_zips = requests['Incident Zip'].unique()
#unique_zips.sort()
#print unique_zips

"""
看起来干净多了。
但是真的做完了吗？
"""
zips = requests['Incident Zip']
# 用is_close表示0或者1开始的比较正确的邮编
is_close = zips.str.startswith('0') | zips.str.startswith('1')
# 非缺省值但不以0或者1开始的邮编认为是有些困惑的
is_far = ~(is_close) & zips.notnull()

#print zips[is_far]

#print requests[is_far][['Incident Zip', 'Descriptor', 'City']].sort('Incident Zip')

"""
可以这样去处理和补齐数据。
但你实际上会发现，好像其实用city直接对应一下就可以补上一些东西啊。
"""
print requests['City'].str.upper().value_counts()
































