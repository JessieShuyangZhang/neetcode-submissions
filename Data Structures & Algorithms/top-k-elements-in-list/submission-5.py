class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        res = []
        for num in nums: 
            counter[num] += 1
        heap = []
        for num, freq in counter.items():
            heap.append((-freq,num))
        heapq.heapify(heap)
        for i in range(k):
            f,v = heapq.heappop(heap)
            res.append(v)
        return res