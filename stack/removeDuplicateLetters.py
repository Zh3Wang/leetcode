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