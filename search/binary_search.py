"""
    二分查找
"""
#迭代法
def binary_search(lst,val):
    n = len(lst)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low+high) // 2
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            low = mid + 1
        elif lst[mid] > val:
            high = mid - 1
    
    return -1

#递归
def binary_search_rec(lst,val):
    n = len(lst)
    low,high = 0,n-1
    return search(lst,low,high,val)

def search(lst,low,high,val):
    if low > high:
        return -1
    mid = (low+high)//2
    if lst[mid] == val:
        return mid
    elif lst[mid] < val:
        return search(lst,mid+1,high,val)
    elif lst[mid] > val:
        return search(lst,low,mid-1,val)

lst = [1,1,3,4,10,99,1,158,666]
pos = binary_search_rec(lst,1)
print(pos)