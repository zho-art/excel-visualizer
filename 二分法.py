def erfenfa(li,val):
    left = 0
    right = len(li)-1
    while left <= right:
        mid = (left + right)//2
        if li[mid] == val:
            return mid
        elif li[mid]>val:
            right = mid -1
        else:
            left = mid +1
    else:
        return None

li = [1,2,3,4,5,6,7]
print(erfenfa(li,3))                