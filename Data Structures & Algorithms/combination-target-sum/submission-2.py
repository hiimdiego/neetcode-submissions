class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def dfs(i, subset, total):
            if total == target:
                output.append(subset.copy())
                return
            if total > target or i >= len(nums):
                return
            subset.append(nums[i])
            dfs(i, subset, sum(subset))
            subset.pop()
            dfs(i + 1, subset, sum(subset))
        dfs(0, [], 0)
        return output