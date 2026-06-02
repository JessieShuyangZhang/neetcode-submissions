class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.klarge = nums
        heapq.heapify(self.klarge)
        while len(self.klarge) > self.k: 
            heapq.heappop(self.klarge)

    def add(self, val: int) -> int:
        heapq.heappush(self.klarge,val)
        if len(self.klarge) > self.k: 
            heapq.heappop(self.klarge)
        
        return self.klarge[0]