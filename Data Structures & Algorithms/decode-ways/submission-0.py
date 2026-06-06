class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ways=[1]*n
        for i in range(n-1,-1,-1):
            if s[i] == '0':
                ways[i] = 0
            else:
                single = ways[i+1] if i+1<n else 1
                if i == n-1:
                    ways[i] = single
                    continue
                double = ways[i+2] if i+2<n else 1
                if int(s[i:i+2])>26:
                    double = 0
                ways[i]= single + double
        return ways[0]