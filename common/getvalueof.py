# coding=utf-8
'''
@File    :   test2.py
@Time    :   2020/08/17 16:28:03
@Author  :   Wangzz 
@Desc    :   查找第K大的元素
'''

def get_value_of(lst,k,head,tail):
    if head >= tail:
        # 如果找到某一个分组的最后一个元素,还没找到K值,那当前这个元素就是第K大的元素
        return lst[tail]
    pivot = partition(lst,head,tail)
    if pivot+1 == k:
        val = lst[pivot]
    elif pivot+1 > k:
        val = get_value_of(lst,k,head,pivot-1)
    elif pivot+1 < k:
        val = get_value_of(lst,k,pivot+1,tail)
    return val

def partition(lst,head,tail):
    pivot = lst[tail]
    i,j = head,head
    for j in range(head,tail):
        if lst[j] < pivot:
            lst[j],lst[i] = lst[i],lst[j]
            i += 1
    lst[i],lst[tail] = lst[tail],lst[i]
    return i

lst = [8,3,1,5,2,17,12,6]
print(lst)
val = get_value_of(lst,5,0,len(lst)-1)
print(val)