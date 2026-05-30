class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def recur():
            t = tokens.pop()
            if t not in "+-*/":
                return int(t)
            b = recur()
            a = recur()
            if t == '+':
                return a + b
            elif t == '-':
                return a - b
            elif t == '*':
                return a * b
            else: 
                return int(a/b)

        return recur()

"""
["4","13","5","/","+"]
t == +
--> t == / . return 5/13
    --> t == 5 return
    --> t == 13 return

"""