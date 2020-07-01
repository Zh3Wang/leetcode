"""
    快速排序
"""

def quick_sort(lst,head,tail):
    if head >= tail:
        return
    
    pivot = partition(lst,head,tail)
    quick_sort(lst,head,pivot-1)
    quick_sort(lst,pivot+1,tail)
    
    return lst

def partition(lst,head,tail):
    #选任意一个元素作为分区点
    pivot = lst[tail]
    i,j = head,head
    for j in range(head,tail):
        if lst[j] < pivot:
            lst[i],lst[j] = lst[j],lst[i]
            i += 1
    lst[i],lst[tail] = lst[tail],lst[i]
    return i

lst = [3,6,7,4,1,2,9,8,5]
print(lst)
n = len(lst)
lst = quick_sort(lst,0,n-1)
print(lst)