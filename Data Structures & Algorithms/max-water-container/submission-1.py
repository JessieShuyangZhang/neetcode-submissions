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
            elif heights[l] < heights[r]:
                l += 1
            else:
                if l + 1 < r - 1:
                    if heights[l + 1] > heights[r - 1]:
                        l += 1
                    else:
                        r -= 1
                else:
                    l += 1  # doesn't matter
        return max_v

"""
 0 1 2 3 4 5 6 7
[1,7,2,5,4,7,3,6]

l = 0, r = 7, v = 7    max_v = 7
l = 1, r = 7, v = 36   max_v = 36
"""
