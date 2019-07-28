#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (29.69%)
# Total Accepted:    217.6K
# Total Submissions: 728.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
# method 1
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         def spiral_coords(r1, c1, r2, c2):
#             for c in range(c1, c2+1):
#                 yield r1, c
#             for r in range(r1+1, r2+1):
#                 yield r, c2
#             if c1<c2 and r1<r2:
#                 for c in range(c2-1, c1, -1):
#                     yield r2, c
#                 for r in range(r2, r1, -1):
#                     yield r, c1

#         if not matrix:
#             return []
#         res = []
#         r1, r2 = 0, len(matrix)-1
#         c1, c2 = 0, len(matrix[0])-1
#         while r1<=r2 and c1<=c2:
#             for r, c in spiral_coords(r1, c1, r2, c2):
#                 res.append(matrix[r][c])
#             r1+=1; r2-=1
#             c1+=1; c2-=1
#         return res

# method 2
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)]+self.spiralOrder([*zip(*matrix)][::-1])



