class MedianFinder:

    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minheap

    def addNum(self, num: int) -> None:
        if len(self.large)>0 and num>self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-num)
        if len(self.small) - len(self.large) > 1:
            med = -heapq.heappop(self.small)
            heapq.heappush(self.large,med)
        elif len(self.large)-len(self.small)>1:
            med = heapq.heappop(self.large)
            heapq.heappush(self.small,-med)

    def findMedian(self) -> float:
        smalllen = len(self.small)
        largelen = len(self.large)
        if largelen > smalllen:
            return self.large[0]
        elif smalllen > largelen:
            return -self.small[0]
        else:
            return (-self.small[0]+self.large[0])/2
        