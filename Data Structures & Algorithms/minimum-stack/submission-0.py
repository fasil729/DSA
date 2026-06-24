class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(min(val, self.stack[-2]))
        else:
            self.stack.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[-2]
        
