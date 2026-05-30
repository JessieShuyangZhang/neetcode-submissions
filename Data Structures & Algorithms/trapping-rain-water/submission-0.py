class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) 
        pref = [0] * n
        trapped = max_l = max_r = 0

        for l in range(1,n):
            max_l = max(max_l, height[l-1])
            pref[l] = max_l
        
        for r in range(n-2, -1, -1):
            max_r = max(max_r, height[r+1])
            t = (min(pref[r], max_r) - height[r])
            trapped += (t if t > 0 else 0)
            
        return trapped