def sort(lst):
    n = len(lst)
    lst = quick_sort(lst,0,n-1)
    return lst

def quick_sort(lst,head,tail):
    if head >= tail:
        return
    
    pivot = partition(lst,head,tail)
    quick_sort(lst,head,pivot-1)
    quick_sort(lst,pivot+1,tail)
    
    return lst

def partition(lst,head,tail):
    pivot = lst[tail]
    i,j = head,head
    for j in range(head,tail):
        if lst[j] < pivot:
            lst[i],lst[j] = lst[j],lst[i]
            i += 1
    lst[i],lst[tail] = lst[tail],lst[i]
    return i

lst = [3,5,4,1,2,9,6,8]
print(lst)
lst = sort(lst)
print(lst)