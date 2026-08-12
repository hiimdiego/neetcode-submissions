class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffToIdx = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in diffToIdx:
                return [diffToIdx[nums[i]], i]
            else:
                diffToIdx[diff] = i