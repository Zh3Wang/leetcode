class MinStack:
    def __init__(self):
        self.stack = []
        self.minItem = None
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minItem == None or self.minItem > x:
            self.minItem = x

    def pop(self) -> None:
        if not self.stack:
            return
        x = self.stack.pop() 
        if not self.stack:
            self.minItem = None
        elif x == self.minItem:
            self.minItem = x
       

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minItem

minStack = MinStack()
minStack.pop()
minStack.push(-3)
minStack.push(0)
minStack.push(-14)
print(minStack.getMin())
