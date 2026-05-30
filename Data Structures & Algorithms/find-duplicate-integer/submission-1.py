class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow2 == slow:
                return slow2
"""
fast = 2, slow = 1
fast = 2, slow = 2
slow2 = 0
slow = 3, slow2 = 1
slow = 2, slow2 = 2
"""



"""
 0 1 2 3 4
[2,1,3,4,2]
0 -> 2 -> 3 -> 4 -> 2
"""