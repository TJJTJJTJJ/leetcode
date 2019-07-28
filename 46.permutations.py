#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (53.57%)
# Total Accepted:    350.9K
# Total Submissions: 651K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
# method 1.0
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        if len(nums)==1:
            return [nums]
        res = list()

        for i, val in enumerate(nums):
            for permute in self.permute(nums[:i]+nums[(i+1):]):
                res.append([val]+ permute)
        return res

# method 1.1
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return [
#             [n]+p
#             for i, n in enumerate(nums)
#             for p in self.permute(nums[:i]+nums[(i+1):]) or [[]]
#         ]


