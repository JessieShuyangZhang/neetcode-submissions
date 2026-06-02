class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minh = [nums[i] for i in range(k)]
        heapq.heapify(minh)
        for i in range(k,len(nums)):
            if nums[i] > minh[0]:
                heapq.heappop(minh)
                heapq.heappush(minh,nums[i])
        return minh[0]