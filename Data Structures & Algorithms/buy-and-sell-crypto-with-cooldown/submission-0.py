class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        for i in range(n-1,-1,-1):
            for canbuy in [True, False]:
                if canbuy: # hold no coin
                    buy = dp[i+1][0]-prices[i]
                    nobuy = dp[i+1][1]
                    dp[i][1] = max(buy,nobuy)
                else: # hold coin
                    sell = prices[i]+(dp[i+2][1] if i+2<=n else 0)
                    hold = dp[i+1][0]
                    dp[i][0] = max(sell,hold)
        return dp[0][1]