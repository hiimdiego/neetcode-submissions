class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        f0, f1 = 1, 1
        for i in range(1, n):
            f2 = f0 + f1
            f0 = f1
            f1 = f2
        return f2