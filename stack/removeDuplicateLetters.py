#去除重复字符串
def removeDuplicateLetters(str):
    #将每个字符预先置为false,表示未处理，处理过的字符置为True
    visited = {}
    #遍历，获得每个字符出现次数
    dict = {}
    for c in str:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
        visited[c] = False
     
    stack = []
    len = 0
    for c in str:
        #遍历字符串，每个字符出现次数-1
        dict[c] -= 1
        #该字符为true的时候，表示处理过的，不再往下验证
        if visited[c]:
            continue
        while len > 0 and stack[-1] > c and dict[stack[-1]] > 0:
            visited[stack[-1]] = False
            stack.pop()
            len -= 1
        stack.append(c)
        visited[c] = True
        len += 1
    ans = ""
    for i in range(len):
        ans += stack[i]
    return ans

print(removeDuplicateLetters('cbacdcbc'))

'''
思路：
1、遍历字符串，统计每个字符出现次数，大于1则为重复出现的字符；同时，将每个字符置为False，用dict存储，如何dict[a] = False,这里是为了记录某个字符是否通过筛选条件，处理完毕;
2、声明用一个空stack栈来保存处理完成的字符result；
3、再一次遍历字符串，每次循环，当前字符的出现次数-1，如果 遇到已处理过的字符（即为True），跳过此次循环；
   while循环result栈，当满足以下三个条件时：不为空 and 栈顶元素（按照字典顺序排列）大于当前循环的字符 and 栈顶元素的出现次数大于0（重复字符）。将栈顶元素弹出并改为False，表明该元素不符合题目要求，淘汰掉
   继续执行后面代码，将当前字符入栈，置为True；
'''