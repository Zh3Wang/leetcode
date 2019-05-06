#棒球游戏
def calPoints(ops):
    stack = []
    for v in ops:
        if v == 'C':
            stack.pop()
        elif  v == 'D':
            stack.append(stack[-1] * 2)
        elif v == '+':
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(v))
            
    return sum(stack)

print(calPoints(["5","-2","4","C","D","9","+","+"]))
