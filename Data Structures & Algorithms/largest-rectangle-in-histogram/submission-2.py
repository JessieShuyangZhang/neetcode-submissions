class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lowleft = [-1] * n
        lowright = [n] * n
        stack= [] # (height, index)
        for i in range(n):
            while len(stack)>0 and stack[-1][0] > heights[i]:
                x = stack.pop()
                lowright[x[1]] = i
            stack.append((heights[i],i))
        
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack)>0 and stack[-1][0] > heights[i]:
                x = stack.pop()
                lowleft[x[1]] = i
            stack.append((heights[i],i))
        
        maxa = 0
        for i in range(n):
            a = (lowright[i]-lowleft[i]-1)*heights[i]
            maxa = max(maxa, a)
        return maxa

"""
[6,6,6,6,6,6]
stack:[(1,1),(7,2)]

[-1,-1,-1,-1,-1,-1]
stack: []
"""