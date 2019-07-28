#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.50%)
# Total Accepted:    492.4K
# Total Submissions: 2.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
# method 1
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums = list(nums)
        
#         nums.sort()
#         len_num = len(nums)
#         res = []
#         for i, a in enumerate(nums):
#             if a > 0 or i > len_num-3:
#                 break
#             if i>0 and a==nums[i-1]:
#                 continue
#             j, k = i+1, len_num-1
#             while j<k:
#                 s = a + nums[j] + nums[k]
#                 if s < 0:
#                     j+=1
#                 elif s > 0:
#                     k-=1
#                 else:
#                     res.append([a, nums[j], nums[k]])
#                     j+=1
#                     k-=1
#                     while nums[j]==nums[j-1] and j<k:
#                         j+=1
#                     while nums[k]==nums[k+1] and j<k:
#                         k-=1
                    
#         return res

# method 2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(nums)
        nums.sort()
        res = list()

        for i, a in enumerate(nums[:-2]):
            if a > 0:
                break
            if i>0 and a==nums[i-1]:
                continue
            tmp_d = dict()
            for b in nums[i+1:]:
                if b not in tmp_d:
                    tmp_d[-a-b]=1
                elif tmp_d.get(b)==1:
                    res.append([a,-a-b,b])
                    tmp_d[b]+=1
        return res


