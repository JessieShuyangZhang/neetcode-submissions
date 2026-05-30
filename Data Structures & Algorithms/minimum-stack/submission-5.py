class MinStack:

    def __init__(self):
        self.stack = []
        self.minsnap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        curmin = val
        if len(self.minsnap) != 0:
            curmin = min(val, self.minsnap[-1])
        self.minsnap.append(curmin)

    def pop(self) -> None:
        self.stack.pop()
        self.minsnap.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minsnap[-1]
