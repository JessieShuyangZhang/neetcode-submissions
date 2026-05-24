class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1] * len(nums)
        for i, num in enumerate(nums): 
            for j in range(len(prods)):
                if j != i:
                    prods[j] *= num
        return prods

