class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0: 
            nn, m = divmod(n,2)
            if m == 1:
                res += 1
            n = nn
        return res