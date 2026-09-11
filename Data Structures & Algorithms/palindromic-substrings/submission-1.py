class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        count = n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if j-i <= 2:
                    dp[i][j] = (s[i] == s[j]) 
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                if dp[i][j]:
                    count += 1
        return count