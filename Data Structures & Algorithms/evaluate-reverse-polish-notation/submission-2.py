class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for c in tokens: 
            if c == '+' or c == "-" or c == "*" or c == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                if c == '+':
                    stack.append(a+b)
                elif c == "-":
                    stack.append(a-b)
                elif c == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(c)

        return stack[-1]