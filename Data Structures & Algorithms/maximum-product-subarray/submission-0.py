class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = nums[0]
        curMin, curMax = 1, 1
        for num in nums:
            tmp = curMax * num
            curMax = max(tmp, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            output = max(output, curMax)
        return output