class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [v for k,v in Counter(tasks).items()]
        counts.sort(reverse=True)
        maxf = counts[0]
        maxcnt = 1
        for i in range(1,len(counts)):
            if counts[i] == maxf:
                maxcnt += 1
            else:
                break
        return max(len(tasks),(n+1)*(maxf-1)+maxcnt)