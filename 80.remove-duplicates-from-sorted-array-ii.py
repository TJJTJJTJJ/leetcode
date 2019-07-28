#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
#
# algorithms
# Medium (39.58%)
# Total Accepted:    194.4K
# Total Submissions: 487.3K
# Testcase Example:  '[1,1,1,2,2,3]'
#
# Given a sorted array nums, remove the duplicates in-place such that
# duplicates appeared at most twice and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# Example 1:
# 
# 
# Given nums = [1,1,1,2,2,3],
# 
# Your function should return length = 5, with the first five elements of nums
# being 1, 1, 2, 2 and 3 respectively.
# 
# It doesn't matter what you leave beyond the returned length.
# 
# Example 2:
# 
# 
# Given nums = [0,0,1,1,1,1,2,3,3],
# 
# Your function should return length = 7, with the first seven elements of nums
# being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
# 
# It doesn't matter what values are set beyond the returned length.
# 
# 
# Clarification:
# 
# Confused why the returned value is an integer but your answer is an array?
# 
# Note that the input array is passed in by reference, which means modification
# to the input array will be known to the caller as well.
# 
# Internally you can think of this:
# 
# 
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
# 
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
# 
# 先说一下我的思路 [1,1,1,1,2,2,3,3,] 当遇到nums[2]时，把nums[2]扔到最后面，nums[3:]全体前移一位
# 显然这种前移方式导致复杂度变大
# 这里提供的是两个指针用来前移，每次只前移一个非重复的元素，想不通两个是怎么等价的，但是这种前移思路应该分析记录一下
# method 1 我去，都是人才啊，这也行，用快慢指针，慢指针表示所求的数组，快指针表示原来数组
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         slow = 0
#         nums_len = len(nums)
#         count = 0
#         for fast in range(1, nums_len):
#             if nums[fast]==nums[slow]:
#                 count+=1
#             else:
#                 count = 0
#             if count < 2:
#                 nums[slow+1], nums[fast] = nums[fast], nums[slow+1]
#                 slow+=1
#         return slow+1

# method 2 对 method 1 的代码简化, idx指向即将放入的位置，计数器等效于idx-2和fast的大小比较
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if idx<2 or nums[idx-2]<num:
                nums[idx]=num
                idx+=1
        return idx

