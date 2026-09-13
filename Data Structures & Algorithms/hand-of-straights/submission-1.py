class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        numgroups = n // groupSize
        counter = dict(Counter(hand))
        minhp = list(counter.keys())
        heapq.heapify(minhp)
        while minhp: 
            smallest = heapq.heappop(minhp)
            groupcount = counter[smallest]
            counter[smallest] = 0
            for j in range(1, groupSize): 
                cnt = counter.get(smallest+j, 0)
                if cnt < groupcount:
                    return False
                counter[smallest+j] = cnt - groupcount
                if counter[smallest+j] == 0: 
                    if minhp[0] != smallest+j:
                        return False
                    heapq.heappop(minhp)
        return True