class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmax, curmin = 1, 1
        for num in nums:
            tmp = curmax * num
            curmax = max(num, num*curmin, num*curmax)
            curmin = min(num, num*curmin, tmp)
            res = max(res, curmax)

        return res