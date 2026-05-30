class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []

        for i, h in enumerate(heights):
            leftbound = i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                maxarea = max(maxarea, height * (i - ind))
                leftbound = ind
            stack.append((leftbound, h))

        for leftbound, h in stack:
            maxarea = max(maxarea, h * (len(heights) - leftbound))

        return maxarea
