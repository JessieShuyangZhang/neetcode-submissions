class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ways=[1]*(n+1)
        for i in range(n-1,-1,-1):
            if s[i] == '0':
                ways[i] = 0
            else:
                ways[i] = ways[i+1]
                if i == n-1:
                    continue
                double = ways[i+2]
                if int(s[i:i+2])>26:
                    double = 0
                ways[i] += double
        return ways[0]