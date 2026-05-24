class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        for num in nums:
            count = hashmap.get(num, 0) + 1
            if count > 1:
                return True
            hashmap.update({num: count})
        return False