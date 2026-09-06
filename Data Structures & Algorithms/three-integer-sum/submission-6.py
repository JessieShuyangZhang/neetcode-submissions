class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        counter = defaultdict(int)
        for num in nums: 
            counter[num] += 1

        for i in range(len(nums)):
            counter[nums[i]] -= 1
            if i>0 and nums[i-1]==nums[i]:
                continue

            for j in range(i+1,len(nums)):
                counter[nums[j]] -= 1
                if j>i+1 and nums[j-1]==nums[j]:
                    continue

                remain = -nums[j]-nums[i]
                if counter[remain] > 0:
                    res.append([nums[i],nums[j],remain])
            for j in range(i+1,len(nums)):
                counter[nums[j]] += 1
            
        return res