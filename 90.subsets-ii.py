#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (41.52%)
# Total Accepted:    196.3K
# Total Submissions: 467.7K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
# method 1 用flag来表示是否已经取过，显然这种效率是低下的
# class Solution:
#     def subsetsWithDup(self, nums):
#         res = list()
#         n = len(nums)
#         nums.sort()

#         def subset(idx, res_tmp, flag):
#             if idx == n:
#                 res.append(res_tmp)
#                 return
#             if idx>0 and nums[idx]==nums[idx-1]:
#                 if flag:
#                     subset(idx+1, list(res_tmp+[nums[idx]]), True)
#                     subset(idx+1, list(res_tmp), False)
#                 else:
#                     subset(idx+1, list(res_tmp), False)
#             else:
#                 subset(idx+1, list(res_tmp+[nums[idx]]), True)
#                 subset(idx+1, list(res_tmp), False)
#         subset(0, [], True)
#         return res

# method 2 这种类似的方法在之前也见到过，是从上至上的，并且小的复制保留这样一种操作
# 感觉方法不是很简洁，就不写了

# method 3 dfs大法好 类似78 not in 感觉怪怪的
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        def dfs(index, path):
            if path not in res:
                res.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])
        dfs(0, [])

        return res
# 这个dfs大法是精髓
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        def dfs(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                else:
                    dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return res
# method 4 for 大法 我在method1的时候尝试写但是没能写出来
# 这是method 2 的精简，这个方法精辟，比method 2的好看多了
# 每次在复制添加前记录下当前res长度，在遇到重复的数字的时候直接从后一部分开始添加
class Solution:
    def subsetsWithDup(self, nums):
        res = list([[]])
        nums.sort()
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                le = len(res)
            for j in range(len(res)-le, len(res)):
                res.append(res[j]+[nums[i]])


