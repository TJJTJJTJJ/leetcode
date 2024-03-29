#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (33.03%)
# Total Accepted:    271.3K
# Total Submissions: 821.4K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
# method 1
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        res = [-1, -1]
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if l==mid and nums[mid]==target:
                res[0]=mid
                break
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]==target:
                r = mid
            else:
                r = mid-1
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r+1)//2
            if r==mid and nums[mid]==target:
                res[1]=mid
                break
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]==target:
                l = mid
            else:
                r = mid-1
        return res        


