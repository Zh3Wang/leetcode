"""
    冒泡排序
"""
import numpy as np

def bubble_sort(lst):
    n = len(lst)
    for i in list(range(n)):
        flag = False 
        # 为什么要 (n-i-1)？
        # 每次冒泡操作都会确定一个元素的位置
        # 后续的冒泡操作无需对确定元素进行比较
        # i就是已确定元素的数量
        for j in list(range(n-i-1)):
            if lst[j] > lst[j+1]:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
                flag = True
        # flag参数表示若本次冒泡操作没有数据交换
        # 排序完成，提前结束循环
        if flag == False: 
            break
    return lst


lst = [3,5,4,1,2,6]
print(lst)
lst = bubble_sort(lst)
print(lst)