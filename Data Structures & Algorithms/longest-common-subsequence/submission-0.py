class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1) # col
        n2 = len(text2) # row
        dp=[[0]*(n1+1) for i in range(n2+1)]
        for i in range(n2-1,-1,-1):
            for j in range(n1-1,-1,-1):
                if text1[j]==text2[i]:
                    dp[i][j]=dp[i+1][j+1]+1
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]