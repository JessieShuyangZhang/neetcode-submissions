class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        res = s[0]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i >= j:
                    continue
                if j-i <= 2:
                    dp[i][j] = (s[i] == s[j]) 
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                if dp[i][j] and len(res)<(j-i+1):
                    res = s[i:j+1]
        """
        if s[i:j+1] is a palindrome, then dp[i][j] = True 
        dp[i][j] = True and s[i] == s[j] --> dp[i-1][j+1] = true
        """
        return res