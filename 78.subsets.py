#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (51.16%)
# Total Accepted:    347.8K
# Total Submissions: 670.1K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
# method 1 利用递归法进行计算
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         if not nums:
#             return None
#         n = len(nums)
#         res = list()

#         def subset(res_tmp, idx, flag):
#             if not res_tmp:
#                 res_tmp = list()
#             if flag:
#                 res_tmp.append(nums[idx])
#             if idx == n-1:
#                 return [res_tmp]
#             a = subset(list(res_tmp), idx+1, True)
#             b = subset(list(res_tmp), idx+1, False)
#             return a+b
        
#         a = subset(None, 0, True)
#         b = subset(None, 0, False)
#         return a+b

# method 2 利用循环做，和 method1 一个原理，这个思路更难得
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = list([[]])
#         for val in nums:
#             res_tmp = list([])
#             for re in res:
#                 re = list(re)
#                 re.append(val)
#                 res_tmp.append(re)
#             res = res+res_tmp
#         return res
# method 3 对method 2 的精简
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = list([[]])
#         for num in nums:
#             res.extend([tmp+[num] for tmp in res] )
#         return res

# method 4 对method 1 的精简，我用的是return，很麻烦，不如这种直接res.append好使，因为本质上是不需要返回的
# 这个的思路就是二叉树啊，那说明method 5 的思路不一样
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = list([])
#         def search(tmp_res, idx):
#             if idx == len(nums):
#                 res.append(tmp_res)
#             else:
#                 search(tmp_res+[nums[idx]], idx+1)
#                 search(tmp_res, idx+1)
#         search([], 0)
#         return res

# dfs，二叉树，左节点表示选择，右节点表示不选择，记录从根节点到叶子节点的path
# method 5 这个思路是：
# path：表示从index之后都不选
# path+[nums[i]]: 在index之后选一个，同时记录选的位置，绝了
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = list()
        def dfs(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return res


