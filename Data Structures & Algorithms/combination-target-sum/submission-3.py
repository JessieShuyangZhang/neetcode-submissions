class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def recur(ind, comb, cursum):
            if cursum == target:
                res.append(comb.copy())
                return
            if ind >= len(nums) or cursum > target:
                return
            
            comb.append(nums[ind])
            recur(ind, comb, cursum + nums[ind])
            comb.pop()
            recur(ind+1, comb, cursum)
        recur(0, [],0)
        return res