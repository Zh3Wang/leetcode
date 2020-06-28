"""
    插入排序
"""
import numpy as np

def insertion_sort(lst):
    n = len(lst)
    for i in range(1,n):
        # 当前需要插入的元素
        # 默认从第二位开始
        # 第一位是已排序区间元素
        value = lst[i] 
        j = i - 1
        while j>=0 and lst[j] > value:
            # 循环遍历已排序数组
            # 寻找合适的位置，并挪动后面的元素
            lst[j+1] = lst[j]
            j = j - 1
        # 插入操作
        lst[j+1] = value
    return lst



lst = [3,5,4,1,2,6]
print(lst)
lst = insertion_sort(lst)
print(lst)