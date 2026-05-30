class Solution:
    def trap(self, height: List[int]) -> int:
        maxr = maxl = 0
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                res += max(0, maxl - height[l])
                maxl = max(maxl, height[l])
                l += 1
            else:
                res += max(0, maxr - height[r])
                maxr = max(maxr, height[r])
                r -= 1
        return res