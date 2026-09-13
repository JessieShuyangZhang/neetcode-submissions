class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(cost) > sum(gas):
            return -1
        
        tank = 0
        startind = 0
        for i in range(n):
            res = i
            tank += gas[i]-cost[i]
            if tank < 0:
                tank = 0
                startind = i+1
        if startind >= n:
            return -1
        return startind