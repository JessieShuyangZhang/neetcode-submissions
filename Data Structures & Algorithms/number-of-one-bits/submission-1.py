class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        i=0
        for i in range(32):
            m = n & (1<<i)
            if m != 0:
                res += 1
        return res