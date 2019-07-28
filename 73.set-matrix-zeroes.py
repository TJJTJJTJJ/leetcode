#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (39.02%)
# Total Accepted:    197.6K
# Total Submissions: 502.9K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
# method 1
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         # leetcode 给的第三种方法有点意思哈，
#         # 相当于把第一种方法的行列记录放在了矩阵里面
#         is_col = False
#         R = len(matrix)
#         C = len(matrix[0])
#         for i in range(R):
#             if matrix[i][0] == 0 and (not is_col):
#                 is_col = True
#             for j in range(1, C):
#                 if matrix[i][j]==0:
#                     matrix[i][0]=0
#                     matrix[0][j]=0
#         for i in range(1,R):
#             for j in range(1,C):
#                 if (not matrix[i][0]) or (not matrix[0][j]):
#                     matrix[i][j]=0
#         if (not matrix[0][0]):
#             for j in range(1,C):
#                 matrix[0][j]=0
#         if is_col:
#             for i in range(R):
#                 matrix[i][0]=0
#         return None

# method 2 对 method 1 的赋0进行优化
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         # leetcode 给的第三种方法有点意思哈，
#         # 相当于把第一种方法的行列记录放在了矩阵里面
#         is_col = False
#         R = len(matrix)
#         C = len(matrix[0])
#         for i in range(R):
#             if matrix[i][0] == 0 and (not is_col):
#                 is_col = True
#             for j in range(1, C):
#                 if matrix[i][j]==0:
#                     matrix[i][0]=0
#                     matrix[0][j]=0
#         for i in range(R,-1,-1):
#             if is_col:
#                 matrix[i][0]=0
#             for j in range(C, 0, -1):
#                 if (not matrix[i][0]) or (not matrix[0][j]):
#                     matrix[i][j]=0

#         return None

        
# method 3
# 这个想法有点6，是直接把leetcode的方法1的列表存储成一个二进制的数字，
# 这个方法的空间复杂度是O(lg(n)/8+lg(m)/8)，可能对最理想的情况或者使用的编程语言有限制
# 并且用位运算符代替了普通的加减乘除
# 点睛之笔 r = r | (1<<i) 和 (r>>i)%2==1
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = 0
        c = 0
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            for j in range(C):
                if matrix[i][j]==0:
                    r = r | (1<<i)
                    c = c | (1<<j)
        for i in range(R):
            for j in range(C):
                if ((r>>i)%2==1) or ((c>>j)%2==1):
                    matrix[i][j]=0
        return None



