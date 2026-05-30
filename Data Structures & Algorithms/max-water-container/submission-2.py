class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_v = 0
        while l < r:
            v = min(heights[l], heights[r]) * (r - l)
            if v > max_v:
                max_v = v
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return max_v
