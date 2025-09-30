import numpy as np
# 1. 从数组np.arange(15)提取 5 到 10 (包括5和10)之间的所有元素
# Z = np.arange(15)
# A = Z[5:11]
# #2.将数组 np.arange(20)转变为 4 行 5 列的二维数组,并执行交换第 1 行和第 2 行，交换第 1 列和第 2 列
# B = np.arange(20).reshape((4,5))
# #print(B)
# #B[[0,1]] = B[[1,0]]
# B[:,[0,1]] = B[:,[1,0]]
# #print(B)
# #3.将数组np.random.randint(1,10,size=(5,5))中所有的奇数替换为 0
# D = np.random.randint(1,10,size=(5,5))
# A = np.where(D%2==1,0,D)
# #print(A)

# #4.从1—50之间的均匀地产生随机数字20个存储数组d中，替换大于等于30数为0并获取给定数组d中前5个最大值的位置(即5个数)。
# A = np.random.randint(1,50,size=20)
# #print(A)
# B = np.where(A>30,0,A)
# M = np.sort(A)
# #print(M)
#N = M[::-1]
#print(N)
#K = N[:5]
#print(K)

# # 5.使用numpy数组计算由5个坐标:(1,9)、(5,12)、(8,20)、(4,10)、(2,8) 构成的图形的周长
# A = np.array([[1,9],
#               [5,12],
#               [8,20],
#               [4,10],
#               [2,8]])
# #print(A)
# B = np.sort(A,axis=0)
# print(B)
# gra1 = np.vstack((B[1:, :], B[0, :]))
# print(gra1)
# dis = np.sqrt(np.sum(np.square(B - gra1), axis=1))
# print(dis)
# print(np.sum(np.sum(dis)))

import pandas as pd
# A = pd.Series([2,3,4,5677,7])
# # B = pd.Index(A)
# # print(A)
# # print(B)
# B = pd.Series([3,4,56,7],['a','b','d','f'])
# print(B)

# s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
# s2 = pd.Series(np.arange(1,5),index=['a','b','c','d'])
# print(s1)
# print(s2)

# dict = {'name':'凡间','age':10,'class':'三班'}
# s3 = pd.Series(dict,index=['name','class','age','sex'])
# print(s3)
# C = s3.isnull()
# print(C)
# D = s3.notnull()
# print(D)
# N = s3[['name','age']]
# print(N)

# arr = np.array(['3.5','4.5','6.7'])
# A = arr.astype(float)
# print(A)

# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)

# add = np.arange(10)
# add[5:8:2]=12
# print(add)

# names = np.array(['Bob','Joe','wil','Bob','wil'])
# data = np.arange(1,6).reshape((5,1))*10+np.arange(1,5)
# A = data[~(names == 'Bob')]  #'~'反过来的意思
# print(data)
# print(A)
# arr = np.empty((5,4))
# for i in range(5):
#     arr[i] = i
# print(arr)
# print('\n')    
# A = arr[[3,4,0,1,2]]
# print(A)

# arr = np.arange(1,4).reshape((3,1))*10+np.arange(1,5)
# print(arr)
# print('\n')
# A = arr[[1,2,2],[0,1,2]]
# print(A)

