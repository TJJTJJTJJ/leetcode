#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (39.27%)
# Total Accepted:    227.7K
# Total Submissions: 575.8K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, val in enumerate(nums):
            if i>0 and val == nums[i-1]:
                continue
            for p in self.permuteUnique(nums[:i]+nums[(i+1):]) or [[]]:
                res.append([val]+p)
        return res

