class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            lastbit = (n >> i) & 1
            res += (lastbit << (31-i))
        return res