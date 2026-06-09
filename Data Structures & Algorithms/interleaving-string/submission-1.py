class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1,n2,n3 = len(s1),len(s2),len(s3)
        if n3!=n1+n2:
            return False
        dp = [[False]*(n2+1) for i in range(n1+1)]
        dp[n1][n2]=True
        
        for i in range(n1,-1,-1):
            for j in range(n2,-1,-1):
                if i+j-1>=0 and i>0 and s3[i+j-1]==s1[i-1] and dp[i][j]:
                    dp[i-1][j] = True
                if i+j-1>=0 and j>0 and s3[i+j-1]==s2[j-1] and dp[i][j]:
                    dp[i][j-1] = True
        return dp[0][0]
        