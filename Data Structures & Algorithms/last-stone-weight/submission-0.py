class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>=2:
            y = -heapq.heappop(maxheap)
            x = -heapq.heappop(maxheap)
            if x == y:
                continue
            heapq.heappush(maxheap,x-y)
        return -maxheap[0] if len(maxheap) == 1 else 0