class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curmin, curmax = 0, 0
        for num in nums: 
            tmp = num + curmax
            curmax = max(num, num+curmax, num+curmin)
            curmin = min(num, tmp, num+curmin)
            res = max(res, curmax)
        return res