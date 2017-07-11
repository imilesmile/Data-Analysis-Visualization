#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:55:37 2017

@author: miao
"""
# The usual preamble
#%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

# Make the graphs a bit prettier, and bigger
pd.set_option('display.mpl_style', 'default')

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)

"""
上次的数据集有点小啦，咱们这里用一个大一点的数据集
"""
complaints = pd.read_csv('./data/311-service-requests.csv')

"""
2.1 瞄一眼数据
dataframe这种格式还是很神奇的，
比如说，你要是直接把dataframe丢出去输出一下，它会告诉你最基本的信息。
比如有多少行多少列，有多少非空的值等等。
"""
print complaints.info()

"""
2.2 选行或者列
上一节提到了，直接用名字就可以取。
"""
print complaints['Complaint Type']
print complaints[:5]

"""
合并一下，取出某一列的前5行
另外你先取列再切片 和 先切片再取列，其实是一样一样的。
"""
print complaints['Complaint Type'][:5]
print complaints[:5]['Complaint Type']


"""
2.3 选多行
选一行是把这一行的名字告诉它，那选多行呢？恩，传一个名称list给他咯
"""
print complaints[['Complaint Type', 'Borough']]


"""
再拼一下：多列的前n行。
"""
print complaints[['Complaint Type', 'Borough']][:10]

"""
2.4 想统计找出Top类型的数据？
dataframe真的很智能，比如你告诉它，我要统计一下数量了！
（用.value_counts()函数），那它就帮你统计数量了
"""
print complaints['Complaint Type'].value_counts()

"""
咱们拿到的结果是排过序的，也就是说如果我只要top 10的话，其实截断一下就可以了：
"""
complaints_count = complaints['Complaint Type'].value_counts()
print complaints_count[:10]

"""
咱们可以把top10画出来。
"""
complaints_count[:10].plot(kind='bar')

"""
如果我们想挑选出来"Complaint Type"字段为某一类
（比如"Noise - Street/Sidewalk"）的数据，怎么选呢？
我们先看怎么选，一会儿解释下。
"""
noise_complaints = complaints[complaints['Complaint Type'] =="Noise - Street/Sidewalk"]
print noise_complaints[:3]


"""
你看看上面我们选出来的数据的 noise_complaints字段，发现我们确实按条件筛出来了想要的数据，背后的原理是什么呢？
我们先看看，中括号内的部分，会生成一个True或者False的布尔型dataframe
"""
print complaints['Complaint Type'] == "Noise - Street/Sidewalk"

"""
既然看到布尔型的数值出来了，大家一定会想到逻辑运算（与或非...），是的，如果你现在需要多个条件判定呢？
恩，比如你的条件是'Complaint Type'字段为"Noise - Street/Sidewalk"，且'Borough'字段为"BROOKLYN"：
"""
is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
in_brooklyn = complaints['Borough'] == "BROOKLYN"
print complaints[is_noise & in_brooklyn][:5]

"""
我们也可以只看选出来的数据里面的一些列：
"""
print complaints[is_noise & in_brooklyn][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']][:10]


"""
3.2 从numpy到pandas
说起来，pandas数据的每一列其实是pd.Series类型的
"""
print pd.Series([1,2,3])


"""
pandas Series底层是numpy数组，如果你在 Series后面加上 .values ，你得到的就是一个实实在在的numpy数组
"""
import numpy as np
print np.array([1,2,3])
print pd.Series([1,2,3]).values

"""
所以呢，其实刚才的布尔判定，和numpy有密不可分的关系（当然，你自己用pandas的时候，可以不管底层是什么实现的）
"""
arr = np.array([1,2,3])
print arr!=2
print arr[arr!=2]

"""
所以，咱们汇总一下，分析点数据出来？
"""
noise_complaints = complaints[is_noise]
print noise_complaints['Borough'].value_counts()

"""
发现曼哈顿好像最吵。绝对大小的数值当然也是有说服力的，咱们还是习惯转换成比例的形式，比如下面这样：
"""
noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()

print noise_complaint_counts/complaint_counts

"""
上一步操作你得到的结果其实都会是0，为啥？python默认的整型和整型除法得到的结果还是整型，所以我们最好把 complaint_counts 字段类型转换一下，转成float型的。
"""
print noise_complaint_counts/complaint_counts.astype(float)

(noise_complaint_counts / complaint_counts.astype(float)).plot(kind='bar')













