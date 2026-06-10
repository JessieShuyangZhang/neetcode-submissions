class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        res = [0] * (n+1)
        res[0],res[1] = 0,1
        for i in range(2,n+1):
            p = int(math.log2(i))
            r = i - 2**p
            res[i] = 1+res[r]
        return res

"""
num of 1s = 1 (highest 1) + num of 1s in the remainder

1000--1
1001--2
1010--2
1011--3
1100--2
1101--3
1110--3
1111--4
10000--1


"""