def quick_sort(lst,head,tail):
    if head >= tail:
        return
    
    pivot = partioned(lst,head,tail)
    quick_sort(lst,head,pivot-1)
    quick_sort(lst,pivot+1,tail)
    
    return lst
    

def partioned(lst,head,tail):
    # 默认取最后一位数为分区点
    pivot = lst[tail]
    i,j = head,head
    for j in range(head,tail):
        if lst[j] < pivot:
            lst[i],lst[j] = lst[j],lst[i]
            i += 1
    lst[i],lst[tail] = lst[tail],lst[i]
    return i

lst = [8,3,1,5,2,17,12,5]
print(lst)
lst = quick_sort(lst,0,len(lst)-1)
print(lst)


