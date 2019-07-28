#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (34.69%)
# Total Accepted:    213.7K
# Total Submissions: 615K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Example 1:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
# 
# method 1 右上到左下 O(m+n)
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if (not matrix) or (not matrix[0]) or target is None:
#             return False
#         R = len(matrix)
#         C = len(matrix[0])
#         i, j = 0, C-1
#         while i<R and j>-1:
#             if matrix[i][j]==target:
#                 return True
#             elif matrix[i][j]>target:
#                 j-=1
#             elif matrix[i][j]<target:
#                 i+=1
#         return False

# method 2 
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if (not matrix) or (not matrix[0]) or target is None:
#             return False
#         R, C = len(matrix), len(matrix[0])
#         l, r = 0, R*C-1
#         while l<=r:
#             mid = (l+r)//2
#             num = matrix[mid//C][mid%C]
#             if num == target:
#                 return True
#             elif num<target:
#                 l = mid+1
#             else:
#                 r = mid-1
#         return False

# method 3 考虑了m*n可能溢出，所以先找到在哪行，再判断在哪列 O(lg(m)+lg(n))
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if (not matrix) or (not matrix[0]) or target is None:
#             return False
#         R, C  = len(matrix), len(matrix[0])
#         l, r = 0, R-1
#         while l<=r:
#             mid = (l+r)//2
#             if matrix[mid][0]<=target and target<=matrix[mid][-1]:
#                 break
#             elif matrix[mid][0]<target:
#                 l = mid+1
#             else:
#                 r = mid-1
#         fix_row = mid
#         l, r = 0, C-1
#         while l<=r:
#             mid = (l+r)//2
#             if matrix[fix_row][mid]==target:
#                 return True
#             elif matrix[fix_row][mid]<target:
#                 l = mid+1
#             else:
#                 r = mid-1
#         return False


# method 4 利用python自带的二分查找类bisect bisect.bisect:二分查找 bisect.insort:插入排序 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (not matrix) or (not matrix[0]) or target is None:
            return False
        import bisect
        i = bisect.bisect_left(matrix, [target])
        if i<len(matrix) and matrix[i][0]==target:
            return True
        row = matrix[i-1]
        j = bisect.bisect_left(row, target)
        if j<len(row) and row[j]==target:
            return True
        else:
            return False


