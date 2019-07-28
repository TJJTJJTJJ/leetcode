#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (42.83%)
# Total Accepted:    325.1K
# Total Submissions: 759.1K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
# # method 1
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         if len(height)==2:
#             return min(height)
        
#         max_area, i, j = 0, 0, len(height)-1
#         while i<j:
#             if height[i] < height[j]:
#                 max_area = max(max_area, height[i]*(j-i))
#                 i+=1
#             else:
#                 max_area = max(max_area, height[j]*(j-i))
#                 j-=1
#         return max_area

# method 1.1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==2:
            return min(height)
        
        max_area, i, j = 0, 0, len(height)-1
        while i<j:
            h = min(height[i], height[j])
            max_area, i, j = max(max_area, h*(j-i)), i+(height[i]==h), j-(height[j]==h)

        return max_area      

