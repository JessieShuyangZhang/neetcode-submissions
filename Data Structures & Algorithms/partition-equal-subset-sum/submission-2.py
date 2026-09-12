class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        n = len(nums)
        dp = [[-1]*(half+1) for i in range(n)]

        # dp[i][t]: whether it’s possible to form sum t using elements from index i onward
        def recur(i, target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0: 
                return False
            if dp[i][target] != -1:
                return dp[i][target]
            dp[i][target] = recur(i+1, target-nums[i]) or recur(i+1, target) 
            return dp[i][target]
        return recur(0, half)
