#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (30.02%)
# Total Accepted:    188.2K
# Total Submissions: 624.8K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        num1 = list(num1)
        num1.insert(0, '0')
        num2 = list(num2)
        num3 = ['0'] * (len(num1)+len(num2))
        e = [0] * (len(num2)+1)
        sum = [0] * (len(num2)+1)

        def str2int(ch):
            return ord(ch)-ord('0')
        
        def int2str(x):
            return chr(x+ord('0'))

        for i in range(-1, -1-len(num3), -1):
            sum_tmp = 0
            for j in range(i, 0, 1):
                if -j>len(num1) or -(i-1-j)>len(num2):
                    continue
                sum[j-i] = str2int(num1[j])*str2int(num2[i-1-j])+e[j-i]
                e[j-i] = sum[j-i]//10
                sum_tmp+=(sum[j-i]%10)
            sum_tmp+=e[-1]
            num3[i] = int2str(sum_tmp%10)
            e[-1]=(sum_tmp)//10
        for i, val in enumerate(num3):
            if val != '0':
                break
        res = ''.join(num3[i:])
        return res
        

