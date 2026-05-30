class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftmin = [-1] * n
        rightmin = [n] * n

        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                leftmin[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                rightmin[i] = stack[-1]
            stack.append(i)

        maxarea = 0
        for i in range(n):
            area = (rightmin[i] - (leftmin[i] + 1)) * heights[i]
            maxarea = max(maxarea, area)

        return maxarea
