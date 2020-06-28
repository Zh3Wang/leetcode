"""
    选择排序
"""
import numpy as np

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        # 默认未排序区间第一个元素最小
        # min记录最小元素的index
        min = i
        # 然后从下一位元素开始遍历
        # 寻找最小值的index
        for j in range(i+1,n):
            if lst[j] < lst[min]:
                min = j
        # 如果min有改变，说明找到了更小的值
        # 交换原最小值和新最小值的位置
        if min != i:
            lst[i],lst[min] = lst[min],lst[i]
    return lst

lst = [3,5,4,1,2,6]
print(lst)
lst = selection_sort(lst)
print(lst)