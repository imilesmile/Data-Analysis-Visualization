#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:09:45 2017

@author: miao
"""
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_style('darkgrid')

"""
Seaborn与可视化
Seaborn是斯坦福大学出的一个非常好用的可视化包，这一节我们一起来看看这个包和相关的一些用法。
"""
names = [
       'mpg'
    ,  'cylinders'
    ,  'displacement'
    ,  'horsepower'
    ,  'weight'
    ,  'acceleration'
    ,  'model_year'
    ,  'origin'
    ,  'car_name'
]
df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data", sep='\s+', names=names)
df['maker'] = df.car_name.map(lambda x: x.split()[0])
df.origin = df.origin.map({1: 'America', 2: 'Europe', 3: 'Asia'})
df=df.applymap(lambda x: np.nan if x == '?' else x).dropna()
df['horsepower'] = df.horsepower.astype(float)
print df.head()

"""
8.1 一般绘图：factorplot 和 FacetGrid
8.1.1 根据2个维度变量绘图
"""
# 画出model_year和mpg的关系图
sns.factorplot(data=df, x="model_year", y="mpg")

"""
8.1.2 可以按照第3个维度绘制不同的关系图
"""
sns.factorplot(data=df, x="model_year", y="mpg", col="origin")

"""
8.1.3 可以从折线图切成柱状图
"""
sns.factorplot("cylinders", data=df, col="origin", kind='bar')
g = sns.FacetGrid(df, col="origin")
g.map(sns.distplot, "mpg")


"""
8.1.4 散点图
"""
g = sns.FacetGrid(df, col="origin")
g.map(plt.scatter, "horsepower", "mpg")

"""
8.1.5 绘图的同时还做回归
"""
g = sns.FacetGrid(df, col="origin")
g.map(sns.regplot, "horsepower", "mpg")
plt.xlim(0, 250)
plt.ylim(0, 60)

"""
8.1.6 kde等高线图
"""
df['tons'] = (df.weight/2000).astype(int)
g = sns.FacetGrid(df, col="origin", row="tons")
g.map(sns.kdeplot, "horsepower", "mpg")
plt.xlim(0, 250)
plt.ylim(0, 60)

"""
8.1.7 按照2个维度展开画图
"""
g = sns.FacetGrid(df, col="origin", row="tons")
g.map(plt.hist, "mpg", bins=np.linspace(0, 50, 11))

"""
8.2 pairplot and PairGrid
8.2.1 多个维度两两组合绘图¶
"""
g = sns.pairplot(df[["mpg", "horsepower", "weight", "origin"]], hue="origin", diag_kind="hist")
for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45)

"""
8.2.2 组合绘图的时候顺便回归一下
"""
g = sns.PairGrid(df[["mpg", "horsepower", "weight", "origin"]], hue="origin")
g.map_upper(sns.regplot)
g.map_lower(sns.residplot)
g.map_diag(plt.hist)
for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45)
g.add_legend()
g.set(alpha=0.5)

"""
8.3 jointplot and JointGrid
8.3.1 联合绘图(kde等高)
"""
sns.jointplot("mpg", "horsepower", data=df, kind='kde')

"""
8.3.2 联合绘图(加回归)
"""
sns.jointplot("horsepower", "mpg", data=df, kind="reg")

g = sns.JointGrid(x="horsepower", y="mpg", data=df)
g.plot_joint(sns.regplot, order=2)
g.plot_marginals(sns.distplot)























































