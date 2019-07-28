#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.69%)
# Total Accepted:    489.5K
# Total Submissions: 1.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
# method 1 记录了当前字符所有可能形成的回文字符串长度
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ""

#         max_len = 0
#         pre_len = [0,1]
#         now_len = []

#         for i, val in enumerate(s):
#             pre_len = now_len
#             now_len = [0, 1]
#             for j in pre_len:
#                 if i-j-1>-1 and s[i-j-1]==val:
#                     now_len.append(j+2)

#             if now_len[-1] > max_len:
#                 max_len = now_len[-1]
#                 max_substr = s[i-max_len+1:i+1]

#         return max_substr

# method 2 拉马车算法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = '#'.join('^{}$'.format(s))
        p = [1 for _ in T]
        id = 1
        mx = 1 
        max_id = 1
        for i in range(1, len(T)-1):
            if i < mx:
                p[i] = min(p[2*id-i], mx-i)
            while(T[i+p[i]]==T[i-p[i]]):
                p[i]+=1
            if(mx<i+p[i]):
                mx = i+p[i]
                id = i
            if p[max_id] < p[i]:
                max_id = i
        s_len = p[max_id]-1
        s_start = (max_id-p[max_id])//2
        return s[s_start:s_start+s_len]

