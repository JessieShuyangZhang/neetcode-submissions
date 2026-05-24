class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_non0 = 1
        num_0s = 0
        for num in nums: 
            if num != 0:
                prod_non0 *= num
            else:
                num_0s += 1
        if num_0s > 1:
            return [0] * len(nums)
            
        for i, num in enumerate(nums): 
            if num == 0:
                nums[i] = prod_non0
            else:
                if num_0s > 0:
                    nums[i] = 0
                else:
                    nums[i] = prod_non0 // num
        return nums