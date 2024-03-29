#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (14.51%)
# Total Accepted:    333.4K
# Total Submissions: 2.3M
# Testcase Example:  '"42"'
#
# Implement atoi which converts a string to an integer.
# 
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this
# function.
# 
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned.
# 
# Note:
# 
# 
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical
# value is out of the range of representable values, INT_MAX (2^31 − 1) or
# INT_MIN (−2^31) is returned.
# 
# 
# Example 1:
# 
# 
# Input: "42"
# Output: 42
# 
# 
# Example 2:
# 
# 
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus
# sign.
# Then take as many numerical digits as possible, which gets 42.
# 
# 
# Example 3:
# 
# 
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a
# numerical digit.
# 
# 
# Example 4:
# 
# 
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a
# numerical 
# digit or a +/- sign. Therefore no valid conversion could be performed.
# 
# Example 5:
# 
# 
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed
# integer.
# Thefore INT_MIN (−2^31) is returned.
# 
#
# method 1
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         num_pm = 1
#         flag = True
#         pre_num = True
#         res = 0
#         pm = False
#         for cha in str:
#             if pre_num:
#                 if cha == ' ' and num_pm > 0:
#                     continue
#                 elif (cha=='+' or cha=='-') and num_pm>0:
#                     num_pm-=1
#                     pm = cha == '-'
#                 elif cha <= '9' and cha >= '0':
#                     res = res*10+ord(cha)-ord('0')
#                     pre_num = False
#                 else:
#                     flag = False
#             else:
#                 if cha <= '9' and cha >= '0':
#                     res = res*10+ord(cha)-ord('0')
#                 else:
#                     break

#         if flag:
#             if pm:
#                 res = max(0-res, -0x80000000)
#             else:
#                 res = min(res, 0x7fffffff)
#         else:
#             res = 0
        
#         return res

# # method 2
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         if len(str) == 0:
#             return 0
#         ls = list(str.strip())

#         sign = -1 if ls[0]=='-' else 1
#         if ls[0] in ['+', '-']: del ls[0]
#         ret = 0
#         while i < len(ls) and ls[i].isdigit():
#             ret = ret*10 + ord(ls[i])-ord(0)
#             i+=1
#         ret = max(-0x80000000, min(sign*ret, 0x7fffffff))
#         return ret

# method 3
class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        ret = re.match('\s*([+,-]?)(\d+).*', str)
        res = 0
        if ret: 
            sign, digits = ret.groups()
            sign=-1 if sign=='-' else 1
            for val in digits:
                res = res*10+ord(val)-ord('0')
            res = max(-0x80000000, min(sign*res, 0x7fffffff))
        return res
        

