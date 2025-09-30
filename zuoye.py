import numpy as np
print(np.version)

A = np.full((10,),False,dtype=bool)
print(A)

import numpy as np
A = np.arange(10)
B = A.reshape((2,5))
print(B)

import numpy as np
A = np.arange(2,24,2)
new_arr = np.where(A % 2 == 0,0,A)
print(new_arr)

S = np.random.rand(10)
print(S)

A = np.arange(10)
new_arr = np.where(A % 2 == 1,-1,A)
print(new_arr)

A = np.random.randint(0,10,size=(4,4))
B = np.eye(4,k=1)
print(B)

import numpy as np
# 创建一个4行4列的数组
a = np.arange(16).reshape((4, 4))
# 取出(0,0)、(1,2)、(3,2)的点
points = [a[0, 0], a[1, 2], a[3, 2]]
print(points)  # 输出这些点的值

a = np.arange(16).reshape((4, 4))
A = a[1:3]
print(A)


a = np.random.randint(1,10,(8,9))
b = a[0:5, 7][a[0:5, 7] > 3]
print(a)
print(b)

a = np.arange(15)
b = a[(a) >= 5 & (a <= 10)]
print(b)


import numpy as np
# 创建一个二维数组
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 逆向行
reversed_rows = array[::-1, :]
# 逆向列
reversed_cols = array[:, ::-1]
print("原始数组:")
print(array)
print("逆向行:")
print(reversed_rows)
print("逆向列:")
print(reversed_cols)


