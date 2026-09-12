class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        if amount==0:
            return 0
        res = [amount+1] * (amount+1)
        res[0] = 0
        
        for current in range(1, amount+1):
            for c in coins:
                if c <= current:
                    res[current] = min(res[current], res[current-c]+1)
                    
        if res[amount] == amount+1:
            return -1
        return res[amount]