class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [[temperatures[0],0]] # pair: [temp, index]
        for i in range(1,n):
            while len(stack) > 0 and stack[-1][0] < temperatures[i] :
                t_pair = stack.pop()
                res[t_pair[1]] = i - t_pair[1]
            stack.append([temperatures[i],i])

        return res
