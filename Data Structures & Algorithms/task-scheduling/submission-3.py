class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0]*26
        for t in tasks:
            counter[ord(t)-ord('A')]+=1
        max_rep = max(counter)
        maxcount = 0
        for i in range(26):
            if counter[i] == max_rep:
                maxcount += 1   
        return max(len(tasks), (max_rep-1)*(n+1)+maxcount)