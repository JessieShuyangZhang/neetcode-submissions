class MedianFinder:

    def __init__(self):
        self.minheap = [] # the larger half of self.nums. 
        self.maxheap = [] # the smaller half of self.nums. 

    def addNum(self, num: int) -> None:
        if self.minheap and num >= self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)

        if len(self.minheap) - len(self.maxheap) > 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        elif len(self.maxheap) - len(self.minheap) > 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.minheap) < len(self.maxheap):
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0]+self.minheap[0])/2


"""
minheap: 3,4. [0]=3
maxheap: 1,2. [0]=2
num = 5

"""