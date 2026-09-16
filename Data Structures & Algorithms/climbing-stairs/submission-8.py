class Solution:
    def climbStairs(self, n: int) -> int:
        #Base case
        if n <= 2:
            return n
        #Create cache
        cache = [0] * (n + 1)
        #initialize first and second elements
        cache[1], cache[2] = 1, 2
        #iterate over n and build cache
        for i in range (3, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]
            
