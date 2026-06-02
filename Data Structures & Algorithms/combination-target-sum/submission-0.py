class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, comb = [], []
        def recur(i, total):
            if total > target or i >= len(nums):
                return
            elif total == target:
                res.append(comb.copy())
                return
            comb.append(nums[i])
            recur(i,total+nums[i])
            comb.pop()
            recur(i+1,total)
                    
        recur(0,0)
        return res
