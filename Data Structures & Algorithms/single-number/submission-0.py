class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bitxor = 0
        for num in nums: 
            bitxor = bitxor^num
        return bitxor