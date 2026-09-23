class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        #cache1 skips last value in nums
        #cache2 skips first value in nums
        cache1, cache2 = [0] * n, [0] * n

        cache1[0], cache1[1] = nums[0], max(nums[0], nums[1])
        cache2[1] = nums[1]

        for i in range(2, n - 1):
            cache1[i] = max(nums[i] + cache1[i - 2], cache1[i - 1])
        
        for j in range(2, n):
            cache2[j] = max(nums[j] + cache2[j - 2], cache2[j - 1])
        

        return max(cache1[-2], cache2[-1])
