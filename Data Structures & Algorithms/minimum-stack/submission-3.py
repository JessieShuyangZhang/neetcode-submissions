class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')  

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.mini = val
        else:
            self.stack.append(val - self.mini)
            if val < self.mini: 
                self.mini = val

    def pop(self) -> None:
        if not self.stack: 
            return;
        encoded = self.stack.pop()
        if encoded < 0:
            self.mini = self.mini- encoded

    def top(self) -> int:
        encoded = self.stack[-1]
        if encoded > 0:
            return encoded + self.mini
        else: 
            return self.mini

    def getMin(self) -> int:
        return self.mini
