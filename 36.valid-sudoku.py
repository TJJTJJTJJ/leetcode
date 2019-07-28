#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (41.98%)
# Total Accepted:    219.1K
# Total Submissions: 520.7K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
# 
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without
# repetition.
# 
# 
# 
# A partially filled sudoku which is valid.
# 
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠ ["5","3",".",".","7",".",".",".","."],
# ⁠ ["6",".",".","1","9","5",".",".","."],
# ⁠ [".","9","8",".",".",".",".","6","."],
# ⁠ ["8",".",".",".","6",".",".",".","3"],
# ⁠ ["4",".",".","8",".","3",".",".","1"],
# ⁠ ["7",".",".",".","2",".",".",".","6"],
# ⁠ [".","6",".",".",".",".","2","8","."],
# ⁠ [".",".",".","4","1","9",".",".","5"],
# ⁠ [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# [
# ["8","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being 
# ⁠   modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is
# invalid.
# 
# 
# Note:
# 
# 
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.
# 
# 
# method 1
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for i in range(9):
#             row_dict = dict()
#             col_dict = dict()
#             gong_dict = dict()
#             for j in range(9):
#                 if board[i][j]=='.' or row_dict.get(board[i][j], 0)==0:
#                     row_dict[board[i][j]] = 1
#                 else:
#                     return False
#                 if board[j][i]=='.' or col_dict.get(board[j][i], 0)==0:
#                     col_dict[board[j][i]] = 1
#                 else:
#                     return False
#                 x = 3*(i//3)+j//3
#                 y = 3*(i%3)+j%3
#                 if board[x][y]=='.' or gong_dict.get(board[x][y], 0)==0:
#                     gong_dict[board[x][y]] = 1
#                 else:
#                     return False
#         return True
# method 2 3 4 是对元素直接进行坐标标记，如果有效，那么这种坐标标记法是唯一的
# method 2 counter
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         import collections
#         coun = collections.Counter()
#         for i, row in enumerate(board):
#             for j, c in enumerate(row):
#                 if c!='.':
#                     coun.update(((c,i), (j,c), (c,i//3,j//3)))
#         max_item = max(list(coun.values())+[1])
#         return 1==max_item

# method 3 len(set)
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         board_list = []
#         for i, row in enumerate(board):
#             for j, c in enumerate(row):
#                 if c!='.':
#                     board_list.extend([(c,i), (j,c), (c,i//3,j//3)])
#         return len(board_list)==len(set(board_list))
# method 4 any
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         board_list = []
#         true_list = []
#         for i, row in enumerate(board):
#             for j, c in enumerate(row):
#                 if c!='.':
#                     for x in [(c,i), (j,c), (c,i//3,j//3)]:
#                         true_list.append(x in board_list or board_list.append(x))
#         return not any(true_list)
                
# method 2.1, 3.1, 4.1
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections
        return 1 == max(list(collections.Counter(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c!='.':
            for x in [(c,i), (j,c), (c,i//3,j//3)]
        ).values())+[1])

        seen = sum([[(c,i), (j,c), (c,i//3,j//3)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c!='.'], [])
        return len(seen)==len(set(seen))

        seen = set()
        return not any( x in seen or seen.add(x)
                        for i, row in enumerate(board)
                        for j, c in enumerate(row)
                        if c!='.':
                        for x in [(c,i), (j,c), (c,i//3,j//3)]
                        )


