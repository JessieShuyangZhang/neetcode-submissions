class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxw = max(stones)
        bucket = [0] * (maxw+1)
        for s in stones:
            bucket[s] += 1
        first = second = maxw
        while first > 0:
            if bucket[first] % 2 == 0: # all stones cancel out
                first -= 1
                continue
            j = min(first-1, second) # try find the second heaviest
            while j > 0 and bucket[j] == 0:
                j -= 1
            if j == 0:
                return first 
            second = j
            newstone = first - second
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[newstone] += 1
            first = max(second, newstone)
        return first