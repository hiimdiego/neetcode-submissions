class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def dfs(i, arr, total):
            if total == target:
                output.append(arr.copy())
                return
            if total > target or i > len(nums) - 1:
                return
            arr.append(nums[i])
            dfs(i, arr, total + nums[i])
            arr.pop()
            dfs(i + 1, arr, total)
        dfs(0, [], 0)
        return output