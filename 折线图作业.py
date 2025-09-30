import pandas as pd  
import matplotlib.pyplot as plt
data = {  
    "普通本科":[721,738,749,761,791],  
    "中等职业教育": [620,601,593,582,557],  
    "普通高中": [797,797,803,800,793]  
}  
  
max_size = 100

class SString:
    def __init__(self):
        self.length=0
        self.ch=[None]*max_size

    def str_assign(self, s):
        n=len(s)
        if n >max_size-1:
            raise Exception('空间已满')
        else:
            self.length=0
            while self.length<n:
                self.length+=1
                self.ch[self.length]=s[self.length-1]
            return self
             
class SNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
  
class LString:
    def __init__(self):
        self.front = SNode()
        self.rear = self.front  
      
def index_bf(s, t, pos):
    i=pos
    j=1
    while i<=s.length and j<=t.length:
        if s.ch[i]==t.ch[j]:
            i+=1
            j+=1
        else:
            i=i-j+2
            j=1          
    if j>t.length:
        return i-t.length-1
    else:
        return -1

if __name__ == '__main__':
    s, t = SString(), SString()
    ss = input(); tt = input(); pos = 1
    print('主串{0}和字串{1}在第{2}个字符后首次匹配的位置为：'.format(ss, tt, pos),
        index_bf(s.str_assign(ss), t.str_assign(tt), pos))

    ss = input(); tt = input(); pos = 1
    print('主串{0}和字串{1}在第{2}个字符后首次匹配的位置为：'.format(ss, tt, pos),
        index_bf(s.str_assign(ss), t.str_assign(tt), pos))

    ss = input(); tt = input(); pos = 1
    print('主串{0}和字串{1}在第{2}个字符后首次匹配的位置为：'.format(ss, tt, pos),
        index_bf(s.str_assign(ss), t.str_assign(tt), pos))
