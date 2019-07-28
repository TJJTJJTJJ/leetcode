#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (29.79%)
# Total Accepted:    215.8K
# Total Submissions: 723K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = list(nums)
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if N < 2 or len(nums)<N:
            return None
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if l>0 and nums[l-1]==nums[l]:
                    l+=1
                    continue
                if nums[l]+nums[r]==target:
                    results.append(result+[nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l]==nums[l-1]:
                        l+=1
                    while l < r and nums[r]==nums[r+1]:
                        r-=1
                if nums[l]+nums[r]>target:
                    r-=1
                if nums[l]+nums[r]<target:
                    l+=1
            return results
        
        if nums[-1]*N<target:
            return None

        for i in range(0, len(nums)-N+1):
            if nums[i]*N>target:
                return None
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        return


