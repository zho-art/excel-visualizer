max_size = 2
class SqStack:  
    def __init__(self, data=None):  
        self._elem = [None] * max_size  # 使用单下划线表示受保护的变量  
        self._top = 0  
        self._stack_size = max_size  
        if data is not None:  
            for e in data:  
                self.push(e) 
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
A = conversion(44445)
print(A)    

