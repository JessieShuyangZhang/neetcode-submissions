class Solution:
    def countBits(self, n: int) -> List[int]:
        p = 0
        res = []
        for i in range(n+1):
            res.append(bin(i).count('1'))
        return res

"""


4   100    1
5   101    2
6   110    2
7   111    3


1000--1
1001--2
1010--2
1011--3
1100--2
1101--3
1110--3
1111--4
10000--1


2^n-1: n
2^n: 1

2^(n+1)-1: n+1



"""