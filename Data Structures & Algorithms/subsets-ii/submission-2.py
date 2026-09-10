class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def recur(ind, subset):
            if ind == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[ind])
            recur(ind+1, subset)
            subset.pop()
            while ind+1<len(nums) and nums[ind] == nums[ind+1]:
                ind += 1
            recur(ind+1, subset)
        recur(0,[])
        return res