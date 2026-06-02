class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, comb = [], []
        def recur(i, total):
            if total == target:
                res.append(comb.copy())
                return
            for j in range(i,len(nums)):
                if total+nums[j]>target:
                    return

                comb.append(nums[j])
                recur(j,total+nums[j])
                comb.pop()
                
        recur(0,0)
        return res
