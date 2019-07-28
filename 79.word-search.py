#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (30.46%)
# Total Accepted:    266.6K
# Total Submissions: 865.4K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
# method 1
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not board or not board[0]:
#             return 
#         m = len(board)
#         n = len(board[0])
#         word = list(word)
#         k = len(word)
#         res = [False]
#         path = list()
#         def search(id, i, j, res, path):
#             if id == k:
#                 res[0] = True
#             if res[0] or i<0 or i>m-1 or j<0 or j>n-1:
#                 return
#             if word[id] == board[i][j] and ((i,j) not in path):
#                 path.append((i,j))
#                 search(id+1, i+1, j, res, path[:])
#                 search(id+1, i, j+1, res, path[:])
#                 search(id+1, i-1, j, res, path[:])
#                 search(id+1, i, j-1, res, path[:])
#         for x in range(m):
#             for y in range(n):
#                 search(0, x, y, res, path[:])
#         return res[0]

# 这里有两个问题
# 第一个：在成功时如何快速结束： 用 or ，当成功时，后面的都不会进行 
# 第二个：如何判断这个数字是否已经取过： 取过之后变成#，奸诈，在search之后再变回来
# 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word = list(word)
        k = len(word)
        def search(idx, i, j):
            if idx == k:
                return True
            if i<0 or i==m or j<0 or j==n:
                return False
            if word[idx] != board[i][j]:
                return False
            board[i][j]='#'
            res = search(idx+1, i+1, j) or \
                search(idx+1, i, j+1) or \
                search(idx+1, i-1, j) or \
                search(idx+1, i, j-1)
            board[i][j]=word[idx]
            return res
        for x in range(m):
            for y in range(n):
                if search(0, x, y):
                    return True
        return False
            


