# coding=utf-8
'''
@File    :   test1.py
@Time    :   2020/08/17 14:51:27
@Author  :   Wangzz 
@Desc    :   输入 'aabbaa' 返回 1 aabbaa
             输入 'ababab' 返回 3 ab
             找出有几个连续相同的字母词组

'''

def test(s):
    l = len(s)+1
    for i in range(1,l):
        # 先按字母分割,从首位字母开始->全部字母
        subs = s.split(s[0:i])
        flag = True
        # 遍历分割后的数组
        for j in subs:
            # 如果不为空
            if j != '':
                flag = False
                break
        if flag == True:
            count = len(subs)-1
            value = s[0:i]
            break
        
    return count,value

lst = 'aabaa'
print(lst)
count,value = test(lst)
print(count,value)