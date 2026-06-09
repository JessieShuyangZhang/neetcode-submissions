class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        # totalsum = sum(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1
        # dp[i][x] means the ways to get sum 'x' for the subarray nums[0:i)
        for i in range(1,n+1):
            for key,val in dp[i-1].items():
                dp[i][key+nums[i-1]] += (1*val)
                dp[i][key-nums[i-1]] += (1*val)

        return dp[n][target]