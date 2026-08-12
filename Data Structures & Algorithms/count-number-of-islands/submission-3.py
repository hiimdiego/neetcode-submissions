class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        numIslands = 0

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))
            while q:
                row, col = q.popleft()
                for r, c in [(row + 1, col),(row, col + 1),(row - 1, col),(row, col - 1)]:
                    if ((r, c) not in visited 
                    and r in range(rows) 
                    and c in range(cols) 
                    and grid[r][c] == '1'):
                        q.append((r, c))
                        visited.add((r, c))

            return
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    numIslands += 1
        return numIslands