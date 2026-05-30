class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, ind)
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while len(stack) != 0 and t > stack[-1][0]:
                found = stack.pop()
                res[found[1]] = i - found[1]
                
            stack.append((t,i))
        return res