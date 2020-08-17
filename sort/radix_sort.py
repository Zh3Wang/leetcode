# coding=utf-8
'''
@File    :   radix_sort.py
@Time    :   2020/08/03 14:41:02
@Author  :   Wangzz 
@Desc    :   基数排序
'''

def radix_sort(lst_origin):
    for i in range(1,-1,-1):
        bucket = {}
        for j in lst_origin:
            # i => 排序的第几位,从最后一位开始排,到第0位
            pos = str(j)[i]
            if pos not in bucket.keys():
                bucket[pos] = []
            bucket[pos].append(j)
        
        # 将桶中的元素取出来
        lst_origin = []
        for k in range(10):
            if str(k) not in bucket.keys():
                continue
            for v in bucket[str(k)]:
                lst_origin.append(v)
    return lst_origin



lst = [34,51,42,14,22,65]
print(lst)
lst = radix_sort(lst)
print(lst)