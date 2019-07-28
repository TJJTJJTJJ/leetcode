#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (21.92%)
# Total Accepted:    250.9K
# Total Submissions: 1.1M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#
# method 1 类似暴力，从上到下的递归，因为可能重复，所以需要一个记录表或者从下到上
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         s_li = list(s)
#         count = [0]
#         def listDecodings(s_list):
#             if not s_list:
#                 count[0] = count[0]+1
#                 return
#             if s_list[0]>'0':
#                 listDecodings(s_list[1:])
#             else:
#                 return
#             if len(s_list)>1 and ((s_list[0]=='1') or (s_list[0]=='2' and s_list[1]<'7')):
#                 listDecodings(s_list[2:])
#         listDecodings(s_li)
#         return count[0]

# method 2， method 1超出时间限制，所以考虑从下到上
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         count = [0, 1]
#         __factory = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#         if not s or s[0]=='0':
#             return 0
#         if s[-1]=='0':
#             count[0]=0
#         else:
#             count[0]=1
        
#         for i in range(2, len(s)+1):
#             if s[-i] in ['1', '2'] and s[-i+1] in ['0']:
#                 count[0], count[1] = count[1], count[0]
#             elif s[-i] in __factory[0:1]+__factory[3:10] and s[-i+1] in __factory[1:10]:
#                 count[0], count[1] = count[0], count[0]
#             elif s[-i] in ['2'] and s[-i+1] in ['7', '8', '9']:
#                 count[0], count[1] = count[0], count[0]
#             elif s[-i] in ['2'] and s[-i+1] in __factory[1:7]:
#                 count[0], count[1] = count[0]+count[1], count[0]
#             elif s[-i] in ['1'] and s[-i+1] in __factory:
#                 count[0], count[1] = count[0]+count[1], count[0]
#             else:
#                 return 0
#         return count[0]

# method 3 ，method2好像把情况复杂化了，五个if可以化简成两个
# 在method2中，是直接考虑s[i]和s[i+1]的组合情况，
# 而method3中，是从自身解码和组合解码的角度考虑的，使分类更清晰，逻辑更条理，厉害厉害
# 可见分类标准不一样，对代码有略微大的影响
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         count = [1, 0]
#         if s[0]!='0':
#             count[1] = 1
#         for i in range(1, len(s)):
#             if '10'<=s[i-1:i+1]<='26':
#                 count[0], count[1] = count[1], count[0]
#             else:
#                 count[0], count[1] = count[1], 0
#             if s[i]!='0':
#                 count[1] = count[0]+count[1]
#         return count[1]

# method 4 来一个秀神的代码，核心思想和method3一样，是从自身解码和组合解码的角度考虑的
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         v, w, p = 0, int(s>''), ''
#         for d in s:
#             v, w, p = w, (d>'0')*w+(9<int(p+d)<27)*v, d
#         return w
# w 表示当前位置的解码方法
# v 表示前一个位置的解码方法
# p 表示前一个位置的字符
# method4的初始化和method3的初始化有点不一样，结果是一样的
# method4是直接从第一个字符开始计算的
# s不为空，v,w = 0,1
# method3是从第二个字符开始计算的
# s不为空，v,w = 1,0/1

# method 5 对metho4的精简版
# 应该给自己提个醒，对于这种循环做同样操作的，可以考虑用reduce和map
from functools import reduce
class Solution:
    def numDecodings(self, s: str) -> int:
        def func(x1, d):
            v, w, p = x1
            v, w, p = w, (d>'0')*w+(9<int(p+d)<27)*v, d
            return (v, w, p)
        return reduce(func,s,(0,s>'',''))[1]

