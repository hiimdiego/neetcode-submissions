class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                sub = subset.copy()
                sub.sort()
                if sub not in output:
                    output.append(sub)
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return output