# coding=utf-8
'''
@File    :   radix_sort.py
@Time    :   2020/08/03 14:41:02
@Author  :   Wangzz 
@Desc    :   基数排序
'''

def radix_sort(lst_origin):
    length = len(lst_origin)
    for i in range(length-1,-1,-1):
        for j in lst_origin:
            # i => 排序的第几位,从最后一位开始排,到第0位
            


lst = [3,5,4,1,2,6]
print(lst)
lst = radix_sort(lst)
print(lst)