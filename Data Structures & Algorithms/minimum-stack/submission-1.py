class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = None
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.curr_min is None or val < self.curr_min:
            self.curr_min = val
        
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.curr_min:
            if self.stack:
                self.curr_min = min(self.stack)
            else:
                self.curr_min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min
