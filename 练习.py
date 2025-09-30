import pandas as pd
import numpy as np
# A = pd.Series(np.arange(4),index=['a','b','c','d'])
# B = pd.Series(np.arange(5),index=['f','a','g','h','t'])
# C = A+B
# #print(C)

# N = pd.DataFrame(np.arange(12).reshape((4,3)),index=['a','b','c','d'],columns=list('ABC'))
# M = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','v','d'],columns=list('ABD'))
# I = N.add(M,fill_value=0)
# print(I)
# A = pd.DataFrame(np.arange(12).reshape(4,3),index=['a','b','c','d'],columns=list('ABC'))
# print(A)

# boolean=[True,False]
# gender=["男","女"]
# data = pd.DataFrame({
#     "height":np.random.randint(150,190,5),
#     "weight":np.random.randint(40,90,5),
#     "smoker":[boolean[x] for x in np.random.randint(0,2,5)],
#     "gender":[gender[x] for x in np.random.randint(0,2,5)],
#     "age":np.random.randint(16,24,5)})
# print(data)
# def gender_map(x):
#    gender = 1 if x == "男" else 0    
#    return gender
# data['gender'].map(gender_map)

import pandas as pd
import numpy as np
# s1 = pd.DataFrame(np.arange(12).reshape(4,3),index=list('dbca'),columns=list('ABC'))
# print(s1)
# A = s1.sort_values(by=['A','B'],ascending=False)
# print(A)

# data = {'A':[1,2,3],
#          'B':[4,5,0],
#          'C':[8,2,0]}
# A = pd.DataFrame(data)
# # print(A)
# N = A.sort_values(by=['B','C'])
# print(N)
# s1 = pd.Series([-7,2,4,5,6,7])
# print(s1)
# A = s1.rank()
# print(A)
# data = {'A':[1,2,4],
#         'B':[2,4,5],
#         'C':[2,4,8]}
# s1 = pd.DataFrame(data)
# print(s1)
# A = s1.unique()
# print(A)
# df = pd.DataFrame([[1.4,np.nan],[7.1,-4.5],[2.0,np.nan],[3.0,4]],index=['a','b','c','d'],columns=['one','two'])
# print(df)
# A = df.quantile()
# print(A)
# df = pd.read_csv("C:\\Users\\周顺\\Desktop\\工作簿1.csv")
# A = pd.read_csv("C:\\Users\\周顺\\Desktop\\工作簿1.csv",chunksize=1)
# print(A)
# # B = A.get_chunk()
# # print(B)

import pandas as pd
import numpy as np
# data = {'a':[1,3,4],'b':[4,5,8],'c':[9,6,4]}
# B = pd.DataFrame(data)
# A = B.to_csv('C:\\Users\\周顺\\Desktop\\工作簿1.csv',index=False,columns=['a','c','b'])
# print(A)

# import pandas as pd  
# import matplotlib.pyplot as plt  
# from matplotlib import font_manager  
  
# # 读取数据  
# a = pd.read_excel('C:\\Users\\周顺\\Desktop\\天气统计.xlsx', sheet_name='Sheet2')  
  
# # 设置字体  
# font = font_manager.FontProperties(fname=r"C:\\Windows\\Fonts\\msyhl.ttc", size=20)  
# # 提取数据  
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

# tem = np.random.randint(1,100,20)
# df1 = pd.DataFrame(tem)
# tem = np.arange(0,100,5)
# df2 = pd.DataFrame(tem)
# tem = np.random.randn(20)
# df3 = pd.DataFrame(tem)
# df = zip([df1,df2,df3],axis=1)
# print(df)

# import numpy as np  
# import pandas as pd  
# # 创建第一个 DataFrame  
# tem = np.random.randint(1, 100, 20)  
# df1 = pd.DataFrame(tem, columns=['Random_Ints'])  
# # 创建第二个 DataFrame  
# tem = np.arange(0, 100, 5)  
# df2 = pd.DataFrame(tem, columns=['Range_Ints'])  
# # 创建第三个 DataFrame  
# tem = np.random.randn(20)  
# df3 = pd.DataFrame(tem, columns=['Random_Floats'])  
# # 使用 pd.concat 沿列方向合并 DataFrame  
# df = pd.concat([df1, df2, df3], axis=1)  
# df.columns = ['col1','col2','col3']
# #提取第一列中不在第二列中出现的数字
# A= df['col1'][~df['col1'].isin(df['col2'])]
# print(A)

# A = str(input('请输入一个三位数的整数'))
# B = len(A)
# C = int(A[0])**B + int(A[1])**B + int(A[2])**B
# if int(A) == int(C):
#     print('{}是三娴熟'.format(int(A)))
# else:
#     print('{}不是'.format(int(A)))    
# class Node:  
#     def __init__(self, data):  
#         # 初始化结点函数  
#         self.data = data  
#         self.next = None  
  
# class SingleLinkedList:  
#     def __init__(self):  
#         # 初始化头节点函数（哨兵节点）  
#         self.head = Node(None)  
#         self.head.next = self.head  # 初始化为循环链表，头节点指向自己  
  
#     def create(self):  
#         print('请输入数据后按回车键确认，若想结束请输入#')  
#         data = input('请输入结点值: ')  
#         current_node = self.head  
#         while data != '#':  
#             new_node = Node(int(data))  
#             current_node.next = new_node  
#             new_node.next = self.head  # 新节点指向头节点，形成循环  
#             current_node = new_node # 移动当前节点到新节点  
#             data = input('请输入结点值: ')  
#         # 确保尾节点的 next 指向头节点（理论上在循环中已经处理了，但显式设置以防万一）  
#         current_node.next = self.head  
  
#     def print_list(self):  
#         current_node = self.head.next  # 跳过哨兵节点  
#         if current_node == self.head:  
#             print('链表为空')  
#             return  
#         while True:  
#             print(current_node.data, end=" -> ")  
#             current_node = current_node.next  
#             if current_node == self.head:  # 如果回到了头节点，结束循环  
#                 break  
#         print("(head)")  # 标记循环的结束，显示回到头节点  
  
# # 示例使用  
# sll = SingleLinkedList()  
# sll.create()  
# sll.print_list()
