#分苹果问题
# pg = 14
# A = int(pg//4)
# print('四个人平均分配:{}'.format(A))
# B = int(pg %4)
# print('剩余多少个:{}'.format(B))
# C = int(A*4)
# print('一共分了多少个:{}'.format(C))

# #⚪的问题
# r = 5
# π = 3.141593
# l = int(2*r*π)
# s = π*r*r
# print(l)
# print(s)

# #猴子吃桃问题(逆向思维)
# A = 1
# B = (A+1)*2
# C = (B+1)*2
# print('买了多少个:{}'.format(C))

#评测问题
# from sympy import symbols, Eq, solve
# #定义变量  
# T, r = symbols('T r')  
# #建立方程组  
# equation1 = Eq(8 * 30, T + 30 * r)
# equation2 = Eq(10 * 6, T + 6 * r) 
# #解方程组  
# solutions = solve((equation1, equation2), (T, r), dict=True)  
 # T_value = solutions[0][T]
# r_value = solutions[0][r]  
# #计算在 10 分钟内刚好评测完需要多少台评测机 
# machines_needed = (T_value + 10 * r_value) / 10  
# print(f"初始任务数 T = {T_value}")  
# print(f"任务增加速度 r = {r_value} 任务/分钟")  
# print(f"需要 {machines_needed:.4f} 台评测机可以在 10 分钟时刚好把评测队列中的程序评测完。")

# #因素分解问题
# def A(n):  
#     factors = []  
#     # 处理2的因数  
#     while n % 2 == 0:  
#        factors.append(2) 
        
#     n = n // 2  
#    # 处理奇数因数，从3开始，步长为2（跳过偶数）  
#     for i in range(3, int(n**0.5) + 1, 2):  
#         while n % i == 0: 
#             factors.append(i)  
#             n = n // i  
# #     # 如果n是一个质数且大于2，则将其自身加入到因数列表中  
#     if n > 2:  
#         factors.append(n)  
#     return factors  
# # # 测试函数  
# print(A(30)) 

# from sympy import symbols, Eq, solve
# #定义变量  
# T, r = symbols('T r')
# #建立方程组  
# equation1 = Eq(24,T+r)
# equation2 = Eq(4,T-r) 
# #解方程组  
# solutions = solve((equation1, equation2), (T, r), dict=True)  
# T_value = solutions[0][T]
# r_value = solutions[0][r] 
# s = int(T_value*r_value)
# print(s)

#清扫问题
# r = 3
# t = 3
# f = 3
# x = f /t
# j = (r+6)*x
# print(j)

#竞赛得分
# from sympy import symbols, Eq, solve
# # #定义变量  
# T, r = symbols('T r')
# # #建立方程组  
# equation1 = Eq(480,T+r)
# equation2 = Eq(0,1.4*T-r) 
# #  #解方程组  
# solutions = solve((equation1, equation2), (T, r), dict=True)  
# T_value = solutions[0][T]
# r_value = solutions[0][r]
# print('小A 和 UIM 分别得多少分:{:.2f} {:.2f}'.format(T_value,r_value))

#简单的分苹果
# from sympy import symbols, Eq, solve
# # #定义变量  
# T, r = symbols('T r')
# #建立方程组  
# equation1 = Eq(11,r-3*T)
# equation2 = Eq(-1,r-4*T) 
# #  #解方程组  
# solutions = solve((equation1, equation2), (T, r), dict=True)  
# T_value = solutions[0][T]
# r_value = solutions[0][r]
# print(T_value)
# print(r_value)
# #print('学生为:{:.2f},苹果为:{:.2f}'.format(T_value,r_value))

# #鸡兔同笼问题
# from sympy import symbols,Eq,solve
# #定义变量
# T,r = symbols('T r')
# #建立方程组
# equation1 = Eq(35,T+r)
# equation2 = Eq(94,4*T+2*r)
# #解方程组
# A = solve((equation1,equation2),(T,r),dict=True)
# B1= int(A[0][T])
# B2= int(A[0][r])
# print('兔子的数量:{:.2f},鸡的数量:{:.2f}'.format(B1,B2))

#定期存款
# # 初始本金  
# T_initial = 10000  
# r_initial = 10000  
# # 复利计算  
# T = T_initial  
# s = 0  
# for i in range(1, 6):  # 5年  
#     T = T * (1 + 0.0035)  # 每年按3.5%复利增长  
#     s += T  # 累计每年的复利后的金额  
# # 输出复利后的累计总额  
# print("复利后的累计总额:", s)  
# # 单利计算  
# r = r_initial * (1 + 0.0040 * 5)  # 5年4%的单利  
# print("单利后的总额:", r)

#英文字母
# english = 'ABCDEFGHIMLTUVWSTRYZ'
# n = 0
# for i in english:
#     if i == 'M':
#         break
#     else:
#         n +=1
#         continue 
# daxie = english[17]    
# print(n+1)       
# print(daxie)

# #销量预测
# '''
# 根据咕咕网校的预测，当课程定价为 110元时,会有 10 人报名。
# 如果课程价格每降低 1 元，就会多 1 名报名者（反之亦然）。
# 如果希望总共能收到 3500 元学费的话，那么应该定价多少呢？
# 已知本题有两个答案符合要求，则取较小的那一个。如果这个答案不是整数，则需四舍五入精确到整数。
# '''
# from sympy import symbols,Eq,solve
# #下变量
# x = symbols('x')
# #建立方程组
# equation1 = Eq(3500,(110-x)*(10+x))
# #解方程组
# # solutions = solve((equation1, equation2), (T, r), dict=True)  
# a = solve((equation1),(x),dict=True)
# T_value = a[0][x]
# print(T_value)

# #字母转换
# english = input('请输入要转换的大写字母:')
# xiaoxie = english.lower()
# print(xiaoxie)

# #回文
# A = input('请输入一行字符串：')
# #将输入的倒置过来，用join来转换字符串
# B = ''.join(reversed(A))
# if B == A:
#     print(True)
# else:
#     print(False)    

#报数游戏
# def A(n):
#     a = int(input('qinghsuru :'))
#     b = 0
#     if a>10 or a<0:
#         raise Exception('请输入10以内的自然数')
#     else:
#         raise Exception('haode')
#         for i in range(1,n+1):
#            b += a**i
#         print(b)      
# A(3)

#模拟报数游
# k = 2
# n = 100
# for i in n:
#     if i == k:
#         del i 
#         continue

# def A(n, k):  
#     # 初始化列表，编号从0到n-1  
#     people = list(range(n))  
#     index = 0  # 从第一个人开始  
#     while len(people) > 1:  
#         # 计算要删除的人的索引
#         print(len(people))  
#         index = (index + k - 1) % len(people) 
#         print(index) 
#         # 删除该人  
#         people.pop(index)  
#     # 剩下的人就是最后留下的  
#     return people[0]  
# # 示例用法  
# n = 10  # 总人数  
# k = 3     
# print("最后留下的是原来的第 {} 号".format(A(n,k)))    

# class SequenceList:  
#     # 初始化顺序表函数  
#     def __init__(self):  
#         self.SeqList = {  
#             '赵小一': 56,  
#             '钱小二': 29,  
#             '孙小三': 69,  
#             '李小四': 95,  
#             '周小五': 92,  
#             '吴小六': 62,  
#             '郑小七': 70,  
#             '王小八': 50,  
#             '宁小九': 80  
#         }  
#     # 求取最大值与最小值  
#     def GetExtremum(self):  
#         while True:  
#             print('*1: 查询最大值')  
#             print('*2: 查询最小值')  
#             print('*3: 查询最大值与最小值')  
#             print('*4: 退出程序')  
#             i = input('请输入: ')  
#             # 将输入转换为整数  
#             choice = int(i)  
#             if choice == 1:  
#                 print('顺序表中的最大值为:', max(self.SeqList),max(self.SeqList.values()))  
#             elif choice == 2:  
#                 print('顺序表中的最小值:', min(self.SeqList))  
#             elif choice == 3:  
#                 print('顺序表中的最大值为:', max(self.SeqList))  
#                 print('顺序表中的最小值:', min(self.SeqList))  
#             elif choice == 4:  
#                 break  
#             else:  
#                 print('无效输入，请重新输入。') 
# if __name__ == "__main__":  
#     seq_list = SequenceList()  
#     seq_list.GetExtremum()  
# class Node:  
#     def __init__(self, data):  
#         self.data = data  
#         self.next = None  
        
# class SingleLinkedList:  
#     def __init__(self):  
#         self.head = Node(None)  # 哨兵节点，不存储实际数据  
#     def create_single_linked_list(self):  
#         print('*请输入数据后按回车键确认，若想结束请输入#。*')  
#         current_node = self.head  
#         while True:  
#             element = input('请输入当前结点的值 (或 # 结束): ')  
#             if element == '#':  
#                 break  
#             try:  
#                 new_node = Node(int(element))  
#             except ValueError:  
#                 print("请输入有效的整数。")  
#                 continue
#             current_node.next = new_node  #指向下一个结点
#             current_node = new_node  #结点到这

#     def print_list(self):  
#         current_node = self.head.next  # 跳过哨兵节点  
#         while current_node:  
#             print(current_node.data, end=" -> ")  
#             current_node = current_node.next  
#         print("None")  
        
#         #尾端插入元素函数
#     def InsertElementInTail(self):
#         Element = (input('请输入待插入结点的值:'))
#         if Element =='#':
#             return
#         cNode = self.head
#         nNode = Node(int(Element))
#         while cNode.next != Node:
#             cNode = cNode.next
#         cNode.next = cNode.next      
  
# if __name__ == '__main__':  
#     B = SingleLinkedList()  
#     B.create_single_linked_list()  
#     B.print_list()
#     B.InsertElementInTail()

# class Node:  
#     def __init__(self, data):  
#         self.data = data  
#         self.next = None  
  
# class SingleLinkedList:  
#     def __init__(self):  
#         self.head = Node(None)  
  
#     def create_single_linked_list(self):  
#         print('*请输入数据后按回车键确认，若想结束请输入#。*')  
#         current_node = self.head  
#         element = input('请输入当前结点的值: ')  
#         while element != '#':  
#             new_node = Node(int(element))  # 确保输入是整数，这里未处理异常  
#             current_node.next = new_node  
#             current_node = current_node.next  
#             element = input('请输入当前结点的值: ')  
  
#     def print_list(self):  
#         current_node = self.head.next  # 跳过哨兵节点  
#         while current_node:  
#             print(current_node.data, end=" -> ")  
#             current_node = current_node.next  
#         print("None")  
  
#     def insert_element_in_tail(self):  
#         element = input('请输入待插入结点的值: ')  
#         if element == '#':  
#             return  
#         current_node = self.head  
#         new_node = Node(int(element))  # 确保输入是整数，这里未处理异常  
#         while current_node.next:  
#             current_node = current_node.next  
#         current_node.next = new_node  
  
#     def insert_element_in_head(self):  
#         element = input('请输入待插入的结点: ')  
#         if element == '#':  
#             return  
#         current_node = self.head  
#         new_node = Node(int(element))  # 确保输入是整数，这里未处理异常  
#         new_node.next = current_node.next  
#         current_node.next = new_node  
  
#     def resolve(self):  # 改名jiejue为resolve，避免中文，同时避免与print_list重复  
#         self.print_list()     
  
# if __name__ == '__main__':  
#     b = SingleLinkedList()  
#     b.create_single_linked_list()  
#     b.print_list()  
#     b.insert_element_in_tail()  
#     b.print_list()  # 使用print_list查看插入后的链表  
#     b.insert_element_in_head()  
#     b.resolve()  # 使用resolve查看最终链表状态

# class Node:
#     def __init__(self,data):
#         #初始化结点函数
#         self.data = data
#         self.next = None
# class SingleLinkedList():
#     def __init__(self):
#     #初始化头节点函数
#         self.head = Node(None)
#     def Creat(self):
#         print('请输入数据后按回车键确认，若想结束请输入#')
#         data = input('请输入结点值:')
#         cNode = self.head
#         while data !='#':
#             nNode = Node(int(data))
#             cNode.next = nNode       #指向
#             nNode.next = self.head   
#             cNode = cNode.next    #创建新的结点
#             data = input('请输入结点值:')
#     def creat(self):
#         current_node = self.head.next  # 跳过哨兵节点  
#         while current_node:  
#             print(current_node.data, end=" -> ")  
#             current_node = current_node.next 
#             if current_node == self.head:  # 如果回到了头节点，结束循环  
#                 break  
#         print("(head)") 
#     # #尾端插入
#     # def breat(self):
#     #     na = input('请输入插入的值:')
#     #     if na == '#':
#     #         return
#     #     cNode = self.head
#     #     nNode = Node(int(na))
#     #     while cNode.next !=self.head:
#     #         cNode = cNode.next
#     #     cNode.next = nNode
#     #     nNode.next = self.head
#     # def A(self):  
#     #     current = self.head.next  # 跳过哨兵节点  
#     #     while current:  
#     #         print(current.data, end=" -> ")  
#     #         current = current.next  
#     #     print("None")       
# B = SingleLinkedList()
# B.Creat()         
# B.creat() 
#双链表
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prew = None
# class List:
#     #初始化头节点函数
#     def __init__(self):
#         self.head = Node(None)
#     #创建双链表函数 
#     def LinkedLIst(self):
#         print('请输入数据后按回车键确认，若想结束请输入#.')
#         data = input('请输入元素:')
#         cNode = self.head
#         while data !='#':
#             nNode = Node(int(data))
#             cNode.next = nNode
#             nNode.prew = cNode
#             cNode = cNode.next
#             data = input('请输入元素:')
#     #尾端插入函数
#     def InserElement(self):
#         Element = input('请输入待插入的结点的值:')
#         if Element == '#':
#             return
#         nNode = Node(int(Element))
#         cNode = self.head
#         while cNode.next != None:
#             cNode = cNode.next
#         cNode.next = nNode
#         nNode.prew = cNode
#     #首端插入
#     def INHead(self):
#         Element = input('请输入待插入的结点值:')
#         if Element == '#':
#             return
#         cNode = self.head.next
#         pNode = self.head
#         nNode = Node(int(Element))
#         nNode.prew = pNode
#         pNode.next = nNode
#         nNode.next = cNode
#         cNode.prew = nNode   
#     #删除元素函数
#     def Delete(self):
#         dElement = int(input('请输入待删除的结点"'))
#         cNode = self.head
#         pNode = self.head
#         if self.IsEmpty():
#             print('当前链表为空！')
#             return
#         while cNode.next !=None and cNode.data !=dElement:
#             pNode = cNode
#             cNode = cNode.next
#         if cNode.data == dElement:
#             if cNode.next == None:
#                 pNode.next = None
#                 del cNode
#                 print('成功删除含有元素',dElement,'的结点')
#             else:
#                 qNode = cNode.next
#                 pNode.next = qNode
#                 qNode.prew = pNode
#                 del cNode
#                 print('成功删除含有元素',dElement,'的结点')
#         else:
#             print('删除失败！链表里面不存在该元素',dElement,'的结点') 
            
#     #遍历双链表函数
#     def Traver(self):
#         cNode = self.head
#         print('按next域遍历带头结点双链表:')
#         if self.IsEmpty():
#             print('当前链表为空!')
#             return
#         while cNode.next != None:
#             cNode = cNode.next
#             self.Vis(cNode)
#         print('None')
    
    
#     #按next域输出元素
#     def Vis(self,tNode):
#         if tNode !=None:
#             print(tNode.data,'->',end=' ')               
            
#     #判断单链表是不是为空函数
#     def IsEmpty(self):
#         if self.GetLength()==0:
#             return True
#         else:
#             return False
#     #获取单链表长度
#     def GetLength(self):
#         cNode = self.head
#         length = 0
#         while cNode.next !=None:
#             length =length+1
#             cNode = cNode.next
#         return length                     
#     #运算      
#     def A(self):  
#         current = self.head.next  
#         if current is None:  
#             print('链表为空！')  
#             return  
#         while current:  
#             print(current.data, end=" -> ")  
#             current = current.next  
#             if current is None:  # 如果到了链表末尾，结束循环  
#                 break  
#         print("(None)")      
# nl = List()
# nl.LinkedLIst()
# nl.A() 
# nl.InserElement()
# nl.A()
# nl.INHead()
# nl.A()                         
# nl.Delete()
# nl.Traver()

# #循环双链表
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prew = None
# class LinkedList:
#     def __init__(self):
#         self.head = Node(None)
#         # self.head.next = self.head  
#         # self.head.prew = self.head 
#     #创建循环双链表 
#     def xiaozhou(self):
#         print('请输入数据后按回车键确认，若想结束请输入#')
#         Emleat = input('请输入结点值:')
#         cNode = self.head
#         while Emleat != '#':
#             nNode = Node(int(Emleat))
#             cNode.next = nNode
#             nNode.prew = cNode
#             self.head.prew = nNode
#             nNode.next = self.head
#             cNode = cNode.next
#             Emleat = input('请输入元素:')
#     #尾端插入元素函数
#     def InTain(self):
#         Element = input('请输入元素值:')
#         if Element =='#':
#             return
#         nNode = Node(int(Element))
#         cNode = self.head
#         while cNode.next !=self.head:
#             cNode = cNode.next
#         cNode.next = nNode
#         nNode.prew = cNode
#         nNode.next = self.head
#         self.head.prew = nNode   
#     #首端插入元素
#     def INhead(self):
#         Element = input('请输入结点值:')
#         nNode = Node(int(Element))
#         if Element == '#':
#             return
#         cNode = self.head.next
#         pnode = self.head
#         nNode.next = cNode
#         nNode.prew = pnode
#         pnode.next = nNode
#         cNode.prew = nNode 
#     #删除结点
#     def Delecor(self):
#         Emlent = input('请输入结点值:')
#         cNode = self.head
#         pNode = self.head
#         if self.IsEmpty():
#             print('当前链表为空！')
#             return
#         while cNode.next != None and cNode.data != Emlent:
#             pNode = cNode
#             cNode = cNode.next
#         if cNode.data == Emlent:
#             qNode = cNode.next
#             pNode.next = qNode
#             qNode.prew = pNode
#             del cNode
#             print('成功删除元素',Emlent,'的节点')
#         else:
#             print('删除失败！不含有该元素',Emlent,'的节点')    
            
#         #判断单链表是不是为空函数
#     def IsEmpty(self):
#         if self.GetLength()==0:
#             return True
#         else:
#             return False
#     #获取单链表长度
#     def GetLength(self):
#         cNode = self.head
#         length = 0
#         while cNode.next !=None:
#             length =length+1
#             cNode = cNode.next
#         return length              
                
#     #计算
#     def A(self):
#         croe = self.head.next
#         if croe.next == self.head:
#             print('链表为空！')
#             return
#         while True:  
#             print(croe.data, end=" <-> ") 
#             croe = croe.next  
#             if croe == self.head:
#                 break
#         print("(head)")
# c = LinkedList()
# c.xiaozhou()
# c.A()
# c.InTain()
# c.A()        
# c.INhead()
# c.A()
# c.Delecor()
# c.A()
#组队问题
# class StudentNode:
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex 
#         self.next = None
# class SLL: 
#     def __init__(self):
#         self.head = StudentNode(None,None)
#     def Creater(self):
#         print('请输入数据后按回车键确认，若想结束按#')
#         cNode = self.head
#         Emlent = input('请输入姓名，性别并用空格隔开:')
#         while Emlent != '#':
#             Name = Emlent.split(' ')[0]
#             Sex = Emlent.split(' ')[1]
#             nNode = StudentNode(Name,Sex)
#             cNode.next = nNode
#             cNode = cNode.next
#             Emlent = input('请输入姓名，性别并用空格隔开:')
#     #拆分单链表
#     def DivideSLL(self,LinkedListB,LinkedListC):
#         aNode = self.head
#         bNode = LinkedListB.head
#         cNode = LinkedListC.head
#         cPos = 0
#         while aNode.next != None:
#             aNode = aNode.next
#             cPos = cPos +1
#             pNode = aNode   #保存位置
#             if cPos % 2 ==1:
#                 bNode.next = pNode
#                 bNode = bNode.next
#             else:
#                 cNode.next = pNode
#                 cNode = cNode.next
#         bNode.next = None
#         cNode.next = None
#     #遍历单链表函数
#     def TraverseSLL(self):
#         cNode = self.head.next
#         while cNode.next !=None:
#             print(cNode.name,'->',end='') 
#             cNode = cNode.next
#         print(cNode.name)
#     #获取单链表长度
#     def GetLength(self):
#         cNode = self.head
#         length = 0
#         while cNode.next !=None:
#             length =length+1
#             cNode = cNode.next
#         return length     
#     #打印函数
#     def PrintSLL(self):
#         cNode = self.head.next
#         if cNode.sex == '男':
#             print('男生小队包含',self.GetLength(),'个人，分别是：')
#             self.TraverseSLL()
#         else:
#             print('女生小队包含',self.GetLength(),'个人，分别是：')
#             self.TraverseSLL()
# if __name__=='__main__':
#     LA = SLL()
#     LB = SLL()
#     LC = SLL()
#     LA.Creater()
#     LA.DivideSLL(LB,LC)
#     LB.PrintSLL()
#     LC.PrintSLL()

# #循环单链表的应用
# class CLNNode:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prew = None
# class CSL:
#     def __init__(self):
#         self.haed = CLNNode(None)
#     #抽奖函数
#     def Lottery(self):
# def A(n):  
#     # 辅助函数，用于递归计算乘积并打印中间结果  
#     def helper(k):  
#         if k == 1:  
#             return 1  # 基准情况，返回1  
#         else:  
#             result = k * helper(k - 1)  # 递归计算乘积  
#         print(result)  # 打印当前步骤的乘积结果  
#         return result  # 返回乘积结果给上一层递归 
#     helper(n)  
  
# # 调用函数A，传入参数3  
# A(3)
# def A(n):
#     if int(n)<1 or int(n)>20:
#         print('请重新输入')
#     elif n == 1:
#         return  1
#     else:
#         result = n * A(n-1)
#         return result 
# n = int(input('请输入需要求解的数:'))
# print(A(n))    
#栈
# MAXSIZE = 10
# class CREam:
#     #顺序栈的初始化
#     def __init__(self):
#         self.elem = [None]*MAXSIZE    #动态分配一个最大容量的数组空间
#         self.top,self.base = 0,0      #栈顶与栈底
#         self.stack_size = MAXSIZE     #最大空间
#     #入栈
#     def push(self,e):
#         if self.top - self.base == self.stack_size:
#             raise Exception('栈空间已满')
#         self.elem[self.top] = e
#         self.top += 1
#     # #出栈
#     def pop(self):
#         if self.top == self.base:    
#             raise Exception('栈已空')
#         self.top -=1
#         return self.elem[self.top]
#     #取栈顶元素
#     def get_top(self):
#         if self.top !=self.base:
#             return self.elem[self.top-1]
#         else:
#             raise Exception('栈已空')
#     #判断栈是不是为空
#     def stack_empty(self):
#         return self.top == self.base
    
#     #栈的长度
#     def __len__(self):
#         return self.top - self.base    
# if __name__ == '__main__':
#     s = CREam()
#     s.push(1)
#     s.push(2)
#     print('栈的长度:',len(s))
#     print('栈顶元素:',s.get_top())
#     s.pop()
#     s.pop()
#     print('栈为空:',s.stack_empty())    
    
    
# MAXSIZE = 10  
# class CREam:  
#     # 顺序栈的初始化  
#     def __init__(self):  
#         self.elem = [None] * MAXSIZE    # 动态分配一个最大容量的数组空间  
#         self.top, self.base = 0, 0      # 栈顶与栈底  
#         self.stack_size = MAXSIZE       # 最大空间  

#     # 入栈  
#     def push(self, e):  
#         if self.top - self.base == self.stack_size:  
#             raise Exception('栈空间已满')  
#         self.elem[self.top] = e  
#         self.top += 1  

#     # 出栈  
#     def pop(self):  
#         if self.top == self.base:      
#             raise Exception('栈已空')  
#         self.top -= 1  
#         return self.elem[self.top]  
  
#     # 取栈顶元素  
#     def get_top(self):  
#         if self.top != self.base:  
#             return self.elem[self.top - 1]  
#         else:  
#             raise Exception('栈已空')  
  
#     # 判断栈是不是为空  
#     def stack_empty(self):  
#         return self.top == self.base  
  
#     # 栈的长度  
#     def __len__(self):  
#         return self.top - self.base  
  
#     # 打印栈里的所有元素  
#     def print_stack(self):  
#         if self.stack_empty():  
#             print("栈为空")  
#         else:  
#             print("栈里的元素:")  
#             for i in range(self.base, self.top):  
#                 print(self.elem[i], end=' ')  
#             print()  # 换行  

# if __name__ == '__main__':  
#     s = CREam()  
#     s.push(1)  
#     s.push(2)  
#     s.push(3)  # 添加更多元素以测试  
#     print('栈的长度:', len(s))  
#     print('栈顶元素:', s.get_top())  
#     s.print_stack()  # 打印栈里的元素  
#     s.pop()  
#     s.print_stack()  # 再次打印栈里的元素  
#     s.pop()  
#     s.pop()  
#     print('栈为空:', s.stack_empty())    
    
    
# #链栈
# class StackNode:
#     def __init__(self,data = None):
#         self.data = data
#         self.next = None
#     def __str__ (self):
#         return str(self.data)
# class LinkStack:
#     #初始化链栈
#     def __init__(self):
#         self.top = None
#     #入栈
#     def                 

#顺序栈
# class CRES:
#     #初始化栈函数
#     def __init__(self):
#         self.MaxStackSize = 10
#         self.s = [None for x in range(0,self.MaxStackSize)]
#         self.top = -1

#     #判断栈是不是空的函数
#     def IsEmptyStack(self):
#         if self.top == -1:
#             iTop = True
#         else:
#             iTop = False
#             return iTop

#     #进栈函数
#     def PushStack(self,x):
#         if self.top < self.MaxStackSize-1:
#             self.top = self.top +1
#             self.s[self.top] = x
#         else:
#             print('栈已满')
#             return  
      
#     #元素出栈函数
#     def Pop(self):
#         if self.IsEmptyStack():
#             print('栈已空')
#             return
#         else:
#             iTop = self.top
#             self.top = self.top - 1
#             return self.s[iTop]

#     #获取栈顶元素
#     def get_top(self):
#         if self.IsEmptyStack():
#             print('栈已空')
#             return
#         else:
#             return self.s[self.top]
    
#     #遍历栈内函数
#     def StackT(self):
#         if self.IsEmptyStack():
#             print('栈已空')
#             return
#         else:
#             for i in range(0,self.top+1):
#                 print(self.s[i],end=' ')
#     #将用户输入的数据元素进栈的函数
#     def Creat(self):
#         data = input('请输入元素(结束请输入#)')
#         while data != '#':
#             self.PushStack(data)
#             data = input('请输入元素:')
#     #开始计算
# ss = CRES()
# ss.Creat()
# print('栈内的元素为:',end=' ')
# ss.StackT()
#链栈
# class StackNode:
#     def __init__(self,data = None):
#         self.data = data
#         self.next = None
#     def __str__ (self):
#         return str(self.data)
# class LinkStack:
#          #初始化链栈
#     def __init__(self):
#         self.top = None
#     #入栈
#     def push(self,e):
#         #在栈顶插入元素e
#         p = StackNode(data = e)  #生成新结点，将新节点数据域为e
#         p.next = self.top    #将新节点插入栈顶
#         self.top = p         #修改指针为p
#     #出栈
#     def pop(self):
#         if self.top is None:
#             raise Exception('栈已空')
#         e = self.top.data
#         self.top = self.top.next
#         return e
#     #返回栈顶元素，不修改栈顶元素
#     def get_top(self):
#         if self.top is not None:
#             return self.top.data
#         else:
#             raise Exception('栈已空')
        
# class Node:
#     def __init__(self,data = None):
#         self.data = data
#         self.next = None
#     def __str__(self):
#         return str(self.data)
# class TRE:
#     #链栈的初始化
#     def __init__(self):
#         self.font = Node()   #对头
#         self.real = self.font
#     #入队
#     def  dfre(self,e):
#         p = Node(e) #数据域为e
#         self.real.next = p
#         self.real = p
#     #出队
#     def chudui(self):
#         #删除元素，并返回
#         if self.font == self.real:
#             raise Exception('队列已空')
#         p = self.font.next #p指向对头元素
#         e = p.data #e保留对头元素
#         self.font.next = p.next #    
                
# #顺序栈
# MAXSIZE = 4
# class dNode:
#     #顺序栈的初始化
#     def __init__(self):
#         self.elem = [None]*MAXSIZE   #分配一个数组空间
#         self.top,self.base = 0,0   #初始化栈顶与栈底
#         self.stack_size = MAXSIZE   #最大容量
#     #入栈
#     def push(self,e):
#         if self.top - self.base == self.stack_size:
#             raise Exception('栈空间已满')
#         self.elem[self.top] = e
#         self.top += 1
#     #出栈
#     def pop(self):
#         if self.top == self.base:
#             raise Exception('栈已空')
#         self.top -=1
#         return self.elem[self.top]

# #链栈
# class eNode:
#     def __init__(self,data = None):
#         self.data = data
#         self.next = None
#     def __str__(self):
#         return str(self.data)
# class Linx:
#     #栈的初始化
#     def __init__(self):
#        self.top = None #构造一个空栈
#     #栈的入栈
#     def push(self,e):
#         p = eNode(data = e) #生成新节点，将节点域置为e
#         p.next = self.top
#         self.top = p
#     # 出栈
#     def pop(self):
#         if self.top is None:
#             raise Exception('栈已空')
#         e = self.top.data
#         self.top = self.top.next
#         return e
#     #取栈顶元素
#     def get_top(self):
#         if self.top is not None:
#             return self.top.data
#         else:
#             raise Exception('栈已空')
       
# #循环队列
# MAXSIZE = 10
# #队列初始化
# class qrty:
#     def __init__(self):
#         self.elem = [None]*MAXSIZE
#         self.font,self.rear = 0,0     #头指针与尾指针
#         self.queue_size = MAXSIZE
#     #入队
#     def en_queue(self,e):
#         if (self.rear+1)%self.queue_size == self.font:
#             raise Exception('队已空')
#         self.elem[self.rear] = e
#         self.rear = (self.rear+1) % self.queue_size

#     #出队
#     def de_queue(self):
#         if self.font == self.rear:
#             raise Exception('队已空')
#         e = self.elem[self.font]
#         self.font = (self.font+1)%self.queue_size
#         return e

#     #取对头元素
#     def get_queue(self):
#         if self.font != self.rear:
#             return self.elem[self.font]
#         else:
#             raise Exception('队已空')

#     # 打印整个队列
#     def _print_queue(self):
#         result = []
#         index = self.font
#         while index != self.rear:
#             result.append(self.elem[index])
#             index = (index + 1) % self.queue_size
#         return result    

# if __name__ == '__main__':
#     q = qrty()
#     q.en_queue(1)
#     q.en_queue(2)
#     q.en_queue(4)
#     print("当前队列状态:", q._print_queue())

# #链队列
# class QNode:
#     def __init__(self,data = None):
#         self.data = data
#         self.next = None
#     def __str__(self):
#         return str(self.data)
# class LinkQueue:
#     #链的初始化
#     def __init__(self):
#         self.font = QNode()
#         self.rear = self.font

# #串的顺序存储
# class StringList:
#     #初始化串
#     def __init__(self):
#         self.MaxStringSize = 256
#         self.chara = ''
#         self.length = 0
#     #判断川是不是空的
#     def IsEmptyString(self):
#         if self.length == 0:
#             IsEmpty = True
#         else:
#             IsEmpty = False
#         return IsEmpty
#     #创建一个串的函数
#     def CreateString(self):
#         stringSh = input('请输入:')
#         if len(stringSh) > self.MaxStringSize:
#             self.chara = stringSh[:self.MaxStringSize]
#         else:
#             self.chara = stringSh
#     #从指定位置开始获取指定长度字串的函数
#     # def SUBstring(self,iPos,lenfth):
                   
# #串的链式存储
# class StringNode:
#     def __init__(self):
#         self.data = None
#         self.next = None
#     #初始化串的函数
#     def __init__(self):
#         self.head = StringNode()
#         self.tail = self.head
#         self.length = 0

# class stringLink:
#     #创建一个串的函数  
#     def CreateString(self):
#         stringSH = input('\n请输入字符串.按回车键结束:')
#         while self.length < len(stringSH):
#             Tstring = StringNode()
#             Tstring.data = stringSH(self.length)
#             self.tail.next = Tstring
#             self.tail = Tstring
#             self.length = self.length + 1

#BF算法
# max_size =100
# class sstring:
#     def __init__(self):
#         #初始化一个空串
#         self.length = 0 #串当前长度
#         self.ch = [None] * max_size #最大长度为max_size空间
#     def str_assign(self,s):
#         #把串的值赋给s
#         n = len(s) #求串s的长度
#         if n > max_size - 1: #此处为max_size-1 因为0号单元弃用
#             raise Exception('空间已满')
#         else:
#             self.length = 0 #把串置为空
#             while self.length < n:
#                 self.length +=1
#                 self.ch[self.length] = s[self.length -1]
#             return self
#     def index_bf(s,t,pos):
#         #返回模式t在主串s中第pos个字符之后第s一次出现的位置。若不存在,则返回值为0
#         #其中，t非空，1<=pos<=s.length
#         i= pos
#         j = 1 #初始化
#         while i <= s.length and j <= t.length: #两串均未比较到串尾
#             if s.ch[i] == t.ch[j]:
#                 i +=1
#                 j +=1  #继续比较后继字符
#             else:
#                 i = i -j +2
#                 j =1  #指针后退，重新开始匹配
#         if j > t.length:
#             return i - t.length   #匹配成功
#         else:
#             return 0 #匹配失败
# if __name__ == '__main__':
#     s,t = sstring(),sstring()   
#     ss = '123' ; tt= '23';pos = 1
#     print('主串{0} 和字符{1}在第{2}个字符后首次匹配的位置为:'.format(ss,tt,pos),index_bf(s.str_assign(ss),t.str_assign(tt),pos))  
    
#     ss = '123210';tt = '21'; pos = 2
#     print('主串{0}和字串{1}在第{2}个字符后首次匹配的位置为:'.format(ss,tt,pos),
#           index_bf(s.str_assign(ss),t.str_assign(tt),pos))
#     ss = '1111111';tt = '111'; pos = 8
#     print('主串{0}和字串{1}在第{2}个字符后首次匹配的位置为:'.format(ss,tt,pos),
#           index_bf(s.str_assign(ss),t.str_assign(tt),pos))   

 
#BF算法AI
# max_size = 100
# class SString:
#     def __init__(self):
#         self.length = 0  # 串当前长度
#         self.ch = [None] * (max_size + 1)  # 预留一个空位，不使用0号单元

#     def str_assign(self, s):
#         n = len(s)
#         if n > max_size:
#             raise Exception('空间已满')
#         self.length = n
#         for i in range(n):
#             self.ch[i + 1] = s[i]  # 从1开始存储
#         return self

    # def index_bf(self, t, pos):
    #     # 确保t是非空串
    #     if t.length == 0:
    #         return 0
    #     i = pos
    #     j = 1
    #     while i <= self.length and j <= t.length:
    #         if self.ch[i] == t.ch[j]:
    #             i += 1
    #             j += 1
    #         else:
    #             i = i - j + 2
    #             j = 1
    #     if j > t.length:
    #         return i - t.length
    #     else:
    #         return 0

# if __name__ == '__main__':
#     s, t = SString(), SString()
#     ss = '123'; tt = '23'; pos = 1
#     s.str_assign(ss)
#     t.str_assign(tt)
#     print('主串{0} 和字符{1}在第{2}个字符后首次匹配的位置为:'.format(ss, tt, pos), s.index_bf(t, pos))

#     ss = '123210'; tt = '21'; pos = 2
#     s.str_assign(ss)
#     t.str_assign(tt)
#     print('主串{0}和字串{1}在第{2}个字符后首次匹配的位置为:'.format(ss, tt, pos), s.index_bf(t, pos))

#     ss = '1111111'; tt = '111'; pos = 5
#     s.str_assign(ss)
#     t.str_assign(tt)
#     print('主串{0}和字串{1}在第{2}个字符后首次匹配的位置为:'.format(ss, tt, pos), s.index_bf(t, pos))

#遍历二叉树
# class BinaryTree:
#     def __init__(self,data = None):
#         self.data = data
#         self.Lchild = None
#         self.rchild = None
#     def create_bitree(self):
#         #按先序次序输入二叉树中结点的值
#         ch = input()
#         if ch =='#':
#             self.data = None
#         else:   #递归创建二叉树
#             self.data = ch #根节点赋给ch
#             self.Lchild = BinaryTree()   #为当前结点创造一个空的左子树
#             self.Lchild.create_bitree()  #递归创建左子树
#             self.rchild = BinaryTree()
#             self.rchild.create_bitree()
#     def A(self):
#         #中序遍历二叉树的递归算法
#         if self.data is not None:   #二叉树为空
#             self.Lchild.A()   #中序遍历左子树
#             print(self.data) #访问根节点
#             self.rchild.A()
#     def B(self):
#         #中序遍历的非递归算法
#         stack = []
#         p = self
#         while p.data is not None or stack:
#             if p.data is not None:     #p非空
#                 stack.append(p)     #根指针进栈
#                 p = p.Lchild  #根指针进栈,遍历左子树
#             else:
#                 q = stack.pop()   #退栈
#                 print(q.data)       #访问根节点
#                 p = q.rchild    #遍历右子树
# def copy(t):
#     #复制一颗完全相同的二叉树
#     if t.data is None:
#         tree = BinaryTree()   #如果是空树，递归结束
#     else:
#         tree = BinaryTree(t.data)    #复制根节点
#         tree.Lchild = copy(t.Lchild)  #递归复制左子树
#         tree.rchild = copy(t.rchild)   #
#     return tree
# # def deph(t):
# #     #计算深度
# #     if t.data is None:
# #         return 0
# #     else:   #二叉树的深度为左子树与右子树较大者加一
# #         return 1 + max(deph(t.Lchild),deph(t.rchild))
# # def node_count(self):
# #     #统计二叉树结点的个数
# #     if t.data is None:
# #         return 0
# #     else:
# #         return 1 + node_count(t.Lchild) + node_count(t.rchild)
# if __name__ == '__main__':
#     tree = BinaryTree()
#     print('请输入二叉树各结点的值:')
#     tree.create_bitree()
#     new_tree = copy(tree)
#     print('复制得到的新树的中序序列(非递归):')
#     new_tree.A()
#     print('复制得到的新树的中序序列(递归):') 
#     new_tree.B()
#     # print('新树的深度:')
#     # print(deph(new_tree))
#     # print('新树的结点树:') 
#     # print(node_count(new_tree))    

#二叉树AI
# class BinaryTree:
#     def __init__(self, data=None):
#         self.data = data
#         self.Lchild = None
#         self.rchild = None
#     def create_bitree(self):
#         # 按先序次序输入二叉树中结点的值
#         ch = input("请输入节点值（输入#表示空节点）: ")
#         if ch == '#':
#             self.data = None
#         else:
#             self.data = ch  # 根节点赋给ch
#             self.Lchild = BinaryTree()  # 为当前结点创造一个空的左子树
#             self.Lchild.create_bitree()  # 递归创建左子树
#             self.rchild = BinaryTree()
#             self.rchild.create_bitree()
#     def inorder_recursive(self):
#         # 中序遍历二叉树的递归算法
#         if self.data is not None:
#             self.Lchild.inorder_recursive()  # 中序遍历左子树
#             print(self.data)  # 访问根节点
#             self.rchild.inorder_recursive()

#     def inorder_iterative(self):
#         # 中序遍历的非递归算法
#         stack = []
#         p = self
#         while p is not None or stack:
#             if p is not None:
#                 stack.append(p)
#                 p = p.Lchild
#             else:
#                 p = stack.pop()
#                 print(p.data)
#                 p = p.rchild
# def copy(t):
#     # 复制一颗完全相同的二叉树
#     if t.data is None:
#         tree = BinaryTree()
#     else:
#         tree = BinaryTree(t.data)
#         tree.Lchild = copy(t.Lchild)
#         tree.rchild = copy(t.rchild)
#     return tree
# def depth(t):
#     # 计算深度
#     if t.data is None:
#         return 0
#     else:
#         return 1 + max(depth(t.Lchild), depth(t.rchild))
# def node_count(t):
#     # 统计二叉树结点的个数
#     if t.data is None:
#         return 0
#     else:
#         return 1 + node_count(t.Lchild) + node_count(t.rchild)
# if __name__ == '__main__':
#     tree = BinaryTree()
#     print('请输入二叉树各结点的值:')
#     tree.create_bitree()
#     new_tree = copy(tree)
#     print('复制得到的新树的中序序列(递归):')
#     new_tree.inorder_recursive()
#     print('复制得到的新树的中序序列(非递归):')
#     new_tree.inorder_iterative()
#     print('新树的深度:')
#     print(depth(new_tree))
#     print('新树的结点数:')
#     print(node_count(new_tree))



#KMP算法
# max_size = 100
# class SString:
#     def __init__(self):
#         # 初始化一个空的串
#         self.length = 0
#         self.ch = [None] * max_size

#     def str_assign(self, s):
#         # 给串赋值
#         n = len(s)
#         if n > max_size - 1:
#             raise Exception('空间已满')
#         self.length = n
#         for i in range(n):
#             self.ch[i] = s[i]
#         return self
# def get_next(t):
#     # 求串t的next数组
#     next_val = [0] * (t.length + 1)   # 初始化next数组，长度为t.length + 1，所有元素初始值为0
#     i = 1
#     j = 0
#     while i < t.length:
#         if j == 0 or t.ch[i - 1] == t.ch[j - 1]:# 注意使用 i-1 和 j-1，因为数组是从0开始的
#             i += 1
#             j += 1
#             next_val[i] = j
#         else:
#             j = next_val[j]
#     return next_val
# def index_kmp(s, t, pos, next_val):
#     # KMP算法查找子串在主串中的位置
#     i = pos - 1  # 注意从pos-1开始，因为数组是从0开始的
#     j = 0
#     while i < s.length and j < t.length:
#         if j == 0 or s.ch[i] == t.ch[j]:
#             i += 1
#             j += 1
#         else:
#             j = next_val[j]
#         if j == t.length:
#             return i - j + 1  # 返回匹配开始的位置
#     return 0  # 如果没有找到匹配，返回0

# if __name__ == '__main__':
#     s = SString(); t = SString()
#     s_str = '123423'; t_str = '23'; pos = 1
#     s.str_assign(s_str); t.str_assign(t_str)
#     next_val = get_next(t)
#     result = index_kmp(s, t, pos, next_val)
#     if result != 0:
#         print(f'主串和子串在第{pos}个字符后首次匹配的位置: {result}')
#     else:
#         print(f'主串和子串在第{pos}个字符后未找到匹配')                          
        
# #哈夫曼算法
# INF = 0x3f3f3f
# class Human:
#     def __init__(self,weight,parent,lchild,rchild):
#         self.weight = weight #结点的权值
#         self.parent = parent #结点的双亲
#         self.lchild = lchild #左孩子下表
#         self.rchild = rchild 
# class HuffmanT:
#     def __init__(self,n,data):
#         self.n = n #全部结点数
#         self.ht =   

import numpy as np
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 生产材料及其成本占比
categories = ['硬件', '软件', '数据', '开发', '维护']
cost_percentages = [40, 20, 15, 15, 10]  # 各项成本占比

# 将数据闭合（雷达图需要闭合）
categories += [categories[0]]
cost_percentages += [cost_percentages[0]]

# 计算角度
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # 闭合

# 绘制雷达图
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, cost_percentages, color='skyblue', alpha=0.6)  # 填充区域
ax.plot(angles, cost_percentages, color='blue', linewidth=2)  # 绘制边界线

# 设置角度刻度
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories[:-1], fontsize=12)

# 设置角度标签的位置
for label, angle in zip(ax.get_xticklabels(), angles):
    if angle in (0, np.pi):
        label.set_horizontalalignment('center')
    elif 0 < angle < np.pi:
        label.set_horizontalalignment('left')
    else:
        label.set_horizontalalignment('right')

# 设置径向刻度
ax.set_rlabel_position(180)  # 将径向刻度标签放在左侧
plt.yticks([20, 40, 60, 80, 100], ["20%", "40%", "60%", "80%", "100%"], color="grey", size=10)
plt.ylim(0, 100)

# 添加标题
plt.title('生产材料成本占比雷达图', size=16, y=1.1)

# 显示图表
plt.tight_layout()
plt.show()
