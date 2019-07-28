#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (46.51%)
# Total Accepted:    270.7K
# Total Submissions: 577.7K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
# method 1
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         grid = [[-1 for _ in range(n)] for _ in range(m)]
#         grid[m-1][n-1], grid[m-2][n-1], grid[m-1][n-2]=0, 1, 1
#         def uniqueGrid(i, j):
#             if grid[i][j]!=-1:
#                 return grid[i][j]
#             if j==n-1:
#                 grid[i][j] = uniqueGrid(i+1, j)
#             elif i==m-1:
#                 grid[i][j] = uniqueGrid(i, j+1)
#             else:
#                 grid[i][j] = uniqueGrid(i+1, j)+uniqueGrid(i, j+1)
#             return grid[i][j]
#         return uniqueGrid(0,0)
        
# method 2 直接用C(m+n-2, n-1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        res = math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)
        return int(res)

