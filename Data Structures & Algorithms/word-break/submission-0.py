class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[n]=True
        for i in range(n-1,-1,-1):
            for j in range(n,i,-1):
                for word in wordDict:
                    if s[i:j]==word:
                        dp[i]= dp[i] or dp[j]
                        if dp[i]:
                            break
        return dp[0]