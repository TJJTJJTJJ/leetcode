#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (46.15%)
# Total Accepted:    193.5K
# Total Submissions: 413.6K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
# method 1 利用递归
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
        
#         if k == 0:
#             return []
#         n_list = list(range(1,n+1))
#         res = self.combine_list(n_list, k)
#         return res

#     def combine_list(self, n_list, k):
#         if len(n_list)<k:
#             return []
#         if k == 0:
#             return [[]]
#         res = list()
#         for i, val in enumerate(n_list):
#             for val_list in self.combine_list(n_list[i+1:], k-1):
#                 res.append([val]+val_list)
            
#         return res

# method 2 从1开始，每次有两个选择

# 取1，从后面的n-1个数中取k-1个数
# 不取1，从后面的n-1个数中取k个数
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []

#         def dfs(cur_nums, idx):
#             # cur_nums 记录当前已经取到的值
#             if len(cur_nums)==k:
#                 res.append(cur_nums)
#                 return
#             if idx>n:
#                 return
#             dfs(cur_nums+[idx], idx+1)
#             dfs(cur_nums, idx+1)
        
#         dfs([], 1)
#         return res

# method 3 直接利用python的库函数
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return list(combinations(list(range(1, n+1)),k))
        
