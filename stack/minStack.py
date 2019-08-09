class MinStack:
    def __init__(self):
        self.stack = []
        self.minItem = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        #如果最小值栈为空，直接入栈
        if not self.minItem:
            self.minItem.append(x)
        elif x <= self.minItem[-1]:
            self.minItem.append(x)
        
    def pop(self) -> None:
        if not self.stack:
            return
        x = self.stack.pop() 
        if x == self.minItem[-1]:
            self.minItem.pop()
       
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minItem[-1]

minStack = MinStack()
minStack.pop()
minStack.push(-3)
minStack.push(0)
minStack.push(-14)
print(minStack.getMin())
