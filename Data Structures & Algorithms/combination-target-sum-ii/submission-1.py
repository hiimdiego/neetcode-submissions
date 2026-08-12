class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        subset = []
        candidates.sort()
        def dfs(i):
            if sum(subset) == target:
                if subset not in output:
                    output.append(subset.copy())
                return
            if i >= len(candidates):
                return
            subset.append(candidates[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return output