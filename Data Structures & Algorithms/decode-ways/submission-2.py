class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == 0:
            return 0
        ways = [0]*(n+1)
        ways[-1] = 1
        ways[-2] = 0 if s[-1] == "0" else 1
        for i in range(n-2, -1, -1):
            if s[i] == "0":
                ways[i] == 0
            elif i+1<n and int(s[i:i+2]) > 26:
                ways[i] = ways[i+1]
            else:
                ways[i] = ways[i+1] + ways[i+2]
        return ways[0]
