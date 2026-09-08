class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cursum, comb):
            nonlocal res
            if i>=len(nums):
                return
            if cursum > target:
                return
            elif cursum == target:
                res.append(comb.copy())
                return
        
            comb.append(nums[i])
            dfs(i, cursum+nums[i], comb)
            comb.pop()
            dfs(i+1, cursum, comb)

        dfs(0,0,[])
        return res