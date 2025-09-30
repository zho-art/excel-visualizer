# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

#折线
# y1 = [np.random.randint(0,10) for x in range(20)]
# x1 = range(5,25)
# plt.plot(x1,y1)
# plt.show()
# y = [np.random.randint(0,10) for x in range(10)]
# plt.plot(y,lw=4,c='r',ls='--')
# plt.show()

# y1 = [x for x in range(10)]
# y2 = [np.random.randint(0,10)for x in range(10)]
# lines = plt.plot(range(10),y1,range(10),y1,range(10),y2)
# line = lines[0]
# line.set_color('r')
# line.set_linewidth(8)
# line.set_alpha(1)
# line.set_drawstyle('steps-post')
# plt.show()
# lines = plt.plot(range(10),y1,range(10),y2)
# plt.setp(lines,linewidth=4)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from matplotlib import font_manager
# y1 = [np.random.randint(10) for x in range(10)]
# font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\msyhl.ttc",size=20)
# plt.plot(y1)
# plt.title('折线图',fontproperties=font)
# plt.xlabel('竖线',fontproperties=font)
# plt.xlim((0,10))
# plt.show()
#英雄联盟
# avenger = [17974.4,50918.4,30033.0,40329.1,52330.2, 
# 19833.3,11902.0,24322.6,47521.8,32262.0,22841.9,12938.7,
# 4835.1,3118.1,2570.9,2267.9,1902.8,2548.9,5046.6,3600.8]
# plt.figure(figsize=(15,5))
# plt.plot(avenger,marker='o')
# font = font_manager.FontProperties(fname=r'C:\\Windows\\Fonts\\msyhl.ttc',size=10)
# plt.title('英雄联盟',fontproperties=font)
# plt.xlabel('时间',fontproperties=font)
# plt.xticks(range(20),["第%d天"%x for x in range(1,21)],fontproperties=font)
# plt.grid(True)
# plt.legend(['人名'],loc='best')
# for index,value in enumerate(avenger):
#     plt.annotate("(%d,%.2f)"%(index,value),xy=(index,value),xytext=(index-0.1,value-0.1))
# plt.show()
# import pandas as pd  
# import matplotlib.pyplot as plt  
# from matplotlib import font_manager
# 读取数据  
# a = pd.read_excel('C:\\Users\\周顺\\Desktop\\天气统计.xlsx', sheet_name='Sheet2')
# # 设置字体  
# font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\msyhl.ttc", size=20)  
# # 提取数据  font
# b = a.iloc[:, 1]  # 最高温  
# c = a.iloc[:, 2]  # 最低温  
# # 绘图  
# plt.figure(figsize=(15, 5))  
# plt.plot(range(1, 13), b, label='最高温', marker='o')  
# plt.plot(range(1, 13), c, label='最低温', marker='x')  
# # 设置标签和标题  
# plt.xticks(range(1, 13), ['%d月' % x for x in range(1, 13)], fontproperties=font)  
# plt.xlabel('月份', fontproperties=font)  
# plt.ylabel('气温', fontproperties=font)  
# plt.title('天气', fontproperties=font)  
# plt.grid(True)  
# plt.legend(loc='best')
# # 添加注解  
# for index, value in enumerate(b, start=1):  
#     plt.annotate("%.1f°" % (value), xy=(index, value), xytext=(index - 0.3, value - 0.3), textcoords='offset points', fontproperties=font)  
# for index, value in enumerate(c, start=1):  
#     plt.annotate("%.1f°" % (value), xy=(index, value), xytext=(index + 0.3, value - 0.3), textcoords='offset points', fontproperties=font)  
# plt.show()

# movies = {"流浪地球":40.78, "飞驰人生":15.77, "疯狂的外星人":20.83, "新喜剧之王":6.10, "廉政风云":1.10, "神探蒲松龄":1.49, "小猪佩奇过大年":1.22, "熊出没·原始时代":6.71}
# plt.figure(figsize=(15, 5))
# A = pd.DataFrame(data={"names":list(movies.keys()),
#                        "tickets":list(movies.values())})
# B = A.iloc[:,0]
# C = A.iloc[:,1]
# # plt.bar(B,fontproperties=font)
# # plt.bar(C)
# plt.bar(movies.keys(),movies.values())
# plt.xticks(range(12),['%dyue'%x for x in range(13)],fontproperties=font)
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from matplotlib import font_manager
# movies = {"流浪地球":[2.01,4.59,7.99,11.83,16],
#           "飞驰人生":[3.19,5.08,6.73,8.10,9.35],
#           "疯狂的外星人":[4.07,6.92,9.30,11.29,13.03],
#           "新喜剧之王":[2.72,3.79,4.45,4.83,5.11],
#           "廉政风云":[0.56,0.74,0.83,0.88,0.92],
#           "神探蒲松龄":[0.66,0.95,1.10,1.17,1.23],
#           "小猪佩奇过大年":[0.58,0.81,0.94,1.01,1.07],
#           "熊出没·原始时代":[1.13,1.96,2.73,3.42,4.05]}
# movie_df = pd.DataFrame(movies)
# font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\msyhl.ttc", size=20)
# plt.figure(figsize=(20,5))
# xticks = np.arange(0,len(movies)*1.5,1.5)
# bar_width = 0.2
# for index in movie_df.index:
#     plt.bar(xticks+(-2+index)*bar_width,movie_df.iloc[index],width=bar_width, label='第%d天票房'%(index+1))
# plt.xticks(xticks, movie_df.columns)
# print(movie_df.iloc[index])
# font.set_size(12)
# plt.legend(prop=font)
# plt.grid()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from matplotlib import font_manager
# font = font_manager.FontProperties(fname=r'C:\\Windows\\Fonts\\msyhl.ttc',size = 20)
# plt.figure(figsize=(15,10))
# menMeans = (20, 35, 30, 35, 27)
# womenMeans = (25, 32, 34, 20, 25)
# groupNames = ('G1','G2','G3','G4','G5')
# plt.bar(groupNames,menMeans,label="男性得分")
# plt.bar(groupNames,womenMeans,bottom=menMeans,label='女性得分')
# plt.legend(prop=font)
# plt.show()

#直方图
# durations = [131, 98, 125, 131,133,155,166,177,148,154,132,133]
# plt.figure(figsize=(9,5))
# nums,bins,patches= plt.hist(durations,12,edgecolor='k',density=True)
# plt.xticks(bins,bins)
# plt.show()

# import matplotlib.pyplot as plt  
# import numpy as np
# import seaborn as sns
# durations = [131, 98, 125, 131,133,155,166,177,148,154,132,133]  
# plt.figure(figsize=(9,5))  
# sns.distplot(durations,12)
# nums,bins,patches= plt.hist(durations,12,edgecolor='k',density=True,alpha=0.7)  
# # 计算位于 bin 中心的值作为刻度标签  
# tick_positions = 0.5 * (bins[:-1] + bins[1:])  
# tick_labels = [f'{int(np.round(val))}' for val in tick_positions]  
# plt.xticks(tick_positions, tick_labels, rotation=45)  
# plt.xlabel('Duration')  
# plt.ylabel('Probability Density')  
# plt.title('Histogram of Durations')  
# plt.grid(axis='y', alpha=0.75)  
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as py
# import pandas as pd

# data = np.random.rand(100)*100
# data = np.append(data,np.array([-120,150]))
# plt.boxplot(data,sym='^',vert=True,widths=[0.1],meanline=True,showmeans=True)
# plt.show()

# X = np.linspace(0,20)
# plt.subplot(2,1,1)
# plt.plot(X,np.sin(X))
# plt.subplot(2,1,2)
# plt.plot(X,np.cos(X))
# plt.subplots_adjust(wspace=0.15,hspace=0)
# plt.show()
# widths = (4,1)
# heights = (1,4)
# fig = plt.figure(figsize=(10,10))
# gs = fig.add_gridspec(2,2,width_ratios=widths,height_ratios=heights)
# plt.show()

# from turtle import *
# from math import sin,cos,e
# def draw():
#     cycle=25
#     t=0
#     while not (t>cycle*360):
#         p=e**cos(t)-2*cos(4*t)+sin(t/12)**5
#         x=a*sin(t)*p
#         y=b*cos(t)*p
#         goto(x,y)
#         dot()
#         t+=1
#         print(t)
# pencolor("red")
# pu()
# speed(0)
# tracer(1000)
# a=b=40
# draw()
# ht()
# done()

# A = 'abcdefg'
# #B = A[3:7] + 'join' + A[0:3]
# B = A[3:] +A[:3]
# for i in B:
#     N = ord(i)
# print(N)

# def shift_and_convert_to_int(letter_string):  
#     # 确保输入字符串长度为7且全为小写字母  
#     if len(letter_string) != 7 or not letter_string.islower():  
#         raise ValueError("输入必须是一个长度为7的小写字母字符串")  
      
#     # 将字符串中的字符左移三位  
#     shifted_string = letter_string[-3:] + letter_string[:-3]  
#     password_integer = int(''.join(str(ord(char) - ord('a') + 1) for char in shifted_string))
#     return password_integer  
# # # 示例使用  
# letter_string = "abcdefg"  # 假设这是王阿姨小纸条上的7个小写字母  
# payment_password = shift_and_convert_to_int(letter_string)  
# print(f"支付密码是: {payment_password}")

# def A(letter_string):
#     c = letter_string[3:]+letter_string[:3]
#     b = 'qwertyuioplkjhgfdsazxcvbnm'
#     n = b.index[c]
#     print(n)
    
# A(letter_string = "abcdefg")    

# def shift_left_circular(s, n):  
# #     # 循环左移n位  
#     return s[-n:] + s[:-n]  
  
# def string_to_ascii_int(s):  
# #     # 将字符串转换为ASCII码组成的字符串，然后转换为整数  
#     ascii_str = ''.join(str(ord(char)) for char in s)  
#     return int(ascii_str)  
  
# # # 王阿姨的密码提示  
# password_hint = "qazxcdf"  
  
# # # 循环左移3位  
# shifted_string = shift_left_circular(password_hint, 3)  
  
# # # 将移位后的字符串转换为整数（ASCII码连接）  
# password_integer = string_to_ascii_int(shifted_string)  
  
# print(shifted_string)  # 输出移位后的字符串，用于验证  
# print(password_integer)  # 输出最终的整数密码


# A = 'abcdefg'
# # #B = A[3:7] + 'join' + A[0:3]
# B = A[3:] +A[:3]
# N = ''.join(str(ord(n)) for n in B)
# print(int(N))

#大小写字母互转
# A = input('请输入一个字母:')
# while A:
#     B = ord(A)
#     print(B)
#     A = input('请输入一个字母:')

# ko = input('请输入一个字母:')
# while ko:
#     if 'A'<=ko and ko <='Z':
#         M = int(ord(ko) + 32)
#         C = chr(M)
#         print(C)
#     else:
#         M = int(ord(ko) -32)
#         C = chr(M) 
#         print(C)
#     ko = input('请输入一个字母:') 
      
# def A(n,k):
#     people = list(range(n))
#     index = 0
#     while len(people)>1:
#         index = (index +k -1) % len(people)
#         people.pop(index)
#     return people[0]
# n = 10
# k = 3
# print('最后留下的是原来的{}号'.format(A(n,k)))

# import numpy as np
# A = np.array([1,2,1,5,6])
# B = np.unique(A)
# print(B)

# import numpy as np 
# A = np.array([1,2,3,4,5,6])
# B = np.percentile(A,50)
# print(B)

# arr = np.random.randn(100)
# B = (arr > -3).all()
# print(B)
# for i in range(100,1000):
#     A = str(i)
#     if int(A[0])**3+int(A[1])**3+int(A[2])**3 == int(A):
#         print(int(A))   

#排序问题
# def A(value,key):
#     for i in range(len(value)):
#         if value[i] == key:
#             return i 
#     return -1
# values = [9,2,1,11,7,6,5,44,33,32,45,70]
# resu = A(values,7)
# if resu == -1:
#     print('查找失败')
# else:
#     print('查找成功，对应下标',resu)
#二分法查找
# def A(value,key,left,right):
#     if left > right:
#         return -1
#     mdff = (left + right)//2
#     if value[mdff] < key:
#         left = mdff +1
#         return A(value,key,left,right)
#     elif value[mdff] > key:
#         right = mdff - 1
#         return A(value,key,left,right)
#     else:
#         return mdff
# values = [0,1,2,3,4,5,6,7,10,15,20,25,26,28,29,39,49,59,69,77,78,99.346,467,789.5468] 
# result = A(values,25,0,len(values)-1)   
# if result ==-1:
#     print('查找失败')
# else:
#     print('查找成功',result)
       
# #冒泡法排序
# def A(array):
#     n = len(array)
#     for i in range(n-1, 0, -1):
#         flag = 1
#         for j in range(0, i):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#                 flag = 0
#         # 注意：移除了 if flag: break 这一行
#     return array  # 将返回语句移到了外层循环之后

# array = [5, 4, 5, 7, 9, 3, 2, 3, 4]
# print("排序前:", array)
# sorted_array = A(array)
# print("排序后:", sorted_array)

#冒泡法
# def A(array):
#     n = len(array)
#     for i in range(n-1,0,-1):
#         for j in range(0,i):
#             if array[j] > array[j+1]:
#                 array[j],array[j+1] = array[j+1],array[j]
#     return array
# array = [1,2,3,2,1,6,7]
# print(A(array))            

# #选择排序
# def A(array):
#     n = len(array)
#     for i in range(0,n):
#         min = i
#         for j in range(i+1,n):
#             if array[j] < array[min]:
#                 min = j
#             array[min],array[i] = array[i],array[min]
#     return array
# array = [3,3,2,4,2,1]
# print(array)
# print(A(array))

#插入排序
# def A(array):
#     n = len(array)
#     for i in range(1,n):
#         if array[i] < array[i-1]:
#             temp = array[i]
#             index = i
#             for j in range(i-1,-1,-1):
#                 if array[j] > temp:
#                     array[j+1] = array[j]
#                     index = j
#                 else:
#                     break
#             array[index] = temp
#     return array
# array = [3,2,1,4,6,7,9,1]
# print(A(array))

#快速排序
# def A(array):
#     return qsort(array,0,len(array)-1)
# def qsort(array,left,right):
#     if left >= right:
#         return array
#     key = array[left]
#     lp = left
#     rp = right
#     while lp < rp:
#         while array[rp] >= key and lp< rp:
#             rp -= 1
#         while array[lp] <= key and lp < rp:
#             lp += 1
#         array[lp],array[rp] = array[rp],array[lp]
#     array[left],array[lp] = array[lp],array[left]
#     qsort(array,left,lp-1)
#     qsort(array,rp+1,right)
#     return array
# array = [5,3,4,5,7,1,8,0]
# print(A(array))         

# A = float(input('请输入数字:'))
# if A>100 and A<1000:
#     B= float(str(A)[::-1])
#     print(B)
# else:
#     print('输入错误')    

# t = int(input(''))
# n = int(input(''))
# A = t/n
# B = 2*n
# print('{:.3f}'.format(A))
# print(B)

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# A = pd.read_csv("C:\\Users\\周顺\\Desktop\\哈.csv",header=None)
# B = np.array(A)
# C = B.flatten()
# df ={}
# for j in C:
#     for char in j:
#         if 'A' <=char <='Z':
#             if char not in df:
#                 df[char] = 0
#             df[char] +=1
# plt.figure(figsize=(15,5))
# movie_df = pd.DataFrame(data={"names":list(df.keys()), "tickets":list(df.values())})
# plt.bar(df.keys(),df.values())
# plt.xticks(fontproperties=font,size=12)
# plt.show()

# digits = [
#     ["XXX", "X.X", "X.X", "X.X", "XXX"],  # 0
#     ["..X", "..X", "..X", "..X", "..X"],  # 1
#     ["XXX", "..X", "XXX", "X..", "XXX"],  # 2
#     ["XXX", "..X", "XXX", "..X", "XXX"],  # 3（注意：这里和2一样，通常3会有不同的表示）
#     ["X.X", "X.X", "XXX", "..X", "..X"],  # 4
#     ["XXX", "X..", "XXX", "..X", "XXX"],  # 5
#     ["XXX", "X..", "XXX", "X.X", "XXX"],  # 6
#     ["XXX", "..X", "..X", "..X", "..X"],  # 7
#     ["XXX", "X.X", "XXX", "X.X", "XXX"],  # 8
#     ["XXX", "X.X", "XXX", "..X", "XXX"]   # 9
# ]
# n = int(input('请输入数字的个数:'))
# number_str = input('请输入自然数:').strip()
# screen = [['.' for _ in range(5 * n + n - 1)] for _ in range(5)]
# for i, digit in enumerate(number_str):
#     digit_matrix = digits[int(digit)]
#     for row in range(5):  # 遍历点阵的每一行
#         for col in range(len(digit_matrix[row])):  # 使用len()来确保不会超出字符串长度
#             if digit_matrix[row][col] == 'X':
#                 screen[row][i * 6 + col] = 'X'  # 注意：这里假设每个数字占6列（5列显示+1列间隔）
# for row in screen:
#     print(''.join(row))

# A = input('')
# B = input('')
# char_to_num = {chr(i): j for i, j in zip(range(65, 91), range(1, 27))}
# c = 1
# b = 1
# for i in A:
#     i = char_to_num[i]
#     c = c*i
# for j in B:
#     j = char_to_num[j]
#     b = b*j
# if   c % 47 == b % 47:
#     print('GO')
# else:
#     print('STAY')

# A = input('')
# B = {'zero':0,
#     'one':1,
#      'two':2,
#      'three':3,
#      'four':4,
#      'five':5,
#      'six':6,
#      'seven':7,
#      'eight':8,
#      'nine':9,
#      'ten':10,
#      'eleven':11,
#      'twelve':12,
#      'thirteen':13,
#      'fourteen':14,
#      'fifteen':15,
#      'sixteen':16,
#      'seventeen':17,
#      'eighteen':18,
#      'nineteen':19,
#      'twenty':20,
#      'another':1}
# words = A.split()
# results = []
# for i in words:
#     if i in B:
#         c = int(B[i])**2 %100
#         results.append(str(c).zfill(2))
# m = sorted(results)
# n = ''.join(m).lstrip('0')
# print(n)

# A  = input('请输入数据:')
# c = ''.join(reversed(str(A)))
# print(c)

# B = A[::-1].lstrip('0')
# print('{}%'.format(B))

# m = A.split('.')
# v = m[0][::-1].lstrip('0')
# k = m[1][::-1]
# l = v + '.' + k
# print(l)


#高级版数字转换
# A = input('请输入：')
# if '%' in A:
#     m = A[:-1]
#     B = m[::-1].lstrip('0')
#     print('{}%'.format(B))
# elif '.' in A:
#     m = A.split('.')
#     v = m[0][::-1].lstrip('0')
#     k = m[1][::-1]
#     l = v + '.' + k
#     print(l)  
# elif '/' in A:  
#     m = A.split('/')
#     v = m[0][::-1].lstrip('0')
#     k = m[1][::-1]
#     l = v + '/' + k
#     print(l)
# else:
#     c = ''.join(reversed(str(A)))
#     print(c)

#时间转换
# t = input('请输入：')
# H = int(t)//3600
# M = (int(t)-3600)//60
# S = (int(t)-3600) % 60
# print('{}:{}:{}'.format(H,M,S))

#单词覆盖还原
# def count_boy_and_girl(s):
#     l = len(s)
#     count_boy = 0
#     count_girl = 0
#     i = 0
#     while i < l:
#         if i + 2 < l and s[i:i+3] == "boy":
#             count_boy += 1
#             for j in range(i, i+3):
#                 s = s[:j] + '.' * 3 + s[j+3:]
#             i += 3
#         elif i + 3 < l and s[i:i+4] == "girl":
#             count_girl += 1
#             for j in range(i, i+4):
#                 s = s[:j] + '.' * 4 + s[j+4:]
#             i += 4
#         else:
#             i += 1
#     return count_boy, count_girl
# s = "......boyogirlyy......girl......."
# print(count_boy_and_girl(s)) 

#时间转换
# t = input('请输入：')
# H = int(t)//3600
# M = (int(t)-3600)//60
# S = (int(t)-3600) % 60
# print('{}:{}:{}'.format(H,M,S))

#单词覆盖还原
# def A(s):
#     lm = len(s)
#     count_boy = 0
#     count_girl = 0
#     for i in range(lm):
#         if s[i:i+3] == 'boy':
#             count_boy += 1
#             for j in range(i,i+3):
#                 s = s[:j] + '.'*3 + s[j+3:]
#         elif s[i:i+4] =='girl':
#             count_girl += 1
#             for j in range(i,i+4):
#                 s = s[:j] + '.'*4 +s[j+4:]
#         for m in range(lm):
#             if s[m:m+1] =='o' or 'y':
#                 count_boy += 1
#                 for j in range(i,i+1):
#                     s = s[:j] + '.' +s[j+1:]    
#     return count_boy,count_girl                            
# s ='......boyogirlyy......girl.......'  
# print(A(s))        
#字母覆盖
# def A(s):
#     count_boy = 0
#     count_girl = 0
#     i = 0
#     while i < len(s):
#         if s[i] == 'o' or s[i] == 'y':
#             count_boy += 1
#         if i + 2 < len(s) and s[i:i+3] == 'boy':
#             count_boy += 1
#             s = s[:i] + '...' + s[i+3:]
#         elif i + 3 < len(s) and s[i:i+4] == 'girl':
#             count_girl += 1
#             s = s[:i] + '....' + s[i+4:]
#         else:
#             i += 1
#     return count_boy, count_girl

# s = '......boyogirlyy......girl.......'
# count_boy, count_girl = A(s)
# print(count_boy)
# print(count_girl)
      
#质数筛
# n = input() 
# a = input().split()
# b = []
# new_b = [int(i) for i in a]
# new_a = [int(i) for i in a if int(i) != 2]
# b = []
# if 2 in new_b:
#     for i in new_a:
#         if i % 2 ==1:
#             b.append(i)
#     b.append(2)
#     print(b)
# else:
#     for i in new_b:
#         if i % 2 ==1:
#             b.append(i)
#         print(b)              

#闰年选择
# x , y = input().split()
# x = int(x)
# y = int(y)
# c = []
# for i in range(x,y+1):
#     if i % 4 == 0:
#         c.append(i)
# b = len(c)
# print(b)    
# print(c)    

# A,B,C = input().split()
# A = int(A)
# B = int(B)
# C = int(C)
# m = A*0.2 + B*0.3 +C*0.5
# print(f"{m:.0f}")

#不高兴的津津
# import pandas as pd
# A = pd.Series([[5,3],[6,2],[7,2],[5,3],[5,4],[0,4],[0,6]])
# B = pd.Series([x[0] + x[1] for x in A])
# C = B.sort_values(ascending=False)
# N = C.index
# M = N[0]
# print(int(M) + 1)

# schedule = []
# for _ in range(7):
#     line = input().split()
#     schedule.append([int(line[0]), int(line[1])])
# import pandas as pd
# B = pd.Series([x[0] + x[1] for x in schedule])
# C = B.sort_values(ascending=False)
# N = C.index
# M = N[0]
# print(int(M) + 1)

#买铅笔
# n = input('')
# n = int(n)
# A = []
# for _ in range(3):
#     line = input().split()
#     A.append([int(line[0]),int(line[1])])   
# for i in A:
#     if i[0] % n == 0:
#         m = (i[0]//n) * i[1]
#         print(m)
#     elif n < i[0]:
#         k = i[1]
#         print(k)
#     else:
#         j = (n//i[0]) +1
#         l = j*i[1]
#         print(l)

#储蓄计划
# def check_budget(budgets):
#     initial_money = 300  
#     saved_money = 0  
#     hand_money = 0 
#     for month, budget in enumerate(budgets, start=1):
#         hand_money += initial_money
#         hand_money -= budget
#         if hand_money >= 100:
#             save_amount = (hand_money // 100) * 100
#             saved_money += save_amount
#             hand_money -= save_amount
#         if hand_money < 0:
#             print('-{}'.format(month))
#             return False, 0
#     final_money = hand_money + saved_money * 1.2
#     return True, final_money
# A = []
# for _ in range(12):
#     line = input().split()
#     A.append(int(line[0])) 
# result, final_money = check_budget(A)
# if result:
#     print("{:.0f}".format(final_money))

#小鱼的数字游戏
# A = input()
# B = A[::-1].lstrip('0')
# print(B)

# A  = input('请输入数据:')
# c = ''.join(reversed(str(A)))
# print(c)

# B = A[::-1].lstrip('0')
# print('{}%'.format(B))

#小鱼的数字游戏
# 输入数据并转换为列表
# A = input("").split()
# B = []
# C = [i for i in A if int(i)!= 0]
# for i in C:
#     B.insert(0,i)
# B = list(B)
# print(B)   

#地板的铺法(记忆法)
# def A(n,memo={}):
#     if n < 0:
#         return 0
#     if n ==0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n in memo:
#         return memo[n]
#     memo[n] = A(n-1,memo) + A(n-2,memo)
#     return memo[n]
# n = input()
# n = int(n)
# print(A(n)) 

# def main():
#     try:
#         # 以二进制模式打开文件
#         with open("C:\\Users\\周顺\\Desktop\\100\\NMC.to-111.raw", "rb") as fp:  # "rb" 表示以二进制读模式打开文件
#             with open("100.dat", "wb") as fp1:  # "wb" 表示以二进制写模式打开文件
#                 while True:
#                     # 逐字节读取文件内容
#                     byte = fp.read(1)
#                     if not byte:
#                         break  # 如果没有更多内容，则退出循环
#                     # 将读取到的字节写入到另一个文件中
#                     fp1.write(byte)
#     except IOError as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     main()

#字符串对比
# a = input('请输入:')
# b = input('请输入:')
# c = 0
# d = 0
# for i in a:
#     c += 1
# for j in b:
#     d += 1       
# if c != d:
#     print('1')
# if c == d:
#     if i == j :
#         print('2')
#     if i.upper() == j.upper() and i != j :
#         print('3')
#     if i.upper() != j.upper():
#         print('4')    

#分解质因数
# a,b = map(int,input('请输入').split())
# for i in range(a,b+1):
#     if i % 2 == 0 :
#         if i ==2:
#             print('{}={}'.format(i,i))
#         else:
#             for j in range(1,i+1):
#                 if i == 2 * j:
#                     print('{}=2{}'.format(i,j))
#     if i % 3 == 0 and i % 2 !=0:
#         for j in range(1,i+1):
#             if i == 3* j:
#                 if j != 1:
#                     print('{}=3{}'.format(i,j))
#                 else:
#                     print('{}={}'.format(i,i))             
#     if i % 2 != 0 and i % 3 != 0:
#         for j in range(1,i+1):
#             for m in range(j,i+1):
#                 if i == j*m:  
#                     if i ==j or i == m:
#                         if j == 1 or m == 1:
#                             print('{}={}'.format(i,i))
#                     else:
#                         print('{}={}{}'.format(i,j,m))    

#矩形面积交
# A = []
# for _ in range(2):
#     line = input().split()
#     A.append([int(line[0]),int(line[1]),int(line[2]),int(line[3])])   

# B = A[0][2:4]
# C = A[1][0:2]
# if A[0][1] > A[1][1]:
#     l = int(A[1][2]) - int(A[0][0])
#     c = int(A[1][3]) - int(A[0][1])
#     a = l* c
#     print('{:.2f}'.format(a))
# else:        
#     l = int(B[0])-int(C[0])
#     c = int(B[1])-int(C[1]) 
#     s = l * c
#     print('{:.2f}'.format(s))

# n = input('请输入位数:')
# n = int(n)
# def hanoi(n,A,B,C):
#     if n == 1:
#         print(f'将圆盘1从{A}移动dao{C}')
#     else:
#         hanoi(n-1,A,C,B)
#         print(f'圆盘{n}从{A}移动到{C}')
#         hanoi(n-1,B,A,C)
# hanoi(n,'A','B','C') 

#回文数
# def A(s):
#     n = len(s)
#     # 字符到索引的映射
#     char_map = {}
#     for i, char in enumerate(s):
#         if char in char_map:
#             char_map[char].append(i)
#         else:
#             char_map[char] = [i]
#     swaps = 0
#     # 处理字符对的交换
#     for char, indices in char_map.items():
#         # 字符数量为奇数，且中间的字符不需要处理
#         if len(s) % 2 == 1 and n % 2 == 1:
#             mid_index = n // 2
#             if mid_index in indices:
#                 indices.remove(mid_index)
#         # 处理字符对的左右交换
#         i = 0
#         j = len(s) - 1
#         while i < j:
#             left_pos = indices[i]
#             right_pos = indices[j]
#             # 计算当前字符对之间的空位数量
#             distance = right_pos - left_pos - (j - i)
#             # 每次只能相邻交换，因此每次可以减少两个位置的距离
#             swaps += distance // 2
#             # 移动 i 和 j 指针
#             i += 1
#             j -= 1
#     return swaps
# # 测试用例
# s = "mamad"
# print(A(s))       

# s = 'mamad'
# n = len(s)
# char_map = {}
# for i, char in enumerate(s):
#     if char in char_map:
#         char_map[char].append(i)
#     else:
#         char_map[char] = [i]
# print(char_map)        
# swaps = 0
# for char, indices in char_map.items():
#     if len(indices) % 2 == 1:
#         mid_index = indices[len(indices) // 2]
# m =n - mid_index + 1
# i = 0
# j = len(indices) - 1
# print(j)
# while i < j:
#     left_pos = indices[i]
#     right_pos = indices[j]
#     distance = right_pos - left_pos - (j - i)
#     swaps += distance // 2
#     i += 1
#     j -= 1
# print(swaps+m)
# s = 'mama'
# n = len(s)
# char_map = {}
# for i, char in enumerate(s):
#     if char in char_map:
#         char_map[char].append(i)
#     else:
#         char_map[char] = [i]
# # 初始化交换次数
# swaps = 0
# for char, indices in char_map.items():
#     if len(indices) % 2 == 1 and len(s) % 2 ==1:
#         mid_index = indices[len(indices) // 2]
#         m = n - mid_index + 1
#         for i in range(len(indices) // 2):
#             swaps += (indices[i] - indices[len(indices) // 2] - i)
#             swaps += (n - indices[len(indices) // 2] - 1 - (indices[len(indices) // 2 + 1 + i] - n + 1))
#     else:
#         # 如果字符出现次数为偶数，则不需要移动中间字符
#         for i in range(len(indices) // 2):
#             swaps += (indices[i] - indices[len(indices) // 2 - 1] - i)
#             swaps += (n - indices[len(indices) // 2 - 1] - 1 - (indices[len(indices) // 2 + i] - n + 1))
# print(swaps)

#数的读法
# a = input('请输入:')
# b = len(a)
# m = ['','十','百','千','万','十万','百万','千万','亿','十亿']
# k = '零一二三四五六七八九'


# def number_to_chinese(num):
#     # 数字到中文的映射
#     units = ["", "十", "百", "千", "万", "十万", "百万", "千万", "亿"]
#     digits = "零一二三四五六七八九"
#     # 将数字转换为字符串，并去掉前导零
#     num_str = "{:0>16}".format(num)[-16:]  # 保证数字至少有16位，方便处理
#     length = len(num_str)
#     # 初始化结果字符串
#     result = []
#     zero_flag = False  # 标记零的状态
#     # 从低位到高位处理每一位数字
#     for i in range(length - 1, -1, -1):
#         digit = int(num_str[i])
#         position = length - 1 - i
#         if digit == 0:
#             if not zero_flag and (position % 4 != 0 or result):
#                 result.insert(0, digits[digit])
#                 zero_flag = True
#         else:
#             result.insert(0, digits[digit] + units[position % 4])
#             zero_flag = False
#             # 如果当前位是万或亿，并且之前没有数字，则插入一个"零"来分隔单位
#             if position % 4 == 0 and not result[0].startswith("零"):
#                 result.insert(0, "零")
#             # 去掉多余的零，例如 "零十" 变为 ""
#             if result[0] == "零十":
#                 result.pop(0)

#     # 去掉结果开头的零和多余的单位
#     while result and result[0] == "零":
#         result.pop(0)
    
#     # 特殊情况处理：数字为零
#     if not result:
#         return "零"
    
#     # 合并结果
#     chinese_num = ''.join(result)
#     # 处理结果中的连续零，例如 "一千零零零百" 变为 "一千"
#     chinese_num = chinese_num.replace("零千", "千").replace("零百", "百").replace("零十", "").replace("零零", "零")
#     # 去掉末尾的零，例如 "一千零" 变为 "一千"
#     if chinese_num.endswith("零"):
#         chinese_num = chinese_num[:-1]
    
#     return chinese_num
# num = 1234567000
# print(number_to_chinese(num))
#查找
# def A(value,key):
#     for i in range(len(value)):
#         if value[i] == key:
#             return i 
#     return -1
# value = [1,2,3,4,5,7,2]
# key = 4
# result = A(value,key)
# if result == -1:
#     print('查找失败')
# else:
#     print('查找成功',result)    

# #二分法查找
# def A(value,key,left,right):
#     mid = (left+right) // 2
#     if value[mid] < key:
#         left = mid + 1
#         return A(value,key,left,right)
#     elif value[mid] > key:
#         right = mid - 1
#         return A(value,key,left,right)
#     else:
#         return mid
# value = [3,4,5,6,7,8,9,9]
# result = A(value,6,0,len(value)-1)
# print('查找成功',result)    

#排序,冒泡排序
# def A(array):
#     n = len(array)
#     for i in range(n-1,0,-1):
#         for j in range(0,i):
#             if array[j] > array [j+1]:
#                 array[j],array[j+1] = array[j+1],array[j]
#     return array        
# array = [0,4,5,3,21,7]
# print(A(array))           
     
# s = 'mamad'
# n = len(s)
# char_map = {}
# for i, char in enumerate(s):
#     if char in char_map:
#         char_map[char].append(i)
#     else:
#         char_map[char] = [i]
# print(char_map)        
# swaps = 0
# for char, indices in char_map.items():
#     if len(indices) % 2 == 1:
#         mid_index = indices[len(indices) // 2]         
# s = 'mama'
# n = len(s)
# char_map = {}
# char_ma = {}
# for i,char in enumerate(s):
#     if char in char_map:
#         char_map[char].append(i)
#     else:
#         char_map[char] = [i]
# for char,indices in char_map.items():
#     if len(indices) % 2 == 1:
#         mid_index = indices[len(indices) // 2]
#         m =n - mid_index + 1
#         mp = s[0:(n//2)] + s[mid_index] + s[(n//2):n-1]
#         print(mp)
#         for i,charmn in enumerate(mp):
#             if charmn in char_ma:
#                 char_ma[charmn].append(i)
#             else:
#                 char_ma[charmn] = [i]
#         print(char_ma)    
#         if mp[0] != mp[n-1]:
#             k = char_ma[mp[0]][1]
#             l = n - int(k) -1
#             m = n - mid_index +1 + l
#             s = mp[0:k] + mp[k+1:n] + mp[k]
#         print(m)    
#     else:
#         for i,charmn in enumerate(s):
#             if charmn in char_ma:
#                 char_ma[charmn].append(i)
#             else:
#                 char_ma[charmn] = [i]
#         print(char_ma)    
#         if s[0] != s[n-1]:
#             k = char_ma[s[0]][1]
#             m = n - int(k) +1
#             s = s[0:k] + s[k+1:n]
#             print(s)

# def number_to_chinese_pinyin(num_str):
#     # 定义数字到拼音的映射
#     num_to_pinyin = {
#         '0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
#         '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu'
#     }
    
#     # 定义单位
#     units = ['', 'shi', 'bai', 'qian']
#     big_units = ['', 'wan', 'yi']  # 大单位：万、亿
    
#     # 去掉前导零
#     num_str = num_str.lstrip('0')
#     if not num_str:
#         return 'ling'
    
#     # 根据长度确定需要拆分的部分
#     length = len(num_str)
#     if length > 8:
#         billion_part = num_str[:-8]
#         ten_million_and_below = num_str[-8:]
#     else:
#         billion_part = ''
#         ten_million_and_below = num_str
    
#     if length > 4 or (length == 4 and int(num_str) > 1000):  # 处理万及以上
#         ten_million_part = ten_million_and_below[:-4] if ten_million_and_below else ''
#         thousand_part = ten_million_and_below[-4:]
#     else:
#         ten_million_part = ''
#         thousand_part = ten_million_and_below
    
#     # 转换各部分为拼音
#     def convert_part(part):
#         pinyin = []
#         zero_flag = False  # 标记是否遇到过零
#         for i, digit in enumerate(reversed(part)):
#             if digit == '0':
#                 if not zero_flag and pinyin:  # 只在非首位且之前非零时插入ling
#                     pinyin.insert(0, num_to_pinyin[digit])
#                 zero_flag = True
#             else:
#                 pinyin.insert(0, num_to_pinyin[digit] + units[i] if i < len(units) - 1 else '')
#                 zero_flag = False
#         # 处理末尾的零（如果整个部分都是零，则只保留一个ling）
#         if pinyin[0] == 'ling' and len(pinyin) > 1:
#             if all(p == 'ling' for p in pinyin):
#                 pinyin = ['ling']
#             else:
#                 while pinyin and pinyin[0] == 'ling':
#                     pinyin.pop(0)
#         elif not pinyin:  # 如果部分为空（即全为0但被其他部分处理），则添加ling
#             pinyin = ['ling']
#         return ' '.join(pinyin).strip()
    
#     # 处理亿和万的部分，如果它们存在
#     result = []
#     if billion_part:
#         result.append(convert_part(billion_part) + big_units[2])
#     if ten_million_part:
#         result.append(convert_part(ten_million_part) + big_units[1])
#     if thousand_part or (not billion_part and not ten_million_part):
#         # 如果千位以下部分存在，或者没有亿和万的部分（即该部分本身就是整个数字）
#         result.append(convert_part(thousand_part))
    
#     # 合并结果，并去除可能的首尾空格
#     return ' '.join(result).strip()

# # 测试
# num_str = "123456700"
# print(number_to_chinese_pinyin(num_str))  # 输出应为: shi er yi san qian si bai wu shi liu wan qi qian ling jiu
#买铅笔
# n = input('')
# n = int(n)
# A = []
# for _ in range(3):
#     line = input().split()
#     A.append([int(line[0]),int(line[1])])   
# for i in A:
#     if i[0] % n == 0:
#         m = (i[0]//n) * i[1]
#         print(m)
#     elif n < i[0]:
#         k = i[1]
#         print(k)
#     else:
#         j = (n//i[0]) +1
#         l = j*i[1]
#         print(l)
        

# n = input('请输入:')
# n = int(n)
# ans = float('inf')
# for _ in range(3):
#     a,b = list(map(int,input().split()))
#     c = n/a
#     if int(c) != c:
#         c = int(c+1)
#     ans = min(ans,int(c*b))
# print(ans)        
#isn代码
# isbn = input()
# x = sum([(i+1)*int(num) for i,num in enumerate(isbn.replace('-','')[:-1])]) % 11
# if x == 10:
#     x ='X'
# if str(x) == isbn[-1]:
#     print('Right')
# else:
#     print(isbn[:-1]+f'{x}')
#阶乘之和
# n = int(input())
# num = 1
# ans = 0
# for i in range(1,n+1):
#     num *= i
#     ans += num
# print(ans)

#递推求阶级和
# def fact(n:int) -> int:
#     if n==1:
#         return 1
#     return fact(n-1)*n
# print(fact(3))
# def fact(n):
#     if n== 1:
#         return 1
#     else:
#         return n* fact(n-1)
# sum = 0
# n = int(input())
# for i in range(1,n+1):
#     sum = sum + fact(i)    
# print(sum)    

#买铅笔
# n = input('请输入:')
# n = int(n)
# for _ in range(3):
#     a,b = map(int,input().split())
#     c = n/a
#     if int(c) != c:
#         c = int(c) + 1
#         m = c*b
# print(m)

# n = input('请输入:')
# x = n.replace('-','')
# a = sum([(i+1)*int(num) for i,num in enumerate(x[:-1])]) % 11
# if str(a) == x[-1]:
#     print('right')
# else:
#     n = n[:-1]+str(a)
#     print(n)

#递归算法
# def A(n):
#     if n == 1:
#         return 1
#     else:
#         return n *A(n-1)  
# n = input('请输入:')
# n = int(n)
# sum = 0
# for i in range(1,n+1):
#     sum = sum + A(i)
# print(sum)    

#计数问题
# n,x = map(int,input().split()) 
# m = 0
# for i in range(1,n+1):
#     for j in str(i):
#         if j == str(x):
#             m += 1
# print(m)            

#级数求和
# k = input()
# k = int(k)
# s = 0
# n = 1
# while True:
#         s += 1/int(n)
#         if s > k:
#             print(n)
#             break
#         n += 1

#小鱼比可爱
# n = int(input('请输入:'))
# a = input('请输入:').split()
# for i in range(0,len(a)):
#     m =0
#     for j in range(0,i):
#         if a[i] > a[j]:
#             m += 1
#     print('{}'.format(m),end=' ')            
        
#小鱼的数字游戏
# import numpy as np
# import pandas as pd
# A = input().split()
# B = []
# C = [i for i in A if int(i)!= 0]
# for i in C:
#     B.insert(0,i)
# print(B)

         
#回文数
# a, b = map(int, input().split())
# for i in range(a, b + 1):
#     if i == 2:
#         m = ''.join(list(reversed(str(i))))
#         if str(i) == m:
#             print(i)
#     if i % 2==1 and i % 3 !=0:
#         if len(str(i)) >= 2:
#             if i % 7 != 0 and i %5 !=0 and i % 11!=0 and i %17!= 0:
#                 m = ''.join(list(reversed(str(i))))
#                 if str(i) == m:
#                     print(i)
#         if len(str(i)) < 2:   
#             m = ''.join(list(reversed(str(i))))
#             if str(i) == m:
#                 print(i)

#金币
# k = int(input('请输入:'))
# a = 0
# for i in range(1,k):
#     n = abs(k-((1+i)*i)/2)
#     if n == 0:
#         for j in range(1,i+1):
#             a += j*j
#         print(a)    

#金币系统
# def calculate_gold_coins(days):
#     total_coins = 0  # 总金币数
#     n = 1            # 当前阶段每天应收到的金币数（n会逐渐增加）
#     days_in_stage = 0  # 当前阶段已过的天数（从0开始）

#     for day in range(1, days + 1):
#         # 每天都会收到n枚金币
#         total_coins += n
#         days_in_stage += 1

#         # 如果当前阶段已结束（即已过了n天），则进入下一个阶段
#         if days_in_stage == n:
#             n += 1
#             days_in_stage = 0  # 重置阶段内天数计数器

#     return total_coins

# # 示例：计算骑士在前10天收到的金币总数
# days = 1000
# total_gold = calculate_gold_coins(days)
# print(f"骑士在前{days}天总共收到了{total_gold}枚金币。")
#金币
# def A(days):
#     m = 0 #总金币
#     n = 1 #分的金币
#     guoqudesj = 0 # 过去的时间
#     for day in range(1,days+1):
#         m += n
#         guoqudesj +=  1
#         if guoqudesj == n:
#             n += 1
#             guoqudesj = 0
#     return m 
# days = int(input('请输入:'))
# print(A(days))           

#数字反转
# N = input('请输入:')
# if int(N) >= 0:
#     A = ''.join(reversed(N)).lstrip('0')
#     print(A)
# else:
#     a = N[1:]
#     B = ''.join(reversed(a)).lstrip('0')
#     print('-{}'.format(B))    

#小鱼的数字游戏
# # 读取输入的一行
# input_line = input().strip('0')
 
# # 将输入的行按空格分割成数字字符串列表
# numbers = input_line.split()
# # 反转数字列表
# reversed_numbers = numbers[::-1]
 
# # 将反转后的数字列表以空格分隔输出
# print(' '.join(reversed_numbers))

# n = input().strip('0')
# numb = n.split()
# a = numb[::-1]
# print(' '.join(a))

# A = input("").split()
# B = []
# C = [i for i in A if int(i)!= 0]
# for i in C:
#     B.insert(0,i)
# B = list(B)
# print(' '.join(B))  

#校门外的树
# l,m = map(int,input('请输入:').split())
# A = []
# for _ in range(m):
#     line = input('请输入区域:').split()
#     A.append([int(line[0]),int(line[1])])
# for row in A:
#     u = row[0]
#     v = row[1]
#     print('{}'.format(u),end=' ')
    
# #     print(u)
# # a = max(u,v)
# # b = min(u,v)
# # print(a)
    
#冰雹猜想
# def A(n,a):
#     a = []
#     if n== 1:
#         print()
#     elif n %2 == 1:
#         n = n * 3 +1
#         a.append(n)
#         return A(n)
#     else:
#         n = n // 2
#         a.append(n)
#         return A(n)
#     return a
# n = int(input('请输入:'))
# print(n)
# for i in reversed(A(n)):
#     print(i)   
    
# def A(n, results=None):
#     if results is None:
#         results = []  
#         results.append(n)
#     if n == 1:
#         pass
#     elif n % 2 == 1:
#         n = n * 3 + 1
#         results.append(n) 
#         return A(n, results)  
#     else:
#         n = n // 2
#         results.append(n) 
#         return A(n, results) 
#     return results 
# n = int(input())
# results = A(n)
# for result in reversed(results):
#     print('{}'.format(result),end=' ')

#质数筛
# n = input('请输入:') 
# a = input('请输入:').split()
# m = max(list(a))
# print(m)
# b = []
# new_a = [int(i) for i in a]
# if 2 in a:
#     b.append(2)
# else:
#     for i in a:
#         for j in range(2,int(m)+1):
#             for k in range(2,int(m)+1):
#                 if i != j * k and i % 2 ==1:
#                     b.append(i)
#                 print(b)    

# n = input() 
# a = input().split()
# m = max(list(a))
# m = int(m)
# b = []
# new_b = [int(i) for i in a]
# if 2 in new_b:
#     b.append(2)
# else:
#     for i in new_b:
#         if i % 2 ==1:
#             for j in range(2,m):
#                 for l in range(2,m):
#                     if i != j *l: 
#                         b.append(i)
# m = ' '.join(map(str, b))
# print(m, end=' ')

#上学迟到
# s,v = map(int,input('请输入:').split())
# t = s / v
# if int(t) != t:
#     t = int(t) + 1
# h = 8 * 60 - t
# if h < 0:
#     l = 24*60 + 8*60 -t
#     m = l // 60
#     b = len(str(m))-2
#     if b == 2:
#         k = l % 60
#         if len(str(k))-2 == 2:
#             print('{:.0f}:{:.0f}'.format(m,k))
#         if len(str(k))-2 == 1:
#             print('{:.0f}:{:.0f}0'.format(m,k))
                
#     if b == 1:
#         k = l % 60
#         if len(str(k))-2 == 2:
#             print('0{:.0f}:{:.0f}'.format(m,k))
#         if len(str(k))-2 == 1:
#             print('0{:.0f}:{:.0f}0'.format(m,k))
# else:
#     m = h//60
#     k = h % 60
#     l = len(str(k))
#     if len(str(k)) == 2:
#         print('0{:.0f}:{:.0f}'.format(m,k))
#     if len(str(k)) == 1:
#         print('0{:.0f}:{:.0f}0'.format(m,k))

#校门外的树
# l,m = map(int,input('请输入:').split())
# A = []
# for _ in range(m):
#     line = input('请输入区域:').split()
#     A.append([int(line[0]),int(line[1])])
# A.sort(key=lambda x: x[0])
# u = []
# v = []
# for row in A:
#     u.append(row[0])
#     v.append(row[1])  
# hp = 0
# for i in range(1,m):
#     if int(u[i]) <= int(v[i-1]):
#             h = -(int(u[i-1]) - int(v[i])) + 1
#             hp += h                
# for i in range(m):
#     for j in range(m):
#         if int(u[i]) > int(v[j]):
#             lp = int(v[i]) - int(u[i]) + 1
#             print(lp)
# print(l + 1 -(hp+lp))

#旗鼓相当的对手
# N = int(input('请输入:'))
# A = []
# for _ in range(N):
#     line= input().split()
#     A.append([int(line[0]),int(line[1]),int(line[2])])
# yu = []
# shu = []
# ying = []
# for i in A:
#     yu.append(i[0])
#     shu.append(i[1])
#     ying.append(i[2])
# m = 0    
# ans = []
# for i in A:
#     a = 0
#     for j in i:
#         a += j
#     ans.append(a)
# for i in range(1,N):
#     if abs(int(yu[i-1]) - int(yu[i])) <=5:
#             if abs(int(shu[i-1]) - int(shu[i])) <=5:
#                     if abs(int(ying[i-1]) - int(ying[i])) <=5:
#                         if abs(int(ans[i-1]) - int(ans[i])) <=10:
#                             m += 1
# print(m)

#彩票摇奖
# n = int(input('请输入行数:'))
# zhong = list(map(int, input('请输入数字，用空格分隔:').split()))
# A = []
# for _ in range(n):
#     line = list(map(int, input('请输入7个整数,用空格分隔:').split()))
#     A.append(line)
# # 对于A中的每一行（列表），统计该行中有多少个元素存在于zhong列表中
# coun = []
# for row in A:
#     counte = sum(1 for num in row if num in zhong)
#     coun.append(counte)
# t = 0
# yi = 0
# er = 0
# san = 0
# si = 0
# wu = 0
# liu = 0
# for i in coun:
#     if i == 1:
#         liu += 1
#     elif i == 2:
#         wu += 1
#     elif i == 3:
#         si += 1
#     elif i == 4:
#         san += 1
#     elif i == 5:
#         er += 1
#     elif i == 6:
#         yi += 1
#     elif i == 7:
#         t += 1
#     else:
#         print('{} {} {} {} {} {} {}'.format(t,yi,er,san,si,wu,liu))      
# print('{} {} {} {} {} {} {}'.format(t,yi,er,san,si,wu,liu))                              

# ## 调整机体姿态
# adjustrobot_position(center_x,center_y, img_w, img_h)
# def generate_magic_square(N):
#     # 初始化一个N×N的矩阵，填充为0
#     magic_square = [[0] * N for _ in range(N)]
    
#     # 将数字1放在第一行的中间位置
#     magic_square[0][N // 2] = 1
    
#     # 定义当前位置(i, j)的初始值
#     i, j = 0, N // 2
    
#     for num in range(2, N * N + 1):
#         # 获取前一个数字的位置
#         prev_i, prev_j = i, j
        
#         # 根据规则计算下一个数字的位置
#         if i == 0 and j != N - 1:  # 第一行但不在最后一列
#             i = N - 1
#             j += 1
#         elif i != 0 and j == N - 1:  # 最后一列但不在第一行
#             i -= 1
#             j = 0
#         elif i == 0 and j == N - 1:  # 第一行且最后一列
#             i += 1
#             j = i  # 直接放在正下方
#         elif (prev_i - 1 < N and prev_j + 1 < N and magic_square[prev_i - 1][prev_j + 1] == 0) or \
#              (prev_i - 1 >= 0 and prev_j + 1 >= N):  # 右上方有空位或超出右边界
#             i -= 1
#             j += 1
#         else:  # 右上方没有空位，则放在正下方
#             i += 1
        
#         # 确保位置没有越界，对于奇数N，这不会发生，但为安全起见
#         i = i % N
#         j = j % N
#         # 将当前数字放入计算出的位置
#         magic_square[i][j] = num
#     return magic_square
# # 示例：生成5×5的幻方
# N = 25
# magic_square = generate_magic_square(N)
# for row in magic_square:
#     print(" ".join(map(str, row)))

# #幻方
# def generate_magic_square(N):
#     # 初始化一个N×N的矩阵，这里不再需要填充为0，因为后续会直接赋值
#     magic_square = [[0] * N for _ in range(N)]
#     # 填充幻方矩阵
#     num = 1  # 从1开始填充数字
#     i, j = 0, N // 2  # 起始位置：第一行中间
#     while num <= N * N:
#         magic_square[i][j] = num  # 将当前数字放入计算出的位置
#         # 计算下一个位置
#         new_i, new_j = (i - 1) % N, (j + 1) % N  # 先尝试右上方位置
#         if magic_square[new_i][new_j] != 0:  # 如果右上方已被填充，则放在正下方
#             new_i, new_j = (i + 1) % N, j  # 正下方位置（i+1可能超出范围，但%N会处理）
#             # 注意：由于N是奇数，且我们从中间开始，所以i+1永远不会使i等于N（即不会越界到下一行数组）
#             # 在这个特定算法中，实际上不需要对i进行取模操作，因为它永远不会超出范围
#             # 但为了代码的通用性和清晰性，我还是保留了它
#         # 更新当前位置为下一个要填充的位置
#         i, j = new_i, new_j
#         num += 1
#     # 注意：由于我们是从中间开始且N是奇数，算法保证了我们不会越界，并且每个位置都会被填充
#     # 因此，上面的while循环可以安全地运行直到num > N * N
#     return magic_square
# def main():
#     # 输入验证
#     while True:
#         try:
#             N = int(input("请输入一个奇数N（1 ≤ N ≤ 39）: "))
#             if 1 <= N <= 39 and N % 2 != 0:
#                 break
#             else:
#                 print("输入无效，请确保N是一个在1到39之间的奇数。")
#         except ValueError:
#             print("输入无效，请输入一个整数。")
#     # 生成并打印幻方
#     magic_square = generate_magic_square(N)
#     for row in magic_square:
#         print(" ".join(map(str, row)))
# # 运行主函数
# if __name__ == "__main__":
#     main()
    
# #自动修正
# a = input('请输入:')
# b= a.upper()
# print(b)

#手机
# a = input('请输入:')
# a= a.lower()
# k = 0
# for i in a:
#     if i == ' ':
#         k += 1
#     elif i == 'a':
#         k += 1
#     elif i == 'b':
#         k += 2
#     elif i == 'c':
#         k += 3
#     elif i == 'd':
#         k += 1
#     elif i == 'e':
#         k+=2
#     elif i == 'f':
#         k += 3
#     elif i == 'g':
#         k += 1
#     elif i == 'h':
#         k += 2
#     elif i == 'i':
#         k += 3
#     elif i == 'j':
#         k += 1
#     elif i == 'k':
#         k += 2
#     elif i == 'l':
#         k += 3
#     elif i == 'm':
#         k += 1
#     elif i == 'n':
#         k += 2
#     elif i == '0':
#         k += 3
#     elif i == 'p':
#         k += 1
#     elif i == 'q':
#         k += 2
#     elif i == 'r':
#         k += 3
#     elif i == 's':
#         k += 4
#     elif i == 't':
#         k += 1
#     elif i == 'u':
#         k += 2
#     elif i == 'v':
#         k += 3
#     elif i == 'w':
#         k += 1
#     elif i == 'x':
#         k += 2
#     elif i == 'y':
#         k += 3
#     else:
#         k += 4
# print(k)                                                                                         

#梦中的统计
# a,b = map(int,input('请输入:').split())
# c,d,e,f,g,h,k,l,m,n=0,0,0,0,0,0,0,0,0,0
# for i in range(a,b+1):
#     for q in str(i):
#         if q == '0':
#             c += 1
#         elif q == '1':
#             d += 1  
#         elif q == '2':
#             e += 1  
#         elif q == '3':
#             f += 1  
#         elif q == '4':
#             g += 1  
#         elif q == '5':
#             h += 1  
#         elif q == '6':
#             k += 1  
#         elif q == '7':
#             l += 1  
#         elif q == '8':
#             m += 1  
#         else:
#             n += 1  
# print('{} {} {} {} {} {} {} {} {} {}'.format(c,d,e,f,g,h,k,l,m,n),end='')

#显示屏
# digits = [
#     ["XXX", "X.X", "X.X", "X.X", "XXX"],  
#     ["..X", "..X", "..X", "..X", "..X"],  
#     ["XXX", "..X", "XXX", "X..", "XXX"],  
#     ["XXX", "..X", "XXX", "..X", "XXX"], 
#     ["X.X", "X.X", "XXX", "..X", "..X"],  
#     ["XXX", "X..", "XXX", "..X", "XXX"],  
#     ["XXX", "X..", "XXX", "X.X", "XXX"],  
#     ["XXX", "..X", "..X", "..X", "..X"],  
#     ["XXX", "X.X", "XXX", "X.X", "XXX"],  
#     ["XXX", "X.X", "XXX", "..X", "XXX"]   
# ]
# n = int(input('请输入数字的个数:'))
# number_str = input('请输入自然数:').strip()
# screen = [['.' for _ in range(5 * n + n - 1)] for _ in range(5)]
# for i, digit in enumerate(number_str):
#     digit_matrix = digits[int(digit)]
#     for row in range(5):  # 遍历点阵的每一行
#         for col in range(len(digit_matrix[row])):  # 使用len()来确保不会超出字符串长度
#             if digit_matrix[row][col] == 'X':
#                 screen[row][i * 6 + col] = 'X'  # 注意：这里假设每个数字占6列（5列显示+1列间隔）
# for row in screen:
#     print(''.join(row))

# digits = [
#     ["XXX", "X.X", "X.X", "X.X", "XXX"],  #0
#     ["..X", "..X", "..X", "..X", "..X"],  #1
#     ["XXX", "..X", "XXX", "X..", "XXX"],  
#     ["XXX", "..X", "XXX", "..X", "XXX"], 
#     ["X.X", "X.X", "XXX", "..X", "..X"],  
#     ["XXX", "X..", "XXX", "..X", "XXX"],  
#     ["XXX", "X..", "XXX", "X.X", "XXX"],  
#     ["XXX", "..X", "..X", "..X", "..X"],  
#     ["XXX", "X.X", "XXX", "X.X", "XXX"],  
#     ["XXX", "X.X", "XXX", "..X", "XXX"]   
# ]
# n = int(input('请输入:'))
# number_str = input('请输入自然数:').strip()
# screen = [['.' for _ in range(3 * n + n - 1)] for _ in range(5)]
# for i, digit in enumerate(number_str):
#     digit_matrix = digits[int(digit)]
#     for row in range(5):  
#         for col in range(len(digit_matrix[row])): 
#             if digit_matrix[row][col] == 'X':
#                 screen[row][i * 4 + col] = 'X' 
# for row in screen:
#     print(''.join(row))

#珠心算测验
# def count_pairs_with_sum_in_set(n, numbers):
#     # 将数字存储到集合中，以便快速查找
#     num_set = set(numbers)
#     count = 0
#     # 遍历每对不同的数字
#     for i in range(n):
#         for j in range(i + 1, n):
#             # 计算两个数字的和
#             total = numbers[i] + numbers[j]
#             # 检查和是否在集合中
#             if total in num_set and total != numbers[i] and total != numbers[j]:
#                 count += 1
#     return count
# # 读取输入
# n = int(input().strip())
# numbers = list(map(int, input().strip().split()))
# result = count_pairs_with_sum_in_set(n, numbers)
# print(result)
      
# def A(n, numbers):
#     a = set(numbers)
#     l = 0
#     for i in range(n):
#         for k in range(i+1,n):
#             tt = numbers[i] + numbers[k]
#             if tt in a and tt != numbers[i] and tt != numbers[k]:
#                 l += 1
#     return l            
# n = int(input().strip())
# numbers = list(map(int, input().strip().split()))
# result = A(n, numbers)
# print(result)

#爱与愁的心痛
# n,m = map(int,input('请输入:').split())
# A = []
# for _ in range(n):
#     a = int(input('请输入:'))
#     A.append(a)
   
# B = []
# for i in range(len(A)):
#     if (i+2) == len(A):
#         continue
#     else:
#         A = str(A)    
#         c = int(A[i]) + int(A[i+1]) + int(A[i+2])
#         B.append(c)
# print(B)         

# n, m = map(int, input().split())
# A = []
# for _ in range(n):
#     a = int(input())
#     A.append(a)
# B = []
# for i in range(len(A) - 2): 
#     c = A[i] + A[i + 1] + A[i + 2]
#     B.append(c)
# v = min(B)
# print(v)

#开灯
# import math
# n = int(input())
# A = []
# for _ in range(n):
#     a = input().split()
#     A.append([float(a[0]),int(a[1])])  
# c = [i[0] for i in A]
# m = [i[1] for i in A]
# m = [str(i) for i in m]
# k = []
# for o,i in enumerate(c):
#     for l in range(1,int(m[o])+1):
#         q = i * l
#         q = math.floor(q) 
#         k.append(q)          
# char_map = {}
# for char in k:
#     if char in char_map:
#         char_map[char] += 1
#     else:
#         char_map[char] = 1
# for key, val in char_map.items():
#     if val % 2 != 0:
#         print('{}'.format(key)) 

#小书童——凯撒密码
# n = int(input('请输入:'))
# a = input('请输入:')
# b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# m = []
# for i,val in enumerate(b):
#     for k in a:
#         if k in val:
#             k = b[i+n]
#             m.append(k)
# m = [i.join()for i in m]
# print(m)

# n = int(input('请输入移动位数: '))
# a = input('请输入字符串: ')
# b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# m = []
# for i in a:
#     if i.islower():
#         index = b.index(i)
#         new_index = (index + n) % 26
#         m.append(b[new_index])
# print(''.join(m)) 

#笨小猴
# a = input('请输入:')
# m = {}
# for i in a:
#     if i in m:
#         m[i] += 1
#     else:
#         m[i] = 1
# b = []        
# for i,k in m.items():
#      b.append(k)
# maxn = max(b)
# minn = min(b)
# c = maxn - minn
# if c == 0:
#     print('No Answer')
#     print(0)    
# elif c == 2:
#     print('Lucky Word')
#     print(c)     
# elif c % 2 !=0:
#     for j in range(2,int(maxn)+1):
#         for k in range(2,int(maxn)+1):
#             if c != j * k :
#                 print('Lucky Word')
#                 print(c)
# else:
#     print('No Answer')     
#     print(0)           

#口算练习题
# n = int(input('请输入:'))
# A = []
# for _ in range(n):
#     line = input('请输入:').split()
#     if len(line) ==2 :
#         A.append([line[0],line[1]])
#     else:             
#         A.append([line[0],line[1],line[2]])
# a = '+'
# b ='-'
# c ='*'
# for i in A:
#     if len(i) == 2:
#         m = int(i[0])+int(i[1])
#         print('{}+{}={}'.format(int(i[0]),int(i[1]),m))
#         l = 0
#         for k in i:
#             l += len(str(k))
#         print(l+len(str(m))+2)  
#     if len(i) != 2:
#         if 'a' in i:
#             m = int(i[1])+int(i[2])
#             print('{}+{}={}'.format(int(i[1]),int(i[2]),m))
#             l = 0
#             for k in i:
#                 l += len(str(k))
#             print(l+len(str(m))+1)  
#         elif 'b' in i:
#             m = int(i[1])-int(i[2])
#             print('{}-{}={}'.format(int(i[1]),int(i[2]),m))
#             l = 0
#             for k in i:
#                 l += len(str(k))
#             print(l+len(str(m))+1) 
#         if 'c' in i:
#             m = int(i[1])*int(i[2])
#             print('{}*{}={}'.format(int(i[1]),int(i[2]),m))
#             l = 0
#             for k in i:
#                 l += len(str(k))
#             print(l+len(str(m))+1)               

#标题统计
# s = input('请输入:')
# a = 0
# for i in s:
#     if i == ' ':
#         continue
#     else:
#         a += 1
# print(a)


#文字处理软件
# q = int(input('请输入数字:'))
# a = input('请输入:')

# while q:
#     b = list(input('请输入:').split())
#     if int(b[0]) == 1:
#         a = a + b[2:]
#         print(a)
#     elif int(b[0]) == 2:
#         m,n = int(b[2]),int(b[4])
#         a = a[m:m+n]
#         print(a)
#     elif int(b[0]) == 3:
#         m = int(b[2])
#         a = a[0:m] + b[4:] + a[m:]
#         print(a)
#     # else:
            
             
            
    # n = int(input('请输入：'))
    # if n == 1:
    #     b = input('请输入要接入的东西:')
    #     a.join(b)
    #     print(a)
    # elif n ==2:
    #     a,b = map(int,input('请输入区间:'))
    #     m = a[a:a+b]
    #     print(m)
    # elif n ==3:
    #     c = int(input('请输入:'))
    #     l = input('请输入:')
    #     p = m[0:c] + l + m[c:]
    #     print(p)
    # else:
    #     a = input('请输入:')
    #     if a in p:
    #         l = len(a)
    #         i= 0
    #         for i in p:
    #             i += 1
    #             if p[i:i+l+1] == 'a':
    #                 print(i)

#评测机队列
# m1, t1 = 8, 30
# m2, t2 = 10, 6
# t3 = 10
# r = (m1 * t1 - m2 * t2) / (t1 - t2)
# V = m1 * t1 - r * t1
# x = (V + r * t3) / t3
# print(int(x))

# 清扫教室
# ren = 3
# fangzi = 3
# t = 3
# x = fangzi/(ren*t)
# y = 9*9*x
# print(int(y))

#竞赛得分
# zong = 240
# ji = 2.4
# fen = 240/2.4
# x = int(1.4 * fen)  
# y = int(fen)
# print('{} {}'.format(x,y))

# A = 35
# B = 47
# x = int(B - A)
# y = int(2*A - B)
# print('{} {}'.format(x,y)) 

# A,B = 10000,10000
# A1 = A*1.035**5
# Ab = round(A1,1)
# A2 = int(B*(1+5*0.04))
# print('{} {}'.format(Ab,A2))           

#跑步
# from sympy import symbols,Eq,solve
# t = symbols('t')
# e1 = Eq(8*t,5*t+100)
# s = solve((e1),(t),dict=True)
# a = s[0][t]
# print(int(a))

# A = 5
# B = 8
# s = 100
# t = s/(B-A)
# t = round(t,1)
# print(t)

#英文字母
# A = 'abcdefghigklmnopqrstuvwxyz'
# A = A.upper()
# a = 0
# for i in A:
#     a += 1
#     if i == 'M':
#         print(a)
# print(A[17])        

#数字反转
# A = input('请输入：')
# B = A[::-1]
# print(B)

#再分肥宅水
# a = input('请输入:').split()
# t = float(a[0])
# n = int(a[1])
# hnags = t/n
# hnags = round(hnags,3)
# beiiz = 2*n
# print(hnags)
# print(beiiz)

#小鱼的游泳时间
# a,b,c,d = map(int,input('请输入:').split())
# t = (c*60+d)-(a*60+b)
# z = t//60
# x = t%60
# print('{} {}'.format(z,x))

#上学迟到
# s,v = map(int,input('请输入:').split())
# t = s/v
# if t != int(t):
#     t = int(t) + 1
# h = 8*60 - t-10
# if h> 0:
#     a = str(h//60)
#     b = str(h %60)
#     if len(a) ==2 and len(b) == 2:
#         print('{}:{}'.format(a,b))
#     elif len(a) == 2 and len(b) ==1:
#         print('{}:0{}'.format(a,b))
#     elif len(a) == 1 and len(b) ==2:  
#         print('0{}:{}'.format(a,b)) 
#     else:
#         print('0{}:0{}'.format(a,b))   
# else:
#     m = t+10 - 8*60
#     h = 24*60 - m
#     a = int(h//60)
#     b = int(h %60)
#     print(f'{a:02}:{b:02}')

# n (n-1) (n-2) * (n-3) / 24
# n = int(input('请输入:'))
# s =  (n*(n-1)*(n-2) * (n-3) )/ 24
# print(int(s))


#数的性质
# n = int(input('请输入:'))
# a = 0
# b = 0
# c = 0
# d = 0
# if n %2 ==0 and 4< n <= 12:
#     a = 1
# elif n %2 ==0 or (4< n <= 12):
#     b = 1
# elif n %2 !=0 and (n<=4 or n > 12):
#     d = 1
# else:
#     c = 1    
# print('{} {} {} {}'.format(a,b,d,c))    

# x = int(input(''))
# m = x % 2 == 0  
# p = 4 < x <= 12 
# a = 1 if m and p else 0
# uim = 1 if m or p else 0
# yong = 1 if (m and not p) or (not m and p) else 0
# zhengmei = 1 if not m and not p else 0
# print(a, uim, yong, zhengmei)1

#闰年判断
# year = int(input(''))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(1)
# else:
#     print(0)  
    
#apple
# n = int(input('请输入:'))
# if n == 1:
#     print('Today, I ate {} apple.'.format(n))
# else:
#     print('Today, I ate {} apples.'.format(n))    
    
#排序
# a,b,c = map(int,input('请输入:').split())
# m = [a,b,c]
# m.sort()
# print(m[0], m[1], m[2])

#月份天数
# year,m = map(int,input('请输入:').split())
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     print(month_days[m-1])
# else:
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     print(month_days[m-1])     

#不高兴的津津
# m = []
# for _ in range(7):
#     a= input('请输入:').split()
#     m.append([int(a[0]),int(a[1])])
# l = []
# for i in  m:
#     k = 0
#     k = int(i[0])+ int(i[1])
#     l.append(k)
# p = sorted(l)
# u = 0
# y = []
# if int(p[6]) <=8:
#     print(0)
# else:
#     for i in l:
#         if int(i) > 8:
#             y.append(i)
# h = len(y)
# for i in range(h):
#     if int(y[i]) == int(y[i+1]):
                 
    # for i in l:
    #     u += 1
    #     if int(i) == int(p[6]):
    #         print(u)    
       
        
# 输入7天的日程安排
# m = []
# for _ in range(7):
#     a = input('请输入: ').split()
#     m.append([int(a[0]), int(a[1])])

# # 计算每天的总上课时间
# l = []
# for i in m:
#     k = i[0] + i[1]
#     l.append(k)
# print(l)
# # 找出最不高兴的一天
# max_unhappiness = 0
# unhappy_day = 0

# for i in range(7):
#     if l[i] > 8 and l[i] > max_unhappiness:
#         max_unhappiness = l[i]
#         unhappy_day = i + 1  # 从1开始计数

# # 输出结果
# if max_unhappiness == 0:
#     print(0)
# else:
#     print(unhappy_day)

#买铅笔
# n = int(input('请输入:'))
# k = []
# for _ in range(3):
#     a,b = map(int,input('请输入:').split())
#     s = n / a
#     if s != int(s):
#         m = (int(s)+1)*b
#         k.append(m)
#     else:
#         m = int(s)*b
#         k.append(m)
# print(min(k))        
            
# ISBN 号码
# isn = input('请输入:')
# isn1 = isn[0:1]+isn[2:5]+isn[6:11]
# s = sum([(i+1)*int(v) for i,v in enumerate(isn1)]) % 11
# if s == 10:
#     x ='X'
# if str(s) == isn[-1]:
#     print('Right')
# else:
#     print(isn[:-1]+f'{x}')

#小鱼的航程（改进版）
# x,n = map(int,input('请输入:').split())
# k = [i for i in range(x,x+n)]
# if 6 in k  and  7 not in  k:
#     l = 250*(n-1)
#     print(l)
# elif  6 in  k and 7 in  k:
#     l = 250 *(n-2)
#     print(l)
# elif 6 not in k and 7 not in k:
#     l = 250 * n
#     print(l)


# x, n = map(int, input('请输入: ').split())
# a = 0
# for i in range(n):
#     current_day = (x + i - 1) % 7 + 1
#     if 1 <= current_day <= 5:
#         a += 1
# b = a * 250
# print(b)

#三角函数
# a,b,c = map(int,input('请输入Z:').split())
# k = [a,b,c]
# l = max(k)
# p = min(k)
# print('{}/{}'.format(p,l))

#陶陶摘苹果
# a = input('请输入:').split()
# c = int(input('请输入:'))
# n = 0 
# for i in a:
#     if (c+30) >= int(i):
#         n += 1
# print(n)        


#找最小值
# n = int(input('请输入:'))
# a = map(int,input('请输入:').split())
# a = [i for i in a]
# print(min(a))    

#分类平均
# n,k = map(int,input('请输入:').split())
# a = []
# b = []
# for i in range(1,n+1):
#     if i % k==0:
#         a.append(i)
#     else:
#         b.append(i)
# a = sum([i for i in a]) / len(a)
# b = sum([i for i in b]) / len(b)
# print('{:.1f} {:.1f}'.format(a,b))
            

#一尺之棰
# def A(n,a):
#     a += 1
#     n = n /2
#     if n <= 1:
#         return a
#     else:
#         return A(n,a)
# n = int(input('请输入:'))
# print(A(n,0))

#[NOIP1998 普及组] 阶乘之和
# n = int(input('请输入:'))
# b = 0
# for j in range(1,n+1):
#     a = 1
#     for i in range(1,j+1):
#         a = a*i
#     b = b + a    
# print(b)    

#[NOIP2002 普及组] 级数求和
# k = int(input('请输入:'))
# while True:
#     n = 1
#     if n> k:
#         print(n)
#     else:
#         n = n+1
#         h = 1
#         h = h+1/int(n)
#         if h > k:
#             print(n)
            
# k = input()
# k = int(k)
# s = 0
# n = 1
# while True:
#         s += 1/int(n)
#         if s > k:
#             print(n)
#             break
#         n += 1

#[NOIP2015 普及组] 金币
# def A(days):
#     m = 0 
#     n = 1 
#     guoqudesj = 0 
#     for day in range(1,days+1):
#         m += n
#         guoqudesj +=  1
#         if guoqudesj == n:
#             n += 1
#             guoqudesj = 0
#     return m        
        
# days = int(input())
# print(A(days))

# import math
# k = int(input())
# m = int((math.sqrt(1 + 8 * k) - 1) // 2)
# sum_sq = m * (m + 1) * (2 * m + 1) // 6
# remaining_days = k - m * (m + 1) // 2
# total = sum_sq + remaining_days * (m + 1)
# print(total)

# def A(k):
#     n = 1
#     m = 0
#     jieduan = 0
#     for i in range(1,k+1):
#         m += n
#         jieduan += 1
#         if jieduan == n:
#             n += 1
#             jieduan = 0
#     return m
# k = int(input('请输入:'))
# print(A(k))
#【深基4.例13】质数口袋
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# L = int(input('请输入承重量 L: '))
# primes = []
# while True:
#     n = 1
#     n += 1
#     if is_prime(n):
#         primes.append(n)
#     a = 0
#     for i in primes:
#         a += i
#         if a <= L:
#             print(n)
#     break
# for prime in primes:
#     print(prime)
# # 输出质数的个数
# print(len(primes))

# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     max_divisor = int(n ** 0.5) + 1
#     for d in range(3, max_divisor, 2):
#         if n % d == 0:
#             return False
#     return True


# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# L = int(input())
# sum_primes = 0
# primes = []
# n = 2

# while True:
#     if is_prime(n):
#         if sum_primes + n > L:
#             break
#         primes.append(n)
#         sum_primes += n
#     n += 1

# for p in primes:
#     print(p)
# print(len(primes))

#[USACO1.5] 回文质数 Prime Palindromes
# def A(num):
#     if num <= 1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True
# a,b = map(int,input('请输入:').split())
# l = []
# for i in range(a,b+1):
#     if str(i) == str(i)[::-1]:
#         l.append(i)
# k = []
# for i in l:
#     if A(i):
#         k.append(i)
# for i in k:
#     print(i)             

#小玉在游泳
# s = float(input('请输入:'))
# a = 0
# n = 2
# w = 0
# while w < s:
#     w += n
#     a += 1
#     n *= 0.98
# print(a)

#[NOIP2011 普及组] 数字反转
# N = input('请输入:')
# if int(N) > 0:
#     a = N[::-1]
#     b = a.lstrip('0')
#     print(b)
# else:
#     a = N[0]
#     b = N[1::]
#     c = b[::-1].lstrip('0')
#     d = a + c
#     print(d)    


#最长连号
# n = int(input('请输入:'))
# a = input('请输入:').split()
# m = 0
# k = []
# for i in range(1,n):
#     if int(a[i]) == (int(a[i-1]) +1):
#         m += 1
#     k.append(m)
# print(k)    

# n = int(input('请输入数字个数:'))
# a = list(map(int, input('请输入数字序列（空格分隔）:').split()))
# m = 1  # 从第一个数字开始，每个数字至少自成一个序列
# k = []

# for i in range(1, n):
#     if a[i] == a[i-1] + 1:
#         m += 1  # 如果递增，则增加当前序列的长度
#     else:
#         k.append(m)  # 记录当前序列长度，并重置m为下一个序列的开始
#         m = 1
# k.append(m)
# print(max(k))

#[NOIP2012 普及组] 质因数分解
# n = int(input('请输入:'))
# def A(num):
#     if n <= 1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True
# a = 2
# bv = []
# while True:
#     if A(a):
#         b = int(n/a)
#         if A(b):
#             print(max(a, b))  # 直接输出较大的质数，这里a和b中必有一个是较大的
#             break
#     a += 1      


#【深基4.习9】打分
# n = int(input('请输入:'))
# k = list(map(int,input('请输入:').split()))
# k.sort()
# a = k[1:-1]
# x = sum([i for i in a])/len(a)
# x = round(x,2)
# print(x)

#[COCI2017-2018#6] 达沃
# N = int(input('请输入:'))
# k = 1
# m = []
# p = []
# while True:
#     x = 1
#     for i in range(1,101):
#         if ((7*i+21*k)*52) == N:
#             m.append(i)
#             p.append(k)
#             break
#         x += 1
#     k += 1

# N = int(input('请输入: '))

# # 检查N是否能被52整除
# if N % 52 != 0:
#     print("无解")
# else:
#     S = N // 52
#     # 检查S是否能被7整除
#     if S % 7 != 0:
#         print("无解")
#     else:
#         M = S // 7
#         max_x = -1
#         best_k = -1
#         # 计算k的最大可能值
#         k_max = (M - 1) // 3
#         # 遍历k的可能值
#         for k in range(1, k_max + 1):
#             x = M - 3 * k
#             if 1 <= x <= 100:
#                 # 更新最优解
#                 if x > max_x or (x == max_x and k < best_k):
#                     max_x = x
#                     best_k = k
#         if max_x == -1:
#             print("无解")
#         else:
#             print(f"x={max_x}, k={best_k}")

#[NOIP2004 提高组]:津津的储蓄计划
# b = []
# for _ in range(12):
#     a = int(input('请输入:'))
#     b.append(a)
# shouzhong = 0
# mamamn = 0
# yuanlai = 300
# a = 0
# for i in b:
#     a += 1
#     shouzhong += yuanlai
#     shouzhong -= int(i)
#     if shouzhong >= 100:
#         l = (shouzhong // 100)*100
#         mamamn += l
#         shouzhong = shouzhong -l
#     if shouzhong < 0:
#         print('-{}'.format(a))
#         break
# mamamn = mamamn*(1+0.2)
# cumk = shouzhong + mamamn 
# if shouzhong >= 0:
#     print(int(cumk))

#【深基5.例1】小鱼比可爱
# n = int(input())
# a = input().split()
# for i in range(0,len(a)):
#     m =0
#     for j in range(0,i):
#         if a[i] > a[j]:
#             m += 1
#     print('{}'.format(m),end=' ')

#【深基5.例2】小鱼的数字游戏
# n = list(map(int,input('请输入:').split()))
# n = n[:-1]
# v = n[::-1]
# for i in v:
#     print('{}'.format(i),end=' ')

#【深基5.例3】冰雹猜想

# def A(n,b):
#     if n == 1:
#         return b
#     if n % 2 ==1:
#         n = n*3+1
#     else:  
#         a = n //2
#         b.append(a)
#         n = a
#     return A(n,b)    
# n = int(input(''))
# result_path = A(n, [n]) 
# result_path = result_path[::-1]
# for num in result_path:
#     print(num, end=' ')

# def A(n, b=None):
#     if b is None:
#         b = []  # 只在首次调用时初始化列表
#     if n == 1:
#         return b
#     if n % 2 == 1:
#         return A(n * 3 + 1, b + [n * 3 + 1])  # 对于奇数，直接计算下一个值并添加到列表中（但这里不直接添加到 b，而是添加到新列表中传递给下一次递归）
#     else:
#         return A(n // 2, b + [n // 2]) 

# # 获取用户输入
# n = int(input('请输入:'))

# # 计算完整路径（传入空列表作为初始值）
# result_path = A(n)  # 由于 b 有默认值 None，所以这里可以直接调用 A(n)

# # 打印结果
# for num in result_path:
#     print(num, end=' ')
# print()

#[NOIP2005 普及组] 校门外的树
# l,m = map(int,input('请输入:').split())
# qujian = []
# for _ in range(m):
#     a = input('请输入:').split()
#     qujian.append([int(a[0]),int(a[1])])
# qujian.sort(key=lambda x :x[0])
# u = []
# v = []
# for row in qujian:
#     u.append(row[0])
#     v.append(row[1])      
# a = 0
# b = 0
# for i in ra

# l, m = map(int, input().split())
# A = []
# for _ in range(m):
#     u, v = map(int, input().split())
#     A.append((u, v))
# # 合并重叠区域
# merged_regions = []
# A.sort()  # 确保列表已按起始点排序
# current_start, current_end = A[0]
# for start, end in A[1:]:
#     if start <= current_end:
#         current_end = max(current_end, end)
#     else:
#         merged_regions.append((current_start, current_end))
#         current_start, current_end = start, end
# merged_regions.append((current_start, current_end))
# # 计算被移除的树的数量
# trees_removed = 0
# for start, end in merged_regions:
#     trees_removed += end - start + 1
# # 计算剩余的树的数量
# total_trees = l + 1  # 包括0到l的所有整数点
# remaining_trees = total_trees - trees_removed
# print(remaining_trees)


# l, m = map(int, input().split())
# A = []
# for _ in range(m):
#     u, v = map(int, input().split())
#     A.append((u, v))
# A.sort()
# chonghe = []
# stard_1,end_1 = A[0]
# for stard,end in A[1:]:
#     if stard <= end_1:
#         end_1 = max(end_1,end)    
#     else:
#         chonghe.append((stard_1,end_1))
#         stard_1,end_1 = stard,end
# chonghe.append((stard_1,end_1)) 
# trees = 0
# for stard,end in chonghe:
#     trees += end-stard+1
# tool = l +1
# shengyu = tool - trees
# print(shengyu)

#【深基5.例5】旗鼓相当的对手
# N = int(input('请输入:'))
# A = []
# for _ in range(N):
#     u,v,w = map(int,input('请输入:').split())
#     A.append((u,v,w))
# a = A[0]
# m = 0
# x = sum([i for i in a])
# for i in A[1:]:
#     y = sum([k for k in i])
#     for j in range(3):
#         if a[j] - i[j] <= 5:
#             if abs(y - x) <= 10:
#                 m += 1
#                 break
#         x = y
#         a = i     
# print(m)               

# N = int(input('请输入:'))
# A = []
# for _ in range(N):
#     u, v, w = map(int, input('请输入:').split())
#     A.append((u, v, w))

# m = 0
# for i in range(N):
#     a = A[i]
#     x = sum(a)
#     for j in range(i + 1, N):
#         b = A[j]
#         y = sum(b)
#         is_rival = True
#         for k in range(3):
#             if abs(a[k] - b[k]) > 5:
#                 is_rival = False
#                 break
#         if is_rival and abs(y - x) <= 10:
#             m += 1

# print(m)

# #
# n = int(input())
# zhong = list(map(int, input().split()))
# A = []
# for _ in range(n):
#     line = list(map(int, input().split()))
#     A.append(line)
# coun = []
# for row in A:
#     counte = sum(1 for num in row if num in zhong)
#     coun.append(counte)
# t = 0
# yi = 0
# er = 0
# san = 0
# si = 0
# wu = 0
# liu = 0
# for i in coun:
#     if i == 1:
#         liu += 1
#     elif i == 2:
#         wu += 1
#     elif i == 3:
#         si += 1
#     elif i == 4:
#         san += 1
#     elif i == 5:
#         er += 1
#     elif i == 6:
#         yi += 1
#     elif i == 7:
#         t += 1
#     else:
#         print('{} {} {} {} {} {} {}'.format(t,yi,er,san,si,wu,liu))      
# print('{} {} {} {} {} {} {}'.format(t,yi,er,san,si,wu,liu))


#[NOIP2015 提高组] 神奇的幻方
# def generate_magic_square(N):
#     magic_square = [[0] * N for _ in range(N)]
#     num = 1  
#     i, j = 0, N // 2  
#     while num <= N * N:
#         magic_square[i][j] = num  
#         new_i, new_j = (i - 1) % N, (j + 1) % N 
#         if magic_square[new_i][new_j] != 0:  
#             new_i, new_j = (i + 1) % N, j  
#         i, j = new_i, new_j
#         num += 1
#     return magic_square
# def main():
#     while True:
#         try:
#             N = int(input())
#             if 1 <= N <= 39 and N % 2 != 0:
#                 break
#             else:
#                 print()
#         except ValueError:
#             print()
#     magic_square = generate_magic_square(N)
#     for row in magic_square:
#         print(" ".join(map(str, row)))
# if __name__ == "__main__":
#     main()

# n = int(input('请输入:'))
# A = []
# for _ in range(n):
#     row = []
#     for i in range(n):
#         a = 1
#         row.append(a)
#     A.append(row) 
# a,b = 0,n//2
# A[a][b] = 1
# for i in range(2,n*n+1):
#     pre_a,pre_b = a,b
#     if pre_a==0 and pre_b!= (n-1):
#         a = n-1
#         b = pre_b + 1
            
#     elif pre_a != 0 and pre_b == (n-1):
#         a = pre_a -1
#         b = 0
#     elif pre_a == 0 and pre_b == (n-1): 
#         a = pre_a + 1
#         b = pre_b
#     else:
#         next_row = (pre_a- 1) % n
#         next_col = (pre_b + 1) % n
#         if A[next_row][next_col] == 0:
#             a, b = next_row, next_col
#         else:
#             a = (pre_a + 1) % n
#             b = pre_b

#     A[a][b] = i
# for i in A:
#     print(' '.join(map(str,i)))   


# n = int(input('请输入奇数N：'))
# magic_square = [[0] * n for _ in range(n)]

# # 初始化第一个数字的位置
# row, col = 0, n // 2
# magic_square[row][col] = 1

# for k in range(2, n*n+1):
#     # 保存当前位置
#     prev_row, prev_col = row, col
    
#     # 尝试右上方移动
#     row = (row - 1) % n
#     col = (col + 1) % n
    
#     # 检查右上方是否已被占用
#     if magic_square[row][col] != 0:
#         # 如果被占用则回退并下移
#         row = (prev_row + 1) % n
#         col = prev_col
    
#     magic_square[row][col] = k

# # 打印幻方
# for r in magic_square:
#     print(' '.join(map(str, r)))


# n = int(input('请输入:'))
# A = []
# for _ in range(n):
#     row = []
#     for _ in range(n):
#         a = 0
#         row.append(a)
#     A.append(row)
# a,b = 0,n//2
# A[a][b] = 1
# for i in range(2,n*n+1):
    
# n = int(input(''))
# magic_square = [[0] * n for _ in range(n)]

# row, col = 0, n // 2
# magic_square[row][col] = 1

# for k in range(2, n*n+1):
#     prev_row, prev_col = row, col
#     row = (row - 1) % n
#     col = (col + 1) % n
#     if magic_square[row][col] != 0:
#         row = (prev_row + 1) % n
#         col = prev_col
#     magic_square[row][col] = k
# for r in magic_square:
#     print(' '.join(map(str, r)))


# n = int(input('请输入:'))
# A = []
# for _ in range(n):
#     row = []
#     for i in range(n):
#         a = 0
#         row.append(a)
#     A.append(row) 
# a,b = 0,n//2
# A[a][b] = 1
# for i in range(2,n*n+1):
#     pre_a,pre_b = a,b
#     if pre_a == 0 and pre_b!= (n-1):
#         a = n-1
#         b = pre_b + 1
#     elif pre_a != 0 and pre_b == (n-1):
#         a = pre_a -1
#         b = 0
#     elif pre_a == 0 and pre_b == (n-1): 
#         a = pre_a + 1
#         b = pre_b
#     else:
#         next_row = (pre_a- 1) % n
#         next_col = (pre_b + 1) % n
#         if A[next_row][next_col] == 0:
#             a, b = next_row, next_col
#         else:
#             a = (pre_a + 1) % n
#             b = pre_b
#     A[a][b] = i
# for i in A:
#     print(' '.join(map(str,i)))  

#【深基5.例10】显示屏e
# digits = [
#     ["XXX", "X.X", "X.X", "X.X", "XXX"], 
#     ["..X", "..X", "..X", "..X", "..X"],  
#     ["XXX", "..X", "XXX", "X..", "XXX"],  
#     ["XXX", "..X", "XXX", "..X", "XXX"], 
#     ["X.X", "X.X", "XXX", "..X", "..X"],  
#     ["XXX", "X..", "XXX", "..X", "XXX"],  
#     ["XXX", "X..", "XXX", "X.X", "XXX"],  
#     ["XXX", "..X", "..X", "..X", "..X"],  
#     ["XXX", "X.X", "XXX", "X.X", "XXX"],  
#     ["XXX", "X.X", "XXX", "..X", "XXX"] ]
# n = int(input('请输入:'))
# a = input('请输入:')
# p = [""] * 5
# b = 0
# for i in a:
#     b += 1
#     if b != n: 
#         m = digits[int(i)]
#         for j in range(5):
#             p[j] += m[j] + '.'
#     else:
#         m = digits[int(i)]
#         for j in range(5):
#             p[j] += m[j]   
# for i in p:
#     print(''.join(map(str,i))) 


#[NOIP2014 普及组] 珠心算测验
# n = int(input('请输入:'))
# x = list(map(int,input('请输入:').split()))
# x.sort()
# a = 0
# for i in range(n):
#     for j in x[i+1:]:
#         for m in x[i+2:]:
#             if x[i] + j == m:
#                 a += 1
# print(a)                

# n = int(input('请输入:'))
# x = list(map(int, input('请输入:').split()))
# x.sort()
# sum_set = set()
# for i in range(n):
#     for j in range(i + 1, n):
#         sum_set.add(x[i] + x[j])          
# a = 0
# for num in x:
#     if num in sum_set:
#         a += 1
# print(a)

#【深基5.习3】爱与愁的心痛
# n,m = map(int,input('请输入:').split())
# A = []
# for _ in range(n):
#     a = int(input('请输入:'))
#     A.append(a) 
# suma= []
# k = 0
# for i in range(n-m):
#      B = sum(A[i:i+m])
#      suma.append(B)
# print(suma)     
# # print(min(suma))            

#深基5.习5】开灯
# n = int(input('请输入:'))
# A = []
# B = []
# for _ in range(n):
#     a,t = map(float,input('请输入:').split())
#     t = int(t)
#     A.append(a)
#     B.append(t)
# k = []
# a = 0
# for m in A:
#     a += 1
#     for i in range(1,B[a-1]+1):
#         l = int(m*i)
#         k.append(l)
# q = dict()          
# for i in k:
#     if i in q:
#         q[i] += 1
#     else:
#         q[i] = 1
# for i,v in q.items():
#     if v % 2 != 0:
#         print('{}'.format(i))


#【深基5.习6】蛇形方阵
# n = int(input('请输入:'))
# A = []
# for i in range(n):
#     l = []
#     for j in range(n):
#         a = 0
#         l.append(a)
#     A.append(l)
# a = 1
# for i in A:
#     for j in range(n):
#         i[j] += a 
#         a += 1
#     a = a
# 定义方向：右、下、左、上
# fangxiang = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# today = 0  # 当前方向索引
# x, y = 0, 0  # 当前位置
# for i in range(1,n*n+1):
#     A[x][y] = i
#     # 计算下一个位置
#     next_x = x + fangxiang[today][0]
#     next_y = y + fangxiang[today][1]
#     # 检查下一个位置是否合法
#     if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n or A[next_x][next_y] != 0:
#         today = (today + 1) % 4  # 切换方向
#         next_x = x + fangxiang[today][0]
#         next_y = y + fangxiang[today][1]
#     x, y = next_x, next_y  # 更新当前位置
# for row in A:
#     m = [f'{num:3d}' for num in row]
#     print(''.join(m))    


#【深基5.习7】杨辉三角
# n = int(input('请输入:'))
# A = []
# for i in range(n):
#     a = []
#     for j in range(i+1):
#         b = 0
#         a.append(b)
#     A.append(a)
# x,y = 0,0
# A[x][y] = 1
# for i in range(1,n):
#     A[i][0] = 1
#     A[i][i] = 1
#     if i >= 2:
#         for j in range(1,i):
#             A[i][j] = A[i-1][j-1]+ A[i-1][j]
# for i in A:
#     print(' '.join(map(str,i)))           


#【深基5.习9】压缩技术
# A = list(map(int,input('请输入:').split()))
# B = []
# for i in range(A[0]):
#     b = []
#     for j in range(A[0]):
#         l = 1
#         b.append(l)
#     B.append(b)
# x,y = 0,0
# for l,v in enumerate(A[1:]):
#     if l % 2 == 0:
#         B[x][y] = 0
#         for k in range(v):
#             next_x = x
#             next_y = y + k
#             if next_x >= A[0] or next_x < 0 or next_y >= A[0] or next_y < 0:
#                 next_x += 1
#                 next_y = y
#             x,y = next_x,next_y           
#     else:
#         B[x][y] = 1
#         for j in range(v):
#             next_x = x
#             next_y = y + j
#             if next_x >= A[0] or next_x < 0 or next_y >= A[0] or next_y < 0:
#                 next_x += 1
#                 next_y = y
#             x,y = next_x,next_y              
# for i in B:
#     print(' '.join(map(str,i)))

# A = list(map(int, input('请输入:').split()))
# N = A[0]
# n = A[1:]
# B = []
# for i in range(A[0]):
#     b = []
#     for j in range(A[0]):
#         l = 1
#         b.append(l)
#     B.append(b)
# x, y = 0, 0
# fill_with_one = False 
# for code in n:
#     fill_value = 1 if fill_with_one else 0
#     for i in range(code):
#         B[x][y] = fill_value
#         y += 1 
#         if y == N:
#             y = 0  
#             x += 1  
#             if x == N:
#                 break
#     fill_with_one = not fill_with_one
# for row in B:
#     print(' '.join(map(str, row)))
#【深基2.例4】销量预测
# a = 110
# n = 10
# w = 3500
# A = []
# for i in range(1,1000):
#     if w == (a-i)*(n+i):
#         b = a-i
#         A.append(b)
# for i in range(1,1000):
#     if w == (a+i)*(n-i):
#         b = a+i
#         A.append(b)
# print(min(A))            

#【深基6.例2】小书童——凯撒密码
# n = int(input('请输入:'))
# a = input('请输入:')
# b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# A = []
# for i in a:
#     if i.islower():
#         e = b.index(i)
#         i = b[e+n]
#         A.append(i)
#         if (e+n) > len(b):
#             i = b[e+n-26]
#             A.append(i)
# print(''.join(A))        

#【深基6.例3】[NOIP2008 提高组] 笨小猴
# dance = input('')
# haoci = dict()
# for i in dance:
#     if i in haoci:
#         haoci[i] += 1
#     else:
#         haoci[i] = 1
# A = []
# for key, val in haoci.items():
#     A.append(val)
# b = max(A) - min(A)
# if b == 1:
#     print('Lucky Word')
#     print(b)
# else:
#     is_prime = True
#     if b < 2:  
#         is_prime = False
#     else:
#         for i in range(2, int(b**0.5) + 1):
#             if b % i == 0: 
#                 is_prime = False  
#                 break  
#     if is_prime:
#         print('Lucky Word')
#         print(b)
#     else:
#         print('No Answer')
#         print(0)

#【深基6.例4】口算练习题
# x,y = map(int,input().split())
# if x == 1:
#     print(10 + y)
# elif x == 2:
#     print(1000000000+y)
# else:
#     print(10**18+y)
# n = int(input())  
# y = int(input())  
# A = []
# for i in range(2):
#     a = input().split()
#     A.append([int(x) for x in a])  
# A[0][n-1], A[0][y-1] = A[0][y-1], A[0][n-1]
# A[1][n-1], A[1][y-1] = A[1][y-1], A[1][n-1]
# B = []
# for i in range(y):
#     if i == 0:
#         s = A[0][0] + sum(A[1][:y])
#     elif i == (y-1):
#         s = sum(A[0][:(i+1)]) + A[1][i]
#     else:
#         s = sum(A[0][:(i+1)]) + sum(A[1][i:y])
#     B.append(s)
# print(max(B))

# T = int(input())
# A = []
# for i in range(T):
#     n = int(input('请输入:'))
#     a = list(map(int,input('请输入:').split()))
#     A.append((n,a))

#【深基6.例4】口算练习题
# i = int(input('请输入:'))
# A = []
# for _ in range(i):
#     n = input('请输入:').split()
#     A.append(n)
# d = []
# for i in A:
#     if 'a' in i:
#         w = sum(int(i) for i in i[1:])
#         print('{}+{}={}'.format(i[1],i[2],w))
#         shu = len(str(w))+ len(i[1]) + len(i[2])
#         print(shu + 2)
#         d.append('a')
#     elif 'b' in i:
#         w = int(i[1]) - int(i[2])
#         print('{}-{}={}'.format(i[1],i[2],w))
#         shu = len(str(w))+ len(i[1]) + len(i[2])
#         print(shu + 2)
#         d.append('b')
#     elif 'c' in i:
#         w = int(i[1])*int(i[2])
#         print('{}*{}={}'.format(i[1],i[2],w))
#         shu = len(str(w))+ len(i[1]) + len(i[2])
#         print(shu + 2)
#         d.append('c')
#     else:
#         m = len(d)
#         if d[m-1] == 'a':
#             w = sum(int(i) for i in i[:])
#             print('{}+{}={}'.format(i[0],i[1],w))
#             shu = len(str(w))+ len(i[0]) + len(i[1])
#             print(shu + 2)
#         if d[m-1] == 'b':
#             w = int(i[0]) - int(i[1])
#             print('{}-{}={}'.format(i[0],i[1],w))
#             shu = len(str(w))+ len(i[0]) + len(i[1])
#             print(shu + 2)
#         if d[m-1] == 'c':
#             w = int(i[0])*int(i[1])
#             print('{}*{}={}'.format(i[0],i[1],w))
#             shu = len(str(w))+ len(i[0]) + len(i[1])
#             print(shu + 2)

#【深基6.例5】[NOIP2018 普及组] 标题统计
# s = input('请输入:')
# a = 0
# for i in s:
#     if i ==' ':
#         continue
#     elif i == '/':
#         continue
#     else:
#         a += 1
# print(a)        


#【深基6.例6】文字处理软件
# q = int(input('请输入:'))
# a = input('请输入字符串:')
# A = []
# for i in range(q):
#     b = input('请输入:').split()
#     if int(b[0]) == 1:
#         a = a + b[1]
#         A.append(a)   
#         a = a
#     elif int(b[0]) == 2:
#         c = int(b[1])
#         d = int(b[2])
#         a = a[c:c+d+1]    
#         A.append(a)
#         a = a
#     elif int(b[0]) == 3:
#         c = int(b[1])
#         a = a[:c] + b[2] + a[c:]
#         A.append(a)
#         a = a
#     else:
#         m = 0
#         c = b[1]
#         n = len(a)
#         for i in range(n-1):
#             m += 1
#             if a[i:i+2] == c:
#                 l = m-1
#                 A.append(l)
#                 break    
#         else:
#             l = -1
#             A.append(l)
# for i in A:
#     print(i)    
                
#【深基6.例7】[NOIP2011 普及组] 统计单词数
# a = input('请输入:')
# a = a.lower()
# b = input('请输入:')
# b = b.lower()
# word = b.split()
# n = len(b)
# m = len(a)
# A = [] 
# l = 0
# c = 0
# j = 0
# if a in word:
#     for i in word:
#         j += 1
#         c += len(i)
#         if i == a:
#             l += 1
#             c = c+ (j-1) -m
#             A.append(c)
#     k = min(A)
#     print("{} {}".format(l,k))
# else:
#     print(-1)    

# a = input('请输入要查找的单词:')
# a = a.lower()
# b = input('请输入要搜索的文本:')
# b = b.lower()
# words = b.split()
# count = 0
# m = []
# for i, word in enumerate(words):
#     if word == a:
#         count += 1
#         c = b.find(word)
#         m.append(c)
# if count > 0:
#     print('{} {}'.format(count,min(m)))
# else:
#     print(-1)


# import numpy as np
# import matplotlib.pyplot as plt 
# # 设置中文显示
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# # 生产材料及其成本占比
# categories = ['硬件', '软件', '数据', '开发', '维护']
# cost_percentages = [40, 20, 15, 15, 10]  # 各项成本占比
# # 将数据闭合（雷达图需要闭合）
# categories += [categories[0]]
# cost_percentages += [cost_percentages[0]]
# # 计算角度
# angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
# angles += angles[:1]  # 闭合
# # 绘制雷达图
# fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
# ax.fill(angles, cost_percentages, color='skyblue', alpha=0.6)  # 填充区域
# ax.plot(angles, cost_percentages, color='blue', linewidth=2)  # 绘制边界线

# # 设置角度刻度
# ax.set_xticks(angles[:-1])
# ax.set_xticklabels(categories[:-1], fontsize=12)

# # 设置角度标签的位置
# for label, angle in zip(ax.get_xticklabels(), angles):
#     if angle in (0, np.pi):
#         label.set_horizontalalignment('center')
#     elif 0 < angle < np.pi:
#         label.set_horizontalalignment('left')
#     else:
#         label.set_horizontalalignment('right')

# # 设置径向刻度
# ax.set_rlabel_position(180)  # 将径向刻度标签放在左侧
# plt.yticks([20, 40, 60, 80, 100], ["20%", "40%", "60%", "80%", "100%"], color="grey", size=10)
# plt.ylim(0, 100)

# # 添加标题
# plt.title('生产材料成本占比雷达图', size=16, y=1.1)

# # 显示图表
# plt.tight_layout()
# plt.show()

#【深基6.习1】手机
# sentence = input('请输入:')
# sentence = sentence.split()
# n = len(sentence)
# A = []
# english = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['t','x','y','z']]
# for i in sentence:
#     for j in i:
#         for k in english:
#             if j in k:
#                 number = 0
#                 for m in k:
#                     number += 1
#                     if m == j:
#                         A.append(number) 
# s = sum(A) + n-1
# print(s)

#【深基6.习3】单词覆盖还原
# l = input('请输入:')
# boy = []
# giry = []
# if 'boy' in l or 'girl' in l:
#     bo = 0
#     gi = 0
#     number = len(l)
#     for i in range(number-2):
#         if l[i:i + 3] == 'boy':
#             bo += 1
#     boy.append(bo)
#     number = len(l)
#     for i in range(number-3):
#         if l[i:i+4] == 'girl':
#             gi += 1
#     giry.append(gi)
#     bo = 0
#     gi = 0
#     l = l.replace('girl','')
#     l = l.replace('boy', '')
#     number = len(l)
#     for i in range(number):
#         if l[i] == 'b' or l[i] == 'o' or l[i] == 'y':
#             bo += 1
#         if l[i] == 'g' or l[i] == 'i' or l[i] == 'r' or l[i] ==  'l':
#             gi += 1
#     giry.append(gi)
#     boy.append(bo)
# else:
#     bo = 0
#     gi = 0
#     number = len(l)
#     for i in range(number):
#         if l[i] == 'b' or l[i] == 'o' or l[i] == 'y':
#             bo += 1
#         if l[i] == 'g' or l[i] == 'i' or l[i] == 'r' or l[i] ==  'l':
#             gi += 1
#     giry.append(gi)
#     boy.append(bo)
    
# print(sum(boy))
# print(sum(giry))    


#【深基6.习4】数字反转（升级版）
# z = int(input())
# for x in range(1,2*10**5):
#     for y in range(x,2*10**5):
#         if z == x+y and x != y:
#             print('YES')
#             print("{} {}".format(x,y))
#             break
# else:
#     print('NO')

# # 【深基6.习7】语句解析
# # 初始化变量 a, b, c
# variables = {'a': 0, 'b': 0, 'c': 0}
# # 输入 PASCAL 代码
# code = input("请输入 PASCAL 代码: ")
# # 按分号分割每条赋值语句
# statements = code.split(';')
# # 遍历每条赋值语句
# for statement in statements:
#     statement = statement.strip()  # 去掉前后空格
#     # 解析赋值语句，格式为 [变量]:=[变量或一位整数]
#     if ':=' in statement:
#         var, value = statement.split(':=')
#         var = var.strip()  # 去掉空格
#         value = value.strip()  # 去掉空格
#         # 如果值是变量，则取变量的值
#         if value in variables:
#             variables[var] = variables[value]
#         # 如果值是一位数字，则直接赋值
#         elif value.isdigit() and len(value) == 1:
#             variables[var] = int(value)
#         else:
#             break
# # 输出 a, b, c 的值
# print(variables['a'], variables['b'], variables['c'])

#L1027. 历届试题 带分数
# def find_fraction_representations(N):
#     digits = '123456789'
#     count = 0
#     # 递归生成所有排列
#     def generate_permutations(current, remaining):
#         if not remaining:
#             # 当排列完成时，尝试分割为整数部分、分子和分母
#             num_str = ''.join(current)
#             for i in range(1, len(num_str)):
#                 for j in range(i + 1, len(num_str)):
#                     integer_part = int(num_str[:i])
#                     numerator = int(num_str[i:j])
#                     denominator = int(num_str[j:])
#                     if denominator == 0:
#                         continue
#                     if integer_part + numerator / denominator == N:
#                         # print(f"{N} = {integer_part} + {numerator} / {denominator}")
#                         # nonlocal count
#                         count += 1
#             return
#         # 递归生成排列
#         for i in range(len(remaining)):
#             generate_permutations(current + [remaining[i]], remaining[:i] + remaining[i+1:])
#     generate_permutations([], list(digits))
#     print(f"Total representations found: {count}")
# # 输入N的值
# N = int(input('请输入: '))
# find_fraction_representations(N)

#回溯
# string = '123456789'
# visted = []
# def A(n):
#     if n == 3:
#         print(visted)
#     else:
#         for i in string:
#             if i not in visted:
#                 visted.append(i)
#                 A(n+1)
#                 visted.remove(i)    
# A(0)

#L1027. 历届试题 带分数
# N = int(input('请输入:'))
# visted = []
# result = []
# a = '123456789'
# def A(n):
#     if n == 9:
#         result.append(visted.copy())
#     else:
#         for i in a:
#             if i not in visted:
#                 visted.append(i)
#                 A(n+1)
#                 visted.remove(i)
# A(0)
# B = []
# for i in result:
#     c = []
#     for j in i:
#         c.append(int(j))
#     B.append(c)
# a = 0
# for i in B:
#     for r in range(1,9):
#         for k in range(r+1,9):
#             integer = ''.join(map(str,i[:r]))
#             molecule = ''.join(map(str,i[r:k])) 
#             denominator=''.join(map(str,i[k:]))
#         if denominator == 0:
#             continue
#         if N == int(integer) + int(molecule)/int(denominator):
#             a += 1
# print(a)

#【深基7.例3】闰年展示
# x,y = map(int,input('请输入：').split())
# a = []
# c = 0
# for i in range(x,y+1):
#     if i %4 == 0 and i % 100 != 0:
#         a.append(i)
#         c += 1
#     if i % 400 == 0:
#         a.append(i)
#         c += 1
# print(c)
# a.sort()
# for i in a:
#     print('{}'.format(i),end= ' ')


#【深基7.例2】质数筛
# n = int(input('请输入:'))
# a = list(map(int,input().split()))
# A = []
# for i in a:
#     if i == 1:
#         continue
#     elif i == 2:
#         A.append(i)
#     elif i > 2:
#         isa = True
#         for j in range(2, int(i**0.5) + 1):
#             if i %j == 0:
#                 isa = False
#         if isa:
#             A.append(i)
# print(A)

#【深基7.例7】计算阶乘
# n = int(input('请输入:'))
# def A(n):
#     if n == 1:
#         return 1
#     else:
#         return n*A(n-1)
# print(A(n))

#[蓝桥杯2022初赛] 纸张尺寸
# name = input('请输入:')
# A = []
# a = [1189,841]
# A.append(a)
# for i in range(1,9):
#     c = min(a)
#     d = int(max(a)/2)
#     e = [c,d]
#     A.append(e)
#     a = e
# if int(name[1]) == 0:
#     for i in A[0]:
#         print(i)
# elif int(name[1]) == 1:
#     print(A[1])
# elif int(name[1]) == 2:
#     print(A[2])
# elif int(name[1]) == 3:
#     print(A[3])
# elif int(name[1]) == 4:
#     print(A[4])
# elif int(name[1]) == 5:
#     print(A[5])
# elif int(name[1]) == 6:
#     print(A[6])
# elif int(name[1]) == 7:
#     print(A[7])
# elif int(name[1]) == 8:
#     print(A[8])

# [蓝桥杯2022初赛] 数位排序
# n = int(input('请输入:'))
# m = int(input('请输入:'))
# a = [i for i in range(1,n+1)]
# for i in range(n):
#     next_x = i
#     for j in range(i+1,n):
#         if sum([int(i) for i in str(a[next_x])]) > sum([int(i) for i in str(a[j])]):
#             next_x = j
#         if sum([int(i) for i in str(a[next_x])]) == sum([int(i) for i in str(a[j])]):
#             if a[next_x] > a[j]:
#                 next_x = j    
#     a[i],a[next_x] = a[next_x],a[i]
# print(a[m-1])

#[蓝桥杯2022初赛] 消除游戏
# s = input('请输入:')
# n = len(s)
# s = list(s)
# def A(n,i):
#     i = 1
#     if i == n:
#         return s
    # elif s[i] == s[i-1] and s[i] != s[i+1]:
    #     del s[i]
    #     del s[i]
    # elif s[i] != s[i-1] and s[i] == s[i+1]:
    #     del s[i-1]
    #     del s[i-1]
#     i += 1
#     return A(n,i)
# A(n,i=1)
# if s == ' ':
#     print('EMPTY')
# else:
#     print(s)
# s = input('请输入:')
# n = len(s)
# s = list(s)  # 将字符串转换为列表，方便修改
# for i in range(1,n-1):
#     if s[i] == s[i-1]: 
#         if s[i] != s[i+1]:
#             del s[i]
#             del s[i]
#         i -= 1
# print(s)


# if not s:
#     print('EMPTY')
# else:
#     print(''.join(s))  # 将列表转换回字符串并输出  


# [蓝桥杯2022初赛] 技能升级
N,M = map(int,input('请输入:').split())
A = []
for _ in range(N):
    A1,B1 = map(int,input('请输入:').split())
    A.append((A1,B1))
a = 0
b = 0
while b <= M:
    A.sort()
    a += A[2][0]
    A[2][0] = A[2][0] - A[2][1]
    b += 1
print(a)