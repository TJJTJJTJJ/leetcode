#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (44.95%)
# Total Accepted:    308.8K
# Total Submissions: 680.4K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
# method 1 key为字符串
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # import collections
#         # strs_dict = collections.defaultdict(list)
#         strs_dict = dict()
#         for val in strs:
#             key = ''.join(sorted(val))
#             strs_dict.setdefault(key,[])
#             strs_dict[key].append(val)
#         res = list()
#         for val in strs_dict.values():
#             res.append(val)
#         return res

# # method 2 tuple为key，直接返回字典的value
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         strs_dict = dict()
#         for val in strs:
#             key = tuple(sorted(val))
#             strs_dict[key]=strs_dict.get(key,[]).append(val)

#         res = d.values()
#         return res

# method 3 直接对列表排序，这个方法并没有借助hashmap来完成这个操作，而是直接通过排序法，排序的关键字为其key，这样排序之后就已经按照key排在一起了
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp1 = sorted(strs, key=sorted) # 第二个sorted是提取其key，第一个sorted对key排序
        import itertools
        group = itertools.groupby(tmp1, key=sorted) # 相邻重复元素分在一起
        res = [ list(g) for _, g in group]
        return res




