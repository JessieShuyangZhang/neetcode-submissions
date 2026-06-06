class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mincost = [float('inf')]*n
        mincost[0], mincost[1] = 0,0
        for i in range(2,n):
            mincost[i] = min(mincost[i-1]+cost[i-1], mincost[i-2]+cost[i-2])
        return min(mincost[n-1]+cost[n-1], mincost[n-2]+cost[n-2])