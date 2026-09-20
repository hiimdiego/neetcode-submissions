class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        numIslands = 0
        seen = set()

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            seen.add((i, j))
            while q:
                r, c = q.popleft()
                for row, col in ((r+1, c), (r, c+1), (r-1,c), (r, c-1)):
                    if (row in range(rows) and col in range(cols) 
                    and grid[row][col] == "1" 
                    and (row, col) not in seen):
                        q.append((row, col))
                        seen.add((row, col))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in seen:
                    bfs(i, j)
                    numIslands += 1
        return numIslands