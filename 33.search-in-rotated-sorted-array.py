#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (32.67%)
# Total Accepted:    378K
# Total Submissions: 1.2M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
# method 1
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if not nums:
#             return -1
#         a, b = nums[0], nums[-1]
#         if a<b:
#             a = b+1
#         p1, p2 = 0, len(nums)-1
#         res=-1
#         while p1<=p2:
#             p3 = (p1+p2)//2
#             if nums[p3]==target:
#                 res = p3
#                 break
#             if target>=a:
#                 if nums[p3]>=a and target>nums[p3]:
#                     p1=p3+1
#                 else:
#                     p2=p3-1
#             if target<a:
#                 if nums[p3]<a and target<nums[p3]:
#                     p2=p3-1
#                 else:
#                     p1=p3+1
#         return res

# method 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<=nums[r]:
                if nums[mid]<target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if nums[l]<=target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return -1

