"""
    归并排序
"""
import numpy as np

def merge_sort(lst):
    n = len(lst)
    lst = merge_sort_rec(lst,0,n-1)
    return lst

def merge_sort_rec(lst,head,tail):
    if head >= tail:
        return
    # 取数组的中间位置
    mid = (head+tail) // 2
    # 递归的方式排序左子数组
    merge_sort_rec(lst,head,mid)
    # 递归的方式排序右子数组
    merge_sort_rec(lst,mid+1,tail)
    # 合并排序好左右数组
    return merge(lst,head,mid,tail)

# 合并的过程
def merge(lst,head,mid,tail):
    # i和j分别指向两个待合并数组的起始位置
    i,j=head,mid+1
    tmp = []
    # i<= mid ，j<=tail表示待合并数组中还有元素
    while i <= mid and j <= tail:
        # 两个数组中的元素互相判断大小
        # 小的元素放到新的数组tmp中，同时i(j)的位置向后移动一位
        # 直到某一个待排序的数组为空
        if lst[i] <= lst[j]:
            tmp.append(lst[i])
            i += 1
        else:
            tmp.append(lst[j])
            j += 1
    
    # 再判断哪个待排序数组还有剩余元素
    # 一并添加到tmp数组中
    start,end = i,mid
    if j <= tail:
        start,end = j,tail
    while start <= end:
        tmp.append(lst[start])
        start += 1

    # 此时tmp数组中是已经合并且排序好的元素集合
    # 再将tmp数组放回原数组lst中
    for n in range(tail-head+1):
        lst[head+n] = tmp[n]
    
    return lst


lst = [5,3,4,6,2,1]
print(lst)
lst = merge_sort(lst)
print(lst)