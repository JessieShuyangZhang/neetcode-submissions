class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxheap = [-count for count in counts.values()]
        heapq.heapify(maxheap)
        t = 0
        cooldown = deque()
        while maxheap or cooldown:
            t += 1
            if not maxheap:
                t = cooldown[0][1]
            else:
                remain = heapq.heappop(maxheap) + 1
                if remain != 0:
                    cooldown.append([remain,t+n])
            
            if cooldown and t == cooldown[0][1]:
                # push to heap so that it executes on next t cycle
                heapq.heappush(maxheap,cooldown.popleft()[0])

        return t
