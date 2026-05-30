class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        long, short = nums1, nums2
        if len(nums1) < len(nums2):
            long, short = short, long
        total = len(nums1) + len(nums2)
        half = total//2

        l,r = 0,len(short)-1
        while True:
            sc=(l+r)//2
            lc = half-(sc+1)-1
            shorta = short[sc] if sc>-1 else float('-inf')
            shortb = short[sc+1] if sc+1<len(short) else float('inf')
            longa = long[lc] if lc>-1 else float('-inf')
            longb = long[lc+1] if lc+1<len(long) else float('inf')
            if shorta<=longb and longa<=shortb:
                if total % 2 == 0:
                    return (max(shorta,longa)+min(shortb,longb))/2
                return min(shortb,longb)
            elif shorta>longb:
                r=sc-1
            else:
                l=sc+1
        



"""
[1,3, 5,7,9] len=5
[2,4, 6,8] len=4
total=9. half = 4. lc=

"""