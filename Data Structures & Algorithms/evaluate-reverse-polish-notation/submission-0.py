class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])
        for t in tokens: 
            if t in ops:
                b = int(stack.pop())
                a = int(stack.pop())
                c = 0
                if t == '+':
                    c = a + b
                elif t == '-':
                    c = a-b
                elif t == '*':
                    c = a*b
                else:
                    c = int(a/b) # -9//4
                stack.append(c)
            else:
                stack.append(int(t))
        return stack[-1]