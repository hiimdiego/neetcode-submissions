class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        output = []
        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()
        def dfs(i, j, visit, prevHeight):
            if ((i, j) in visit or i < 0 or j < 0 or i == rows 
            or j == cols or heights[i][j] < prevHeight):
                return
            visit.add((i, j))
            dfs(i + 1, j, visit, heights[i][j])
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols-1])

        for i in range(rows):
            for j in range(cols):
                if (i, j) in atl and (i, j) in pac:
                    output.append([i, j])
        return output