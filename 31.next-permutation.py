#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (30.07%)
# Total Accepted:    217.9K
# Total Submissions: 724.3K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return
        len_nums = len(nums)
        j = len_nums-1
        while j>0 and nums[j]<=nums[j-1]:
            j-=1

        if j==0:
            self.swap(nums, 0, len_nums-1)
        else:
            k = len_nums-1
            while nums[k]<=nums[j-1]:
                k-=1
            nums[j-1], nums[k] = nums[k], nums[j-1]
            self.swap(nums, j, len_nums-1)

    def swap(self, nums, i, j):
        while i<j:
            nums[i], nums[j]=nums[j], nums[i]
            i+=1
            j-=1


