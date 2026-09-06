class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lefts = set(['(',  '{', '['])
        for c in s: 
            if c in lefts:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack[-1]
                if (last == '{' and c == '}') or (last == '[' and c == ']') or (last == '(' and c == ')'):
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False

        return True