class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Create hash_set for each 3x3 subblock
        sub_blocks = {i: set() for i in range(9)}
        #Iterate through sudoku block
        for i in range(0, 9):
            #Create sets for each row and column in sudoku block
            row = set()
            col = set()
            for j in range(0, 9):
                #Check if val exists in each row and column
                if ((board[i][j] in row) or (board[j][i] in col)):
                    return False
                #Add val to each set only if its valid
                if (board[i][j] != "."):
                    row.add(board[i][j])
                if (board[j][i] != "."):
                    col.add(board[j][i])
                #Check if val exists in each square
                square_idx = int(i / 3) * 3 + int(j / 3)
                if (board[i][j] in sub_blocks[square_idx]):
                    return False
                if (board[i][j] != "."):
                    sub_blocks[square_idx].add(board[i][j])
        return True