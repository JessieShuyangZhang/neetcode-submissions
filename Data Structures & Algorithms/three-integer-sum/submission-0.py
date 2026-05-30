class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            # skip duplicates - it has been covered in the last iteration
            if i >= 1 and num == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r] > -num:
                    r -= 1
                elif nums[l]+nums[r] < -num:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1

        return res


"""
nums = [-1,0,1,2,-1,-4]
srted= [-4,-1,-1,0,1,2]
"""