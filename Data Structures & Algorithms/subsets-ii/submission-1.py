class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def dfs(ind, comb):
            if ind == len(nums):
                res.append(comb.copy())
                return
            
            comb.append(nums[ind])
            dfs(ind+1, comb)
            comb.pop()

            while ind+1 < len(nums) and nums[ind+1] == nums[ind]:
                ind += 1
            dfs(ind+1, comb)

        dfs(0,[])
        return res