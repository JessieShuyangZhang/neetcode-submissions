class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total / 2
        running=0
        
        def recur(i, running):
            if i >= len(nums) or running > half: 
                return False
            elif running == half:
                return True
            return recur(i+1, running+nums[i]) or recur(i+1, running) 
        return recur(0, 0)
