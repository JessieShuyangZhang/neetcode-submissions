class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(numsset, perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for num in numsset:
                perm.append(num)
                dfs(numsset - {num}, perm)
                perm.pop()
        dfs(set(nums), [])
        return res