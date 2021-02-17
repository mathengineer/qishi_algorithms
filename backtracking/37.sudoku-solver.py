#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_size = len(board)

        def get_next(row, col):
            if col < board_size-1:
                return row, col+1
            elif row < board_size-1: # and col == board_size-1 implicitly
                return row+1, 0
            else:
                return None

        def validate_row(row, col, new_value):
            # the row is valid before adding the element at row, col
            # only need to check whether the new element the same as any other
            for n in board[row]:
                if new_value == n:
                    return False
            return True

        def validate_col(row, col, new_value):
            # similar to validate_row
            for i in range(board_size):
                if new_value == board[i][col]:
                    return False
            return True

        def find_threesome(i):
            if 0<=i<3:
                return (0, 1, 2)
            elif i<6:
                return (3, 4, 5)
            else:
                return (6, 7, 8)

        def validate_subbox(row, col, new_value):
            # similar to validate_row
            for i in find_threesome(row):
                for j in find_threesome(col):
                    if new_value == board[i][j]:
                        return False
            return True

        def validate(row, col, new_value):
            if validate_row(row, col, new_value) and validate_col(row, col, new_value) and validate_subbox(row, col, new_value):
                return True
            else:
                return False

        possible_values = [str(i) for i in range(1, 10)]

        def backtrack(row, col):
            while board[row][col] != '.':
                new_ind = get_next(row, col)
                if new_ind is None:
                    return True
                else:
                    row, col = new_ind

            for n in possible_values:
                if validate(row, col, n):
                    board[row][col] = n
                    new_ind = get_next(row, col)
                    if new_ind is None:
                        return True # only need one solution
                    else:
                        if backtrack(*new_ind):
                            return True
                        else:
                            board[row][col] = '.' # backtrack

        backtrack(0, 0)
        
# @lc code=end

