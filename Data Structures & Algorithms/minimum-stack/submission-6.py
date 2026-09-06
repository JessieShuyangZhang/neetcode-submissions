class MinStack:

    def __init__(self):
        self.stack = []
        self.curmin = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.curmin.append(val)
        else:
            lastmin = self.curmin[-1]
            self.curmin.append(min(lastmin,val))
        self.stack.append(val)        

    def pop(self) -> None:
        self.stack.pop()
        self.curmin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curmin[-1]
