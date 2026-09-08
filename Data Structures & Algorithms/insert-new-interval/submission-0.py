class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < n and not (intervals[i][0] > newInterval[1]):
            a, b = intervals[i][0], intervals[i][1]
            x, y = newInterval[0], newInterval[1]
            x = min(a, x)
            y = max(b, y)
            newInterval[0], newInterval[1] = x, y
            i += 1
        res.append(newInterval)
        while i < n: 
            res.append(intervals[i])
            i += 1
        return res