class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #create a cache of amount + 1 entries
        cache = [amount+1] * (amount+1)
        cache[0] = 0
        #iterate from 1 to amount + 1
        for i in range(1, amount+1):
            #iterate over coins in array
            for c in coins:
                if i - c >= 0:
                    cache[i] = min(cache[i], 1 + cache[i-c])
        #if cache != amount + 1 return minCoins
        return cache[amount] if cache[amount] != amount+1 else -1