#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
numpy practice

Created on Mon Jul 10 12:20:49 2017

@author: miao

"""

import bin.numpy as np

a = np.array([1, 2, 3])  # 一维Numpy数组
print type(a)            # Prints "<type 'numpy.ndarray'>"
print a.shape            # Prints "(3,)"
print a[0], a[1], a[2]   # Prints "1 2 3"
a[0] = 5                 # 重赋值
print a                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])   # 二维Numpy数组
print b.shape                     # Prints "(2, 3)"
print b[0, 0], b[0, 1], b[1, 0]   # Prints "1 2 4"

"""
生成一些特殊的Numpy数组(矩阵)时，我们有特定的函数可以调用：
"""
a = np.zeros((2,2))  # 全0的2*2 Numpy数组
print a              # Prints "[[ 0.  0.]
                     #          [ 0.  0.]]"

b = np.ones((1,2))   # 全1 Numpy数组
print b              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7) # 固定值Numpy数组
print c               # Prints "[[ 7.  7.]
                      #          [ 7.  7.]]"

d = np.eye(2)        # 2*2 对角Numpy数组
print d              # Prints "[[ 1.  0.]
                     #          [ 0.  1.]]"

e = np.random.random((2,2)) # 2*2 的随机Numpy数组
print e                     # 随机输出

"""
Numpy数组索引与取值

可以通过像list一样的分片/slicing操作取出需要的数值部分。
"""
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

row_r1 = a[1, :]    # a 的第二行  
row_r2 = a[1:2, :]  # 同上
print row_r1, row_r1.shape  # Prints "[5 6 7 8] (4,)"
print row_r2, row_r2.shape  # Prints "[[5 6 7 8]] (1, 4)"

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print col_r1, col_r1.shape  # Prints "[ 2  6 10] (3,)"
print col_r2, col_r2.shape  # Prints "[[ 2]
                            #          [ 6]
                            #          [10]] (3, 1)"

a = np.array([[1,2], [3, 4], [5, 6]])

# 取出(0,0) (1,1) (2,0)三个位置的值
print a[[0, 1, 2], [0, 1, 0]]  # Prints "[1 4 5]"

# 和上面一样
print np.array([a[0, 0], a[1, 1], a[2, 0]])  # Prints "[1 4 5]"

# 取出(0,1) (0,1) 两个位置的值
print a[[0, 0], [1, 1]]  # Prints "[2 2]"

# 同上
print np.array([a[0, 1], a[0, 1]])  # Prints "[2 2]"

"""
我们还可以通过条件得到bool型的Numpy数组结果，再通过这个数组取出符合条件的值

"""
a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)  # 判定a大于2的结果矩阵

print bool_idx      # Prints "[[False False]
                    #          [ True  True]
                    #          [ True  True]]"

# 再通过bool_idx取出我们要的值
print a[bool_idx]  # Prints "[3 4 5 6]"

# 放在一起我们可以这么写
print a[a > 2]     # Prints "[3 4 5 6]"

"""
Numpy数组的类型
"""
x = np.array([1, 2])  
print x.dtype         # Prints "int64"

x = np.array([1.0, 2.0]) 
print x.dtype             # Prints "float64"

x = np.array([1, 2], dtype=np.int64)  # 强制使用某个type
print x.dtype                         # Prints "int64"

"""
Numpy数组的运算
"""
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# [[ 6.0  8.0]
#  [10.0 12.0]]
print x + y
print np.add(x, y)

# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print x - y
print np.subtract(x, y)

# 元素对元素，点对点的乘积
# [[ 5.0 12.0]
#  [21.0 32.0]]
print x * y
print np.multiply(x, y)

# 元素对元素，点对点的除法
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print x / y
print np.divide(x, y)

# 开方
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print np.sqrt(x)

"""
矩阵的内积
"""
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# 向量内积，得到 219
print v.dot(w)
print np.dot(v, w)

# 矩阵乘法，得到 [29 67]
print x.dot(v)
print np.dot(x, v)

# 矩阵乘法
# [[19 22]
#  [43 50]]
print x.dot(y)
print np.dot(x, y)

"""
特别特别有用的一个操作是，sum/求和(对某个维度)
"""
x = np.array([[1,2],[3,4]])

print np.sum(x)  # 整个矩阵的和，得到 "10"
print np.sum(x, axis=0)  # 每一列的和 得到 "[4 6]"
print np.sum(x, axis=1)  # 每一行的和 得到 "[3 7]"

"""
矩阵的转置，在Numpy数组里用.T实现
"""
x = np.array([[1,2], [3,4]])
print x    # Prints "[[1 2]
           #          [3 4]]"
print x.T  # Prints "[[1 3]
           #          [2 4]]"

# 1*n的Numpy数组，用.T之后其实啥也没做:
v = np.array([1,2,3])
print v    # Prints "[1 2 3]"
print v.T  # Prints "[1 2 3]"

"""
Broadcasting

Numpy还有一个非常牛逼的机制，你想想，如果你现在有一大一小俩矩阵，
你想使用小矩阵在大矩阵上做多次操作。
举个例子，假如你想将一个1n的矩阵，加到mn的矩阵的每一行上：

"""
#你如果要用for循环实现是酱紫的(下面用y的原因是，你不想改变原来的x)

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # 设置一个和x一样维度的Numpy数组y

# 逐行相加
for i in range(4):
    y[i, :] = x[i, :] + v

# 恩，y就是你想要的了
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print y

#上一种方法如果for的次数非常多，会很慢，于是我们改进了一下

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))  # 变形，重复然后叠起来
print vv                 # Prints "[[1 0 1]
                         #          [1 0 1]
                         #          [1 0 1]
                         #          [1 0 1]]"
y = x + vv  # 相加
print y  # Prints "[[ 2  2  4
         #          [ 5  5  7]
         #          [ 8  8 10]
         #          [11 11 13]]"

#其实因为Numpy的Broadcasting，你可以直接酱紫操作

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # 直接加！！！
print y  # Prints "[[ 2  2  4]
         #          [ 5  5  7]
         #          [ 8  8 10]
         #          [11 11 13]]"

#更多Broadcasting的例子请看下面：
v = np.array([1,2,3])  # v has shape (3,)
w = np.array([4,5])    # w has shape (2,)
# 首先把v变成一个列向量
# v现在的形状是(3, 1);
# 作用在w上得到的结果形状是(3, 2)，如下
# [[ 4  5]
#  [ 8 10]
#  [12 15]]
print np.reshape(v, (3, 1)) * w

# 逐行相加
x = np.array([[1,2,3], [4,5,6]])
# 得到如下结果:
# [[2 4 6]
#  [5 7 9]]
print x + v

# 先逐行相加再转置，得到以下结果:
# [[ 5  6  7]
#  [ 9 10 11]]
print (x.T + w).T
# 恩，也可以这么做
print x + np.reshape(w, (2, 1))




































