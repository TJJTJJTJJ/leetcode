#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (49.87%)
# Total Accepted:    206.8K
# Total Submissions: 414.7K
# Testcase Example:  '3'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
# 
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, two is written as II in Roman numeral, just two one's added
# together. Twelve is written as, XII, which is simply X + II. The number
# twenty seven is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
# 
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# 
# Given an integer, convert it to a roman numeral. Input is guaranteed to be
# within the range from 1 to 3999.
# 
# Example 1:
# 
# 
# Input: 3
# Output: "III"
# 
# Example 2:
# 
# 
# Input: 4
# Output: "IV"
# 
# Example 3:
# 
# 
# Input: 9
# Output: "IX"
# 
# Example 4:
# 
# 
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# 
# 
# Example 5:
# 
# 
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
#
# method 1
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         _list_num = [[],[0],[0,0],[0,0,0],[0,1],[1],[1,0],[1,0,0],[1,0,0,0],[0,2],[2]]
#         _list_Ro = [['I','V','X'],['X','L','C'],['C','D','M'],['M']]
#         i=0
#         res = []
#         while num>0:
#             num, b = divmod(num, 10)
#             tmp_str = ''.join([ _list_Ro[i][tmp] for tmp in _list_num[b]])
#             res.insert(0, tmp_str)
#             i+=1
#         ret = ''.join(res)
#         return ret
# method 2
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         M = ["", "M", "MM", "MMM"];
#         C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
#         X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
#         I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
#         return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];

# method 3
class Solution:
    # @return a string
    def intToRoman(self, num):
        value_roman = {1000:"M", 900:"CM", 500:"D", 400:"CD",
                       100:"C", 90:"XC", 50:"L", 40:"XL",
                       10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        roman = ""
        for v in [1000,900,500,400,100,90,50,40,10,9,5,4,1]:
            roman += value_roman[v] * (num//v)
            num %= v
        return roman

