#括号匹配
def isValidParentheses(str):
    map = {'{':'}','[':']','(':')'}
    stack = []
    for s in str:
        if s == '{' or s == '[' or s == '(':
            stack.append(s)
        else:
            if not stack:
                return False
            if s != map[stack[-1]]:
                return False
            stack.pop()
    return not stack
                    

str = input()
print(isValidParentheses(str))