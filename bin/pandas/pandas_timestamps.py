#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:01:07 2017

@author: miao
"""

import pandas as pd
"""
7.1 Unix时间戳怎么搞？
"""
# Read it, and remove the last row
popcon = pd.read_csv('./data/popularity-contest', sep=' ', )[:-1]
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']

#print popcon[:5]

"""
开始的时候我们需要转成int型
"""
popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)

"""
然后可以用 pd.to_datetime 函数去把整型按照时间戳转成具体的日期和时间
"""
popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')

#print popcon['atime'].dtype

"""
你再看看 atime 和 ctime 字段，就变成标准时间啦！
"""

#print popcon[:5]

"""
6.2 根据时间筛选数据

另外一个操作是，我们需要按照时间去筛选数据，这个也很简单，你只需要告诉pandas，我需要大于/小于某个日期的数据！！

"""
popcon = popcon[popcon['atime'] > '1970-01-01']

"""
~ 取反操作
"""
nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]

print nonlibraries.sort('ctime', ascending=False)[:10]




















