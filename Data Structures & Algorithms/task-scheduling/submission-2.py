class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0]*26
        for t in tasks:
            counts[ord(t)-ord("A")] += 1
        maxf = max(counts)
        maxcnt = 0
        for c in counts:
            if c == maxf:
                maxcnt += 1
        
        return max(len(tasks),(n+1)*(maxf-1)+maxcnt)