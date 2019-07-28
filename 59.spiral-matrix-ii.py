#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (45.45%)
# Total Accepted:    130.7K
# Total Submissions: 285.5K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
# 
#
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = list([[]])
        start = n*n+1
        while start>1:
            start, end = start-len(A), start-1
            A = [list(range(start, end+1))]+list(zip(*A[::-1]))
        return A

