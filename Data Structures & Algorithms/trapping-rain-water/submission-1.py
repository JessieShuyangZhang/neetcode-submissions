class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        res = max_l = max_r = 0
        while l < r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])
            if height[l] < height[r]:
                t = max_l - height[l]
                res += t if t > 0 else 0
                l += 1
            else:
                t = max_r - height[r]
                res += t if t > 0 else 0
                r -= 1

        return res
