class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hp = nums
        heapq.heapify(self.hp)
        for i in range(len(nums)-k):
            heapq.heappop(self.hp) # get rid of the smallest n-k so that only k largest are kept

    def add(self, val: int) -> int:
        if len(self.hp) == self.k:
            if val > self.hp[0]:
                heapq.heappop(self.hp)
            else:
                return self.hp[0]
        heapq.heappush(self.hp, val)
        return self.hp[0]
