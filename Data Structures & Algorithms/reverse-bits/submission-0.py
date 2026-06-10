class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            lastbit = n & 1
            if lastbit == 0:
                res = res << 1
            else:
                res = (res << 1) + 1
            n = n >> 1
        return res