class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        numIslands = 0
        seen = set()
        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            seen.add((i, j))
            while q:
                row, col = q.popleft()
                for r, c in ((row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)):
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in seen):
                        q.append((r,c))
                        seen.add((r,c))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in seen:
                    bfs(i, j)
                    numIslands += 1
        return numIslands