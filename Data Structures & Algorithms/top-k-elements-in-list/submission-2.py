class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums: 
            mp[num] = mp.get(num,0) + 1

        freq = [[] for _ in range(len(nums)+1)]
        for num,f in mp.items():
            freq[f].append(num)

        res = []

        for freq_i in range(len(freq)-1,0,-1):
            for num in freq[freq_i]: 
                res.append(num)
                if len(res) == k: 
                    return res;
