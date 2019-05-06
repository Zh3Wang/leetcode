class Stack:
    def __init__(self):
        self.stack = []
    def push(self,x):
        self.stack.append(x)
        
    def pop(self):
        if self.isEmpty():
            return
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        return not (len(self.stack) > 0)

stack = Stack()
stack.push(1)
stack.pop()
stack.pop()
print(stack.isEmpty())