#重复次数与循环体是不一样的
#求出n个数据中前i个的最大值
# A = [1,2,3,4,5,6,1,3,4,5,6,2,0,8,8,9]
# max = A[0]
# for i in range(1,len(A)):
#     if A[i] >max:
#         max = A[i]
#     print(max)

# #实现无循环的方法
# def Fun(self):
#     i = 0
#     print('周顺 学号:2023001080')
# Fun(1)    
#单循环
# def Fun(n):
#     data = 0
#     for i in range(1,n+1):
#         data = data + i
#     print(data) 
# Fun(10)   

# for i in range(1,10):
#     for j in range(1,i+1):      
#         print('{}*{}={:<4}'.format(i,j,i*j),end='')
#     print()    

# def A(n):
#     data = 0
#     for i in range(1,n+1):
#         data+=i
#     print(data)    
# A(10)

# n = int(input('请输入一个整数n:'))
# A = int((n*(n+1))/2)
# print(A)

# def A(n):
#     for i in range(2,n):
        
#         if n%i != 0:
#             print('{}为素数'.format(i+1))
#         else:
#             print('不为素数')    
# A(3)            

# def A(n):
#     a = 1
#     for i in range(1,n+1):
#         a = a*i
#     print(a)    
# A(3)    


# def fibonacci_like_sequence(n, a1=1, a2=2):  
#     if n == 1:  
#         return a1  
#     elif n == 2:  
#         return a2  
#     a, b = a1, a2  
#     for i in range(3, n + 1):  
#         c = a + b  
#         a, b = b, c  
#     return b  
# # 计算第20项的值  
# result = fibonacci_like_sequence(4)  
# print(result)

# def A(n):
#     a = 1
#     b = 2
#     for i in range(3,n+1):
#         c = a+b
#         a,b = b,c
#     return b
# result = A(4)  
# print(result)

# #阶乘和
# def A(n):
#     a = 0
#     for i in range(1,n+1):
#         c = 1
#         for j in range(1,i+1):
#             c = c*j
#         a = a+c
#     print(a)
# A(3)        

# #单循环求阶乘和
# def A(n):
#     a = 0
#     for i in range(1,n+1):
#         c = 1
#         c = c*i
#     c +=c   
#     print('{}'.format(c))
# A(3)  

# class SequenceList:
# #初始化顺序表函数
#     def __init__(self):
#         self.SeqList=[]   
#     #创建顺序表函数
#     def CreateSequenceList(self):
#         print('*********************')
#         print('*请输入数据后按回车键确认，若想结束请输入"#"。*')
#         print('**********************')
#         Element=input('请输入元素:')
#         while Element !='#':
#             self.SeqList.append(int(Element))
#             Element=input('请输入元素:')
#     #查找元素值函数
#     def FindElement(self):
#         key = int(input('请输入想要查找的元素值:'))
#         if key in self.SeqList:
#             ipos = self.SeqList.index(key)
#             print('查找成功！值为',self.SeqList[ipos],'的元素，位于当前顺序表的第',ipos+1,'个位置。')
#         else:
#             print('查找失败！当前顺序表中不存在值为',key,'的元素') 
            
#     #指定位置插入元素函数的实现
#     def InsertElement(self):
#         Ipos = int(input('请输入待插入的位置:'))-1
#         Element =  int(input('请输入待插入的值:')) 
#         self.SeqList.insert(Ipos,Element)
#         print('插入后，当前顺序表：\n',self.SeqList)
        
#     #指定位置删除元素函数的实现
#     def DeleteElement(self):
#         dpos = int(input('请输入待删除元素的位置:'))
#         print('正在删除',self.SeqList[dpos],'...')
#         self.SeqList.remove(self.SeqList[dpos])
#         print('删除后的顺序表为:\n',self.SeqList)
        
#     #遍历顺序表元素函数的实现
#     def TraverseElement(self):
#         SequenceList = len(self.SeqList)
#         print('****遍历顺序表中的元素****') 
#         for i in range(0,SequenceList):
#             print('第',i+1,'个元素的值为',self.SeqList[i])                            
# # 使用示例  
# if __name__ == "__main__":  
#     seq_list = SequenceList()  
#     seq_list.CreateSequenceList()  
#     seq_list.FindElement()
#     seq_list.InsertElement()
#     seq_list.DeleteElement()
#     seq_list.TraverseElement()
#     print("顺序表内容:", seq_list.SeqList)

# #顺序表的应用
# class SequenceList:
# #初始化顺序表函数
#     def __init__(self):
#         self.SeqList={'赵小一':56,
#                       '钱小二':29,
#                       '孙小三':69,
#                       '李小四':95,
#                       '周小五':92,
#                       '吴小六':62,
#                       '郑小七':70,
#                       '王小八':50,
#                       '宁小九':80}
# #求取最大值与最小值
#     def GetExtremum(self):
#         while True:
#             print('*1:查询最大值')
#             print('*2:查询最小值')
#             print('*3:查询最大值与最小值')
#             print('*4:退出程序')
#             i = int(input('请输入:'))
#             if i == 1:
#                 print('顺序表中的最大值为:',max(self.SeqList.values()))
#             elif i == 2:
#                 print('顺序表中的最小值:',min(self.SeqList.values()))
#             elif i == 3:
#                 print('顺序表中的最大值为:',max(self.SeqList.values()))   
#                 print('顺序表中的最小值:',min(self.SeqList.values()))   
#             elif i == 4:
#                 break
# if __name__ == "__main__":  
#     seq_list = SequenceList()  
#     seq_list.GetExtremum()      
          
#单链表
class Node:
    def __init__(self,data):
        #初始化结点函数
        self.data = data
        self.next = None
class SingleLinKedList:
    def __init__(self):
    #初始化头节点函数
        self.head = Node(None)
    #创建单链表函数的实现
    def CreateSingleLinKedList(self):
        print('*请输入数据后按回车键确认，若想结束请输入#。*')
        cNode = self.head
        Element = input('请输入当前结点的值:')
        while Element !='#':
            nNode = Node(int(Element))
            cNode.next = nNode   #指向
            cNode = cNode.next   #结点
            Element = input('请输入当前结点的值:') 
    def print_list(self):  
        current_node = self.head.next  # 跳过哨兵节点  
        while current_node:  
            print(current_node.data, end=" -> ")  
            current_node = current_node.next  
        print("None")          
    #尾端插入元素函数
    def InsertElementInTail(self):
        Element = (input('请输入待插入结点的值:'))
        if Element =='#':
            return
        cNode = self.head
        nNode = Node(int(Element))
        while cNode.next != None:
            cNode = cNode.next
        cNode.next = nNode
    def A(self):  
        current = self.head.next  # 跳过哨兵节点  
        while current:  
            print(current.data, end=" -> ")  
            current = current.next  
        print("None")
    
    #首端插入元素
    def INsertElementInHead(self):
        Element = input('请输入待插入的结点:')
        if Element == '#':
            return
        cNode = self.head
        nNode = Node(int(Element))
        nNode.next = cNode.next
        cNode.next = nNode
    def jiejue(self):
        self.print_list() 
        
    #查找指定位置并返回其位置
    def FindElement(self):
        pos = 0
        cNode = self.head
        key = int(input('请输入想要查找的元素值:'))
        if self.IsEmpty():
            print('当前链表为空!')
            return
        while cNode.next !=None and cNode.data !=key:
            cNode = cNode.next
            pos = pos+1
        if cNode.data == key:
            print('查找成功，值为',key,'的结点位于该链表的第',pos,'个位置。')
        else:
            print('查找失败！当前单链表不存在值为',key,'的元素')        
    
    #判断单链表是不是为空函数
    def IsEmpty(self):
        if self.GetLength()==0:
            return True
        else:
            return False
    #获取单链表长度
    def GetLength(self):
        cNode = self.head
        length = 0
        while cNode.next !=None:
            length =length+1
            cNode = cNode.next
        return length 
    
    #删除元素函数
    def DeleteElement(self):
        dElement = int(input('请输入待删除结点的值:'))
        cNode = self.head
        pNode = self.head
        if self.IsEmpty():
            print('当前链表为空')
            return
        while cNode.next != Node and cNode.data !=dElement:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == dElement:
            pNode.next = cNode.next
            del cNode
            print('成功删除含有元素',dElement,'的结点')
        else:
            print('删除失败!当前链表中不存在含有元素',dElement,'的结点') 
    #遍历单链表函数
    def TraverseElement(self):
        cNode = self.head
        if cNode.next == None:
            print('当前链表为空！')
            return
        print('你当前的链表为：')
        while cNode !=None:
            cNode = cNode.next
            self.VisitElement(cNode)
    #输出单链表的元素
    def VisitElement(self,tNode):
        if tNode !=None:
            print(tNode.data,'->',end=" ")
        else:
            print('None')                                                       
              
if __name__ =='__main__':
    B = SingleLinKedList()
    B.CreateSingleLinKedList()
    B.print_list()
    B.InsertElementInTail()
    B.A()
    B.INsertElementInHead()
    B.jiejue()
    B.FindElement()
    B.DeleteElement()
    B.TraverseElement()
    
    
    