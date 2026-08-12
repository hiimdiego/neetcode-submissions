class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Create hash sets
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        #use row-column traversal 
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if (val in rows[r] or val in cols[c] 
                    or val in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(val)
                rows[r].add(val)
                squares[(r // 3, c // 3)].add(val)
        return True