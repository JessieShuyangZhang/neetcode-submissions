class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removals = 0
        _, prevEnd = intervals[0]
        for i in range(1, len(intervals)):
            x, y = intervals[i]
            if x >= prevEnd: # no overlap
                prevEnd = y
            else:
                prevEnd = min(prevEnd, y)                     
                removals += 1
        return removals
