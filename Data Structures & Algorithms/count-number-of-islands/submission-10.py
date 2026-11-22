class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0
        q = deque()

        def bfs(i, j):
            q.append((i,j))
            while q:
                r, c = q.pop()
                nbrs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for (row, col) in nbrs:
                    if (row < rows and row >= 0 and col < cols and col >= 0 
                    and grid[row][col] == "1"):
                        grid[row][col] = "0"
                        q.append((row, col))

        
        #iterate through grid, and if space not visited and =1, run bfs
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    numIslands += 1
        return numIslands
        