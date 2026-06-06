class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        maxSoFar = [0] * n
        maxSoFar[0],maxSoFar[1] = nums[0],nums[1]
        for i in range(2,n):
            maxSoFar[i] = max(maxSoFar[0:i-1]) + nums[i] 
        return max(maxSoFar)