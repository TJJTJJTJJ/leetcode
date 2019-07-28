#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (41.40%)
# Total Accepted:    302K
# Total Submissions: 725.2K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# method 1: leetcode给的第一种方法就挺好，数个数，然后直接改，哈哈哈
# method 2：用p_zero指向最后一个为0的数字，用p_second指向倒数最后一个为2的数字，然后不停地进行交换
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if not nums:
#             return None
#         p_zero, p_second = -1, len(nums)
#         while p_zero<len(nums)-1 and nums[p_zero+1]==0:
#             p_zero+=1
#         while p_second>0 and nums[p_second-1]==2:
#             p_second-=1
#         if p_zero==len(nums)-1 or p_second==0:
#             return None
#         i = p_zero+1
#         while i<p_second:
#             if nums[i]==0:
#                 nums[i], nums[p_zero+1]=nums[p_zero+1], nums[i]
#                 p_zero+=1
#                 while p_zero<len(nums)-1 and nums[p_zero+1]==0:
#                     p_zero+=1
#                 i = p_zero+1
#             elif nums[i]==2:
#                 nums[i], nums[p_second-1]=nums[p_second-1], nums[i]
#                 p_second-=1
#                 while p_second>0 and nums[p_second-1]==2:
#                     p_second-=1
#             else:
#                 i+=1
            
#         return None

# method 2.2 我刚刚算错了一个信息，交换之后可能会破坏原有规则，
# 并且是2交换后可能破坏0的规则，0交换后可能会破坏2的规则
# 这么一来，我也必须在交换之后重新保持一下既有规则
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if not nums:
#             return None
#         p_zero, p_second = -1, len(nums)
#         while p_zero<len(nums)-1 and nums[p_zero+1]==0:
#             p_zero+=1
#         while p_second>0 and nums[p_second-1]==2:
#             p_second-=1
#         if p_second-p_zero==1:
#             return None
#         i = p_zero+1
#         while i<p_second:
#             if nums[i]==0:
#                 nums[i], nums[p_zero+1]=nums[p_zero+1], nums[i]
#                 p_zero+=1
#                 while p_second>0 and nums[p_second-1]==2:
#                     p_second-=1
#             elif nums[i]==2:
#                 nums[i], nums[p_second-1]=nums[p_second-1], nums[i]
#                 p_second-=1
#                 while p_zero<len(nums)-1 and nums[p_zero+1]==0:
#                     p_zero+=1
#                 i = p_zero+1
#             else:
#                 i+=1
            
#         return None

# method 3 用 p_zero 指向即将放0的位置，用 p_second 指向即将放2的位置，虽然约束没有method2那么强，但是依然是很强的，操作是交换i与p_zero的值
# 其基本逻辑：
# if nums[i]==0:nums[i], nums[p_zero] = nums[p_zero], nums[i], p_zero++
# 如果指向的是即将放0的位置，可能会出现p_zero和i都是0的情况，交换之后p_zero可能与i相等甚至大于i的情况：0,0,0,0,2,1
# 针对这个问题的解法，衍生出多个版本
# method 3.1 不管p_zero是否为0，始终保持p_zero<i，针对的是0.0..即开始位置是两个0挨着的情况，其他情况下不会出现p_zero与i相等的情况
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         p_zero, p_second = 0, len(nums)-1
#         i = p_zero
#         while i <= p_second:
#             if nums[i]==0 and p_zero<i:
#                 nums[i], nums[p_zero] = nums[p_zero], nums[i]
#                 p_zero +=1
#             elif nums[i]==2 and i<p_second:
#                 nums[i], nums[p_second] = nums[p_second], nums[i]
#                 p_second-=1
#             else:
#                 i+=1
#         return None
# 
# 刚刚想了想，2,0,0 不管p_zero和p_second怎么指，交换之后都会破坏规则
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         p_zero, p_second = 0, len(nums)-1
#         while p_zeros<len(nums) and nums[p_zero]==0:
#             p_zero+=1
#         while p_second>-1 and nums[p_second]==2:
#             p_second-=1
#         if p_zero>p_second:
#             return None
#         i = p_zero
#         while i <= p_second:
#             if nums[i]

# method 4 用num0，num1，nums2记录0,1,2的个数，从前到后遍历的同时就直接更新之前的数组
# 0:0~nums0-1, 1:nums0~nums1-1, 2:nums1~nums2-1
# 这个方法具有通用性
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         n0, n1, n2 = -1, -1, -1
#         for val in nums:
#             if val == 0:
#                 n0, n1, n2 = n0+1, n1+1, n2+1
#                 nums[n2], nums[n1], nums[n0]  = 2, 1, 0
#             elif val == 1:
#                 n1, n2 = n1+1, n2+1
#                 nums[n2], nums[n1] = 2, 1
#             elif val == 2:
#                 n2+=1
#                 nums[n2] = 2
#         return None




