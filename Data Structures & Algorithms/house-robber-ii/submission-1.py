class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=3:
            return max(nums)
        dp = [0]*(n-1) # for houses 0 ~ n-1
        dp1 = [0]*(n-1) # for houses 1 ~ n
        dp[0],dp[1] = nums[0],max(nums[:2])
        dp1[0],dp1[1]= nums[1],max(nums[1:3])
        for i in range(2,n-1):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        for i in range(2,n-1):
            house = i+1
            dp1[i] = max(dp1[i-2]+nums[house], dp1[i-1])
        return max(dp[-1],dp1[-1])