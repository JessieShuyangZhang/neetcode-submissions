class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums: 
            mp[num] = mp.get(num,0) + 1
        freq = [[] for _ in range(len(nums))]
        for num,f in mp.items():
            freq[f-1].append(num)
        res = []
        i = 0
        for freq_i in range(len(freq)-1,-1,-1):
            for num in freq[freq_i]: 
                if i == k: 
                    break;
                res.append(num)
                i += 1
                
        return res