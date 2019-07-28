#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (30.78%)
# Total Accepted:    291.7K
# Total Submissions: 946.4K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
# method1 依次遍历输入流
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s)<=numRows:
            return s
        index = 0
        L = ['' for _ in range(numRows)]
        direction = -1
        for cha in s:
            L[index]+=(cha)
            if index == 0 or index == numRows-1:
                direction = 0-direction
            index+=direction
        res = ''.join(L)
        return res



