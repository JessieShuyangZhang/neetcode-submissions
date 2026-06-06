class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmax, curmin = 1,1
        for num in nums:
            tmp = num*curmax
            curmax = max(tmp,num*curmin,num)
            curmin = min(tmp,num*curmin,num)
            res = max(res,curmax)
        return res