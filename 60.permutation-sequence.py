#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (32.37%)
# Total Accepted:    132.4K
# Total Submissions: 406.2K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the k^th permutation sequence.
# 
# Note:
# 
# 
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 3
# Output: "213"
# 
# 
# Example 2:
# 
# 
# Input: n = 4, k = 9
# Output: "2314"
# 
# 
# method 1
# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         res = list()
#         tmp = list(str(val) for val in range(1,n+1))
#         fac, i = 1, 0
#         while k>fac*(i+1) and i<n:
#             i+=1
#             fac = i*fac
#         for ii in range(n-i-1):
#             res.append(tmp.pop(0))
#         while i>0:
#             ii, k = divmod(k-1, fac)
#             k+=1
#             fac/=i
#             i-=1
#             res.append(tmp.pop(int(ii)))
#         res.append(tmp.pop())
#         return ''.join(res)

# method 2 对method 1的一些操作可以合并
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = list()
        res = list()
        tmp = list(str(val) for val in range(1,n+1))
        fac = 1
        for i in range(1, n):
            fac*=i
        k-=1
        for i in range(n-1,-1,-1):
            index, k = divmod(k, fac)
            fac=fac/(i or 1)
            res.append(tmp.pop(int(index)))
        return ''.join(res)



