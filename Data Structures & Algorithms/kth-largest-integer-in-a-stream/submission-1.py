class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.klarge = []
        for x in nums: 
            if len(self.klarge) == k:
                if x > self.klarge[0]:
                    heapq.heappop(self.klarge)
                    heapq.heappush(self.klarge,x)
            else:
                heapq.heappush(self.klarge,x)
            

    def add(self, val: int) -> int:
        if len(self.klarge) == self.k:
            if val > self.klarge[0]:
                heapq.heappop(self.klarge)
                heapq.heappush(self.klarge,val)
        else:
            heapq.heappush(self.klarge,val)
        
        return self.klarge[0]