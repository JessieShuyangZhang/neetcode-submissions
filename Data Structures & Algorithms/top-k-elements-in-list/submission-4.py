class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = dict(Counter(nums))
        res = []
        freqlist = [[] for i in range(len(nums)+1)]
        for num,freq in mp.items(): 
            freqlist[freq].append(num)

        for i in range(len(freqlist)-1, 0, -1):
            for num in freqlist[i]:
                res.append(num)
                if len(res) == k:
                    return res
