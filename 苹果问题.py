apples = 10
Sonny_apple = 2
xiaoli_applr = 4
liangren_apple = Sonny_apple + xiaoli_applr
xiaofeng_apple = apples - liangren_apple
print(liangren_apple,xiaofeng_apple)

def compress_array(arr):  
    if not arr:  
        return []  
  
    compressed = []  
    current_element = arr[0]   
    count = 1  
  
    for i in range(1, len(arr)): 
        if arr[i] == current_element:  
            count += 1  
        else:  
            compressed.append(current_element)    
            compressed.append(count)    
            current_element = arr[i]  
            count = 1    
    compressed.append(current_element)  
    compressed.append(count)  
    return compressed  
A = compress_array([1,2,2,3,3,3])
print(A)   


def brute_force_search(T, P):  
    n = len(T)   
    m = len(P)    
    for i in range(n - m + 1):    
        j = 0  
        while j < m and T[i + j] == P[j]:  
            j += 1  
        if j == m:  
            return i 
    return -1  
T = "HERE IS A SIMPLE EXAMPLE"  
P = "SIMPLE"  
print(brute_force_search(T, P))  
  
P = "NOT FOUND"  
print(brute_force_search(T, P)) 

def compute_next(P):  
    m = len(P)  
    next = [0] * m  
    k = -1  # next[0] is always -1  
    j = 0  
    while j < m - 1:  
        if k == -1 or P[j] == P[k]:  
            j += 1  
            k += 1  
            if P[j] != P[k]:  
                next[j] = k  
            else:  
                next[j] = next[k]  
        else:  
            k = next[k]  
    return next  
  
def KMP_search(T, P):  
    n = len(T)  
    m = len(P)  
    next = compute_next(P)  
    i = j = 0  
    positions = []  
  
    while i < n:  
        if P[j] == T[i]:  
            i += 1  
            j += 1  
        if j == m:  
            positions.append(i - j)  
            j = next[j - 1]   
        elif i < n and P[j] != T[i]:  
            if j != 0:  
                j = next[j - 1]  
            else:  
                i += 1  
  
    return positions  
  
T = input().strip()  
P = input().strip()  
positions = KMP_search(T, P)  
for pos in positions:  
    print(pos)