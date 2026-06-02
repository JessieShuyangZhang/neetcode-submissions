class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], set()
        def dfs(i):
            if i == len(nums):
                res.append(list(subset))
                return

            # choice 1: include nums[i]
            subset.add(nums[i])
            dfs(i+1)

            subset.remove(nums[i])
            dfs(i+1)
        dfs(0)
        return res