class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recur(ind, subset):
            if ind >= len(nums):
                res.append(subset.copy())
                return
            
            recur(ind+1, subset)
            subset.append(nums[ind])
            recur(ind+1, subset)
            subset.pop()

        recur(0, [])
        return res