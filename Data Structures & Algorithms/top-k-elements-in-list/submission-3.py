class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = dict(Counter(nums))
        heap = [] # min heap
        res = []
        for num, freq in mp.items():
            heapq.heappush(heap,(freq,num))

            if len(heap) > k:
                heapq.heappop(heap) #remove item with smallest freq

        return [num for freq,num in heap]