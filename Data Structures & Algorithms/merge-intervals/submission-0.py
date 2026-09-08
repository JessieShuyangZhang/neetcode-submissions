class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        for interval in intervals: 
            if not res:
                res.append(interval)
                continue
             
            a, b = res[-1]
            x, y = interval

            # if no overlap, simply append
            if b < x or y < a: 
                res.append(interval)
            # if overlaps, merge then append to res
            else:
                res.pop()
                merged=[min(a,x), max(b,y)]
                res.append(merged)
            
        return res