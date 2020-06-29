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
        return True
    mid = (head+tail) / 2
    merge_sort_rec(lst,head,mid)
    merge_sort_rec(lst,mid+1,tail)

    merge(lst[head:tail],lst[head:mid],lst[mid+1,tail])


def merge(lst,lst1,lst2):
    pass

lst = [3,5,4,1,2,6]
print(lst)
lst = merge_sort(lst)
print(lst)