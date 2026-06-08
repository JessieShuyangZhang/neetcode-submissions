class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        dp=[[0]*(amount+1) for i in range(n+1)]
        for i in range(n):
            dp[i][0]=1
        # for i in range(amount+1):
        #     dp[n][i]=0

        for i in range(n-1,-1,-1):
            for a in range(1, amount+1):
                if a >= coins[i]:
                    dp[i][a] += dp[i][a-coins[i]]
                dp[i][a] += dp[i+1][a]

        return dp[0][amount]