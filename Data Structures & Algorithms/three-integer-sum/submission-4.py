class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = dict(Counter(nums))
        nums.sort()
        res = []

        for i in range(len(nums)): 
            counter[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                counter[nums[j]] -= 1
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                twosum = nums[i]+nums[j]
                if twosum > 0:
                    break
                if -twosum in counter and counter[-twosum] > 0:
                    res.append([nums[i],nums[j],-twosum])

            for j in range(i+1, len(nums)):
                counter[nums[j]] += 1

        return res