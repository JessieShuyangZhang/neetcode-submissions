class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxh = [-i for i in nums]
        heapq.heapify(maxh)
        while k>1:
            heapq.heappop(maxh)
            k -= 1
        return -heapq.heappop(maxh)