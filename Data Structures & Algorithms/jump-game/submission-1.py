class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        canreach = [False] * n
        canreach[0] = True
        for i in range(n):
            if canreach[i] == False:
                continue
            for j in range(1, nums[i]+1):
                if i+j < n:
                    canreach[i+j] = True
                else:
                    return True
        return canreach[-1]