class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1ton = (1+n)*n//2
        for num in nums:
            sum1ton -= num
        return sum1ton