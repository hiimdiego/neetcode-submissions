class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        cache1, cache2 = [0] * len(nums), [0] * len(nums)

        cache1[0], cache1[1] = nums[0], max(nums[0], nums[1])
        cache2[1] = nums[1]

        for i in range(2, len(nums) - 1):
            cache1[i] = max(nums[i] + cache1[i-2], cache1[i-1])

        for j in range(2, len(nums)):
            cache2[j] = max(nums[j] + cache2[j-2], cache2[j-1])

        return max(cache1[-2], cache2[-1])

        #[0, 0, 0, 0, 0]
        #[2, 9, 0, 0, 0]
        #[2, 9, 10, 0, 0]
        #[2, 9, 10, 12, 0]

        #[0, 0, 0, 0, 0]
        #[0, 9, 0, 0, 0]
        #[0, 9, 9, 12, 15]
