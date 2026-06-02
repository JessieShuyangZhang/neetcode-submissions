class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        bucket = [0] * 100
        for s in stones:
            bucket[s-1] += 1
        first,second,i = 0,0,99
        while i > -1:
            if first==0 or second==0:
                if bucket[i] == 1:
                    if first == 0:
                        first = i+1
                    else: 
                        second = i+1
                    bucket[i] = 0
                elif bucket[i] >= 2:
                    if first == 0:
                        first = second = i+1
                        bucket[i] -= 2
                    else: 
                        second = i+1
                        bucket[i] -= 1
                    
            if first > 0 and second > 0:
                if first != second:
                    w = first - second
                    bucket[w-1] += 1
                    if i < w-1:
                        i = w-1
                first = second = 0
            if bucket[i] == 0:
                i -= 1

        if first!=0 and second == 0:
            return first
        else:
            return 0