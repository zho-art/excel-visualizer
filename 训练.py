import pandas as pd
import numpy as np
# #da1 = pd.DataFrame({'a':np.arange(1,5),
#                     'b':np.arange(2,6)})
# #print(da1)

# A = [pd.Series(np.arange(3)),pd.Series(np.arange(2))]
# pd5 = pd.DataFrame(A)
# #print(A)
# #print(pd5)
# B = pd5.iloc[0]
#print(B)

# ps1 = pd.Series(np.arange(5),index=['a','b','c','d','e'])
# ps1['g'] = 0
# print(ps1)
# s1 = pd.Series({'f':888})
# ps2 = ps1.append(s1)
# print(ps2)

# pd1 = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
# print(pd1)
# pd1.insert(1,'E',[9,99,999])
# print(pd1)
MAXSIZE = 5
#初始化
def _init_(self):
    self.elem = [None]*MAXSIZE
    self.top,self.base=0,0
    self.stack_size = MAXSIZE      #stack_size置为栈的最大容量MAXSIZE
#入栈
def  push(self,e):
    if self.top==self.base:
        raise Exception('栈已空')
    self.elem[self.top] = e
    self.top +=1
#出栈
def pop(self):
    if self.top == self.base:
        raise Exception('栈已空')
    self.top -=1
    return self.elem[self.top]
#取栈顶元素
def get_top(self):
    if self.top != self.base:
        return self.elem[self.top-1]
    else:
        raise Exception('栈已空')    
