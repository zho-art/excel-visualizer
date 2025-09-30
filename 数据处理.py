import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# A = pd.Series([1, pd.NA, 3.5, pd.NA, 7])
# print(A)
# B = A.dropna()
# print(B)

# data = pd.DataFrame([[pd.NA, 6.5, 3.], [pd.NA, pd.NA, pd.NA],[pd.NA, pd.NA, pd.NA], [pd.NA, 6.5, 3.]])
# print(data)
# B = data.dropna(thresh=2)
# print(B)
# A = data.dropna(axis=1, how='all')
# print(A)

# data[0] = pd.NA
# data.dropna(axis=1, how='all')
# print(data)
# B = data.dropna()  #有nan的一行全部删掉
# print(B)

# data = pd.Series([1,2,pd.NA,34,0,pd.NA])
# A = data.fillna(999)
# print(A)

# data = pd.DataFrame([[pd.NA, 6.5, 3.], [pd.NA, pd.NA, pd.NA],[pd.NA, pd.NA, pd.NA], [pd.NA, 6.5, 3.]])
# # print(data)
# # data[[2,1]] = 0
# # print(data)
# data.iloc[2,1]=0
# print(data)

# data = pd.DataFrame(np.random.randn(7,3))
# data.iloc[:3,2] = pd.NA
# print(data)
# A = data.fillna(method='ffill') 
# print(A)
# data = ['foor','got','gut']
# df = { }
# for i,volue in enumerate(data):
#     df[i] = volue
# print(df)    
# pitchers = [('Nolan', 'Ryan'),('Roger', 'Clemens'),('Schilling', 'Curt')]
# it , im = zip(*pitchers)
# print(it)
# words = ['apple', 'bat', 'bar', 'atom', 'book']
# df ={}
# for lender in words:
#     lent = lender[0]
#     if lent not in df:
#         df[lent] = [lender]
#     else:
#         df[lent].append(lender)
# print(df)            

# maping = {}
# for key,value in zip(range(5),reversed(range(5))):
#     maping[key] = value
# print(maping)    
# maping = dict(zip(range(5),reversed(range(5))))
# print(maping)
# #集合推导式
# strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
# loc = {key:index
#        for index,key in enumerate(strings)}
# print(loc)
# a=np.linspace(1,10,4)
# b=np.linspace(1,10,4,endpoint=False)
# A = np.concatenate([a,b])
# print(A)
# A = np.zeros((3,5))
# print(A)
# a = np.full((3,4),10.1)
# B = np.full_like(a,21.11)
# print(a)
# print(B)
# a=np.arange(1,4).reshape((3,1))*10+np.arange(1,5)
# print(a)
# b=np.arange(1,4).reshape((3,1))*10+np.arange(1,6)
# print(b)
# arr3d = np.array([[[1, 2, 3], [4, 5, 6]], 
# [[7, 8, 9], [10, 11, 12]]])
# A = arr3d[1, :, 1]
# print(A)
# data = np.arange(1,4).reshape((3,1))*10+np.arange(1,4)
# print(data)
# data[data % 10 < 2] = 0
# print(data)
# names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will'])
# data = np.arange(1,6).reshape((5,1))*10+np.arange(1,5)
# data[names == 'Joe'] = 7.5
# print(data)
# data = np.arange(1,4).reshape((3,1))*10+np.arange(1,5)
# print(data)
# print()
# A = data[[1, 2, 0, 2]][:, [0, 3, 1, 2]]
# print(A)
# A =np.arange(1)
# print(A)
# a = np.array([[1,2],[3,4]])
# b = np.array([[11,12],[13,14]])
# values, vectors = np.linalg.eig(a)
# print(values)

# data = pd.Series(np.random.randint(3,10,5),index=['a','b','c','d','e'])
# print(data)
# dict = {'name':'范建','age':18,'class':'三班'}
# s3 = pd.Series(dict,index=['name','class','age','sex'])
# dta = ['class','name','age','ser']
# s4 = pd.Series(dict,index=dta)
# print(s4)
# data = pd.Series(np.arange(3,7),index=['a','b','c','d'])
# A = 'a' in data
# print(A)
# dict = {'name':'范建','age':18,'class':'三班'}
# s3 = pd.Series(dict,index=['name','class','age','sex'])
# A = s3['name':'age']
# print(A)

# data = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
# # print(data)
# # dr = data.reindex(['a','c','b'],columns=['A','C','B'])
# # print(dr)
# data.loc['d'] = [1,1,1]
# A = data.drop(['a','d'])
# print(A)

df1 = pd.DataFrame(np.arange(12).reshape(4,3),index = ['a','b','c','d'], columns=list('ABC'))
# df2 = pd.DataFrame(np.arange(9).reshape(3,3),index = ['a','d','f'], columns= list('ABD'))
# print(df1)
# print(df2)
# A = df1 + df2
# print(A)
#A = 1/ df1
# A = df1.rdiv(1)
# print(A)

# df = pd.DataFrame(np.random.randn(9).reshape(3,3),index=['a','b','c'],columns=list('ABC'))
# A = df.applymap(lambda x:'%.2f' % x**2)
# print(A)
# a=pd.DataFrame(np.random.randint(0,100,(3,5)),index=(1,2,3),columns=("A","B","C","D","E"))
# print(a)
# a.iloc[:2]=[1,1,1,1,1]
# print(a)
# a.loc[:2]=[2,3,4,5,6]
# print(a)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager
from matplotlib import font_manager
#font = font_manager.FontPropertise(fname=r"C:\Windows\Fonts\ALGER.TTF",size = 20)
# plt.xlabel('tianshu',fontproperties=font)
# values = np.linspace(0,20)
# plt.style.use("seaborn")
# fig, axes = plt.subplots(2,2,sharex=False)
# ax1 = axes[0,0]
# ax1.plot(values)
# ax2 = axes[0,1]
# ax2.plot(np.sin(values),c='y')
# ax3 = axes[1,0]
# ax3.plot(np.cos(values),c='b')
# ax4 = axes[1,1]
# ax4.plot(np.tan(values),c='g')
# plt.show()
# data = pd.DataFrame([[1., 6.5, 3.], [1., pd.NA, pd.NA],[pd.NA, pd.NA, pd.NA], [pd.NA, 6.5, 3.]])
# data[0] = pd.NA
# data[3] = pd.NA
# print(data)
# A = data.dropna(thresh=2)
# print(A)

# df = pd.DataFrame(np.random.randn(7,3))
# df.iloc[:4,1] = pd.NA
# df.iloc[:2,2] = pd.NA
# print(df)
# print()
# A = df.fillna({1:0.5,2:1})
# print(A)
# data = pd.DataFrame(np.random.randn(1000, 4))
# col = data[2]
# A = col[np.abs(col) > 3]
# print(A)
# data = pd.Series([1,2,-999,7,-999,-999,-999])
# A = data.replace([-999,-1000],[0,np.nan])
# print(data)
# print(A)

# data = pd.DataFrame(np.arange(12).reshape((3, 4)),index=['Wuhan', 'Beijing', 'Guangzhou'],columns=['one', 'two', 'three', 'four'])
# print(data)
# transform = lambda x: x[:4].upper()
# data.index = data.index.map(transform)
# print(data)
# ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# bins = [18, 25, 35, 60, 100]
# group_names = ['Youth','YoungAdult','MiddleAged','Senior']
# A = pd.cut(ages, bins, labels=group_names)
# print(A)

# df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
# print(df)
# print()
# A = df.sample(n=2)
# print(A)
# val ='ab, guido'
# A = val.find(',')
# print(A)
import re
# A = re.match('a','abcade').group()
# print(A)
# pattern = re.compile(r'\d+') # 查找数字
# C = 'run88oob123google456'[:10]
# A = pattern.findall(C)
# print(A)


# words = ['apple', 'bat', 'bar', 'atom', 'book']
# df ={}
# for lender in words:
#     lent = lender[0]
#     if lent not in df:
#         df[lent] = [lender]
#     else:
#         df[lent].append(lender)
# print(df)            
