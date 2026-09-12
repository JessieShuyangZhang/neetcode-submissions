class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        maxlen = 1
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], 1+dp[j])
            maxlen = max(dp[i], maxlen)
        return maxlen