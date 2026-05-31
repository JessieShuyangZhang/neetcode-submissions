class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r, res = 0, k-1, []
        heap = [(-x,index) for index, x in enumerate(nums[l:r])]
        heapq.heapify(heap)
        while r < len(nums):
            heapq.heappush(heap, (-nums[r],r))
            curmax, maxind = heap[0]
            while maxind<l:
                heapq.heappop(heap)
                curmax, maxind = heap[0]
            res.append(-curmax)
            l += 1
            r += 1

        return res
