class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arith = set(["+", "-", "*", "/"])
        for t in tokens: 
            if t in arith:
                second = int(stack.pop())
                first = int(stack.pop())
                if t == "+":
                    stack.append(first+second)
                elif t == '-':
                    stack.append(first-second)
                elif t == '*':
                    stack.append(first*second)
                else:
                    stack.append(int(first/second))

            else: 
                stack.append(int(t))
        return stack[0]