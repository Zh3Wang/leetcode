def search(lst,val):
    n = len(lst)
    low,high = 0,n-1
    while low <= high:
        mid = (low+high) // 2
        if lst[mid] < val:
            low = mid + 1
        else:
            if mid == 0 or lst[mid-1] < val:
                return mid
            else:
                high = mid - 1
    return -1
lst = [1,1,3,4,10,99,99,158,158,666]
pos = search(lst,10)
print(pos)


