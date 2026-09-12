class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        wordset = set(wordDict)
        dp[-1] = s[-1] in wordset
        for i in range(n-2, -1, -1):
            dp[i] = s[i:] in wordset
            if dp[i] == True:
                continue
            for j in range(i+1, n):
                dp[i] = dp[j] and (s[i:j] in wordset)
                if dp[i] == True:
                    break
            
        return dp[0]