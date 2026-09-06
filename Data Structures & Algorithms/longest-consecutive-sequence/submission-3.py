class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [0,3,2,5,4,6,1,1]
        0: 1 -->7
        3: 2
        2: 2 --> 4 --> 5
        5: 1 --> 4
        4: 2+1+1=4. so 4 is now part of a 4-number sequence. boundaries: 3-(2-1)=2, 5+(1-1)=5. update 2, 5 values to 4
        6: 4+1=5  --> 7. boundaries: 5-(4-1)=2, 5+NULL. update 2 value to 5
        1: 1+1+5=7. 1 is now part of 7-num seq. boundaries: 0-(1-1)=0, 2+(5-1)=6. update 0,6 vals to 7
        """

        mp = defaultdict(int)  # num -> length of sequence that num is part of
        res = 0
        for num in nums:
            if num in mp:
                continue
            seqlen = mp.get(num - 1, 0) + 1 + mp.get(num + 1, 0)
            mp[num] = seqlen
            if num - 1 in mp:
                mp[num - 1 - (mp[num - 1] - 1)] = seqlen
            if num + 1 in mp:
                mp[num + 1 + (mp[num + 1] - 1)] = seqlen
            if seqlen > res:
                res = seqlen 
        return res