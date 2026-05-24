class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums: 
            mp[num] = mp.get(num,0) + 1
        heap = [(freq,num) for num,freq in mp.items()]

        k_largest = heapq.nlargest(k, heap)
        return [item[1] for item in k_largest]