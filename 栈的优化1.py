max_size = 100
class SqStack:  
    def __init__(self, data=None):  
        self._elem = [None] * max_size  # 使用单下划线表示受保护的变量  
        self._top = 0  
        self._stack_size = max_size  
        if data is not None:  
            for e in data:  
                self.push(e)  

    def push(self, e):  
        if self._top == self._stack_size:  
            raise Exception('栈空间已满')  
        self._elem[self._top] = e  
        self._top += 1  
  
    def __str__(self):  
        return str(self._elem[:self._top])  # 返回栈中元素的字符串表示  
B = SqStack(['a', 'b', 'c', 'd','f'])  
print(B)  # 输出: ['a', 'b', 'c', 'd']

def conversion(n):
    s = SqStack()
    if n==0:
        print(0)
    else:
        while n:
            s.push(n%8)
            n = int(n//8)
        while not s.stack_empty():
            e = s.pop()
            print(e,end='')
A = conversion(44)
print(A)                

