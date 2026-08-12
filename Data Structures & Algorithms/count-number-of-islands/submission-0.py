class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #check if grid is empty
        if not grid:
            return 0
        #initialize rows and cols
        rows, cols = len(grid), len(grid[0])
        #initialize visited and number of islands
        visit = set()
        islands = 0

        #define bfs traversal
        def bfs(i, j):
            q = collections.deque()
            visit.add((i, j))
            q.append((i, j))
            while q:
                m, n = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = m + dr, n + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
        #use row-order traversal 
        for i in range(rows):
            for j in range(cols):
                #check grid value
                if (grid[i][j] == "1" and (i, j) not in visit):
                    bfs(i, j)
                    islands += 1
        return islands
                