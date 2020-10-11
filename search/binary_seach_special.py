"""
    二分查找变种
"""

# 查找第一个符合指定value的位置
def b_search_first(lst,val):
    n = len(lst)
    low,high = 0,n-1
    while low <= high:
        mid = (low+high) // 2
        if lst[mid] < val:
            low = mid + 1
        elif lst[mid] > val:
            high = mid - 1
        else:
            #如果找到相等的值，判断其是否第0位 或者 他的前一位是否相等
            #否则，目标值在[low,mid-1]中，继续二分查找过程
            if mid == 0 or lst[mid-1] != val:
                return mid
            else:
                high = mid - 1
        
    return -1

#查找最后一个符合条件的值
def b_search_last(lst,val):
    n = len(lst)
    low,high = 0,n-1
    while low <= high:
        mid = (low+high) // 2
        if lst[mid] < val:
            low = mid + 1
        elif lst[mid] > val:
            high = mid - 1
        else:
            #如果找到相等的值，判断其是否最后一位 或者 他的后一位是否相等
            #否则，目标值在[mid+1,high]中，继续二分查找过程
            if mid == n-1 or lst[mid+1] != val:
                return mid
            else:
                low = mid + 1
        
    return -1

#查找第一个大于等于value的值
def b_search_big(lst,val):
    n = len(lst)
    low,high = 0,n-1
    while low <= high:
        mid = (low+high)//2
        if lst[mid] < val:
            low = mid + 1
        else:
            #如果mid的值大于或等于val，此时要满足第一个的条件，必须是“第一位”或“前一位小于val”
            if mid == 0 or lst[mid-1] < val:
                return mid
            else:
                high = mid - 1
    return -1      

#查找最后一个小于等于value的值
def b_search_big_last(lst,val):
    n = len(lst)
    low,high = 0,n-1
    while low <= high:
        mid = (low+high)//2
        if lst[mid] > val:
            high = mid - 1
        else:
            if mid == n-1 or lst[mid+1] > val:
                return mid
            else:
                low = mid + 1
    return -1


lst = [1,1,3,4,10,99,99,158,158,666]
pos = b_search_big_last(lst,158)
print(pos)