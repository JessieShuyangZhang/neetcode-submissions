class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1]*(amount+1)
        dp[0]=0
        coins.sort()

        for i in range(1,amount+1):
            for c in coins:
                if i<c:
                    continue
                elif i ==c:
                    dp[i] = 1
                else:
                    if dp[i-c] == -1:
                        continue
                    if dp[i] == -1:
                       dp[i] = 1+dp[i-c]
                    else:
                        dp[i]=min(dp[i],1+dp[i-c])
            
        return dp[-1]