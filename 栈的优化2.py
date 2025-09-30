max_size = 100  
class SqStack:  
    def __init__(self, data=None):  
        self._elem = [None] * max_size  
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
    def pop(self):  
        if self.is_empty():  
            raise IndexError('pop from empty stack')  
        self._top -= 1  
        return self._elem[self._top]  
  
    def is_empty(self):  
        return self._top == 0  
  
    def __str__(self):  
        return str(self._elem[:self._top])
  
def conversion(n):  
    s = SqStack()  
    if n == 0:  
        print(0)  
    else:  
        while n:  
            s.push(n % 8)  
            n = n // 8  
        result = ""  
        while not s.is_empty():  
            result += str(s.pop())  
        return result  # 现在返回转换后的字符串
A = conversion(80)  
print(A)  