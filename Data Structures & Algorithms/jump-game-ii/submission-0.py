class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        minjumps = [float('inf') for i in range(n)]
        minjumps[0] = 0
        for i in range(n):
            for j in range(1, nums[i]+1):
                jumpto = min(i+j, n-1)
                minjumps[jumpto] = min(minjumps[jumpto], minjumps[i]+1)
        return minjumps[-1]
