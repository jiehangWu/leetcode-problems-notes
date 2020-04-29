#   A valid sudoku must contain the digits 1 - 9 without reptition.
#   Each column must contain the digits 1 - 9 without reptition.
#   Each of the 9 3x3 sub-boxes of the grid must contain the digits 1 - 9 without reptiton.
#   The input of the board is a 2d matrix of strings with empty cell as ".".

#   Naturally, we would think of checking every row, column, and block with a hash set for 
#   repetitions of any number.
#   The order is row by row, but we can convert the row and col into corresponding cell
#   in the sub-box.

# board: List[List[str]]
def isValidSudoku(board):
    for i in range(len(board)):
        rows, cols, blocks = set(), set(), set()
        for j in range(len(board[0])):
            if board[i][j] != "." and board[i][j] in rows:
                return False
            else:
                rows.add(board[i][j])
            if board[j][i] != "." and board[j][i] in cols:
                return False
            else:
                cols.add(board[j][i])
            # compress/expand the matrix 
            block_r, block_c = i // 3 * 3 + j // 3, i % 3 * 3 + j % 3
            if board[block_r][block_c] != "." and board[block_r][block_c] in blocks:
                return False
            else:
                blocks.add(board[block_r][block_c])

    return True


inputTrue = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

inputFalse = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(inputTrue))
print(isValidSudoku(inputFalse))