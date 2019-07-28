#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (45.67%)
# Total Accepted:    217.5K
# Total Submissions: 472.2K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
# method 1
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         res = [0 for _ in range(n)]
#         for i in range(m):
#             for j in range(n):
#                 if i==0 and j>0:
#                     res[j]=res[j-1]+grid[i][j]
#                 elif j==0:
#                     res[j]+=grid[i][j]
#                 else:
#                     res[j]=min(res[j], res[j-1])+grid[i][j]
#         return res[-1]

# method 2
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = [float('inf') for _ in range(n)]
        res[0]=0
        for i in range(m):
            for j in range(n):
                if j==0:
                    res[j]+=grid[i][j]
                else:
                    res[j]=min(res[j],res[j-1])+grid[i][j]
        return res[-1]

