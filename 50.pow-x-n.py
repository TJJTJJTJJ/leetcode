#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (27.58%)
# Total Accepted:    300.8K
# Total Submissions: 1.1M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
# 
# 
# method 1：这个迭代是从n上循环的，下一个方面更妙
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1;
        if n<0:
            n = -n
            x = 1/x
        if n%2==0:
            tmp = self.myPow(x, n//2)
            return tmp*tmp
        else:
            tmp = self.myPow(x, n//2)
            return x*tmp*tmp

# method 2
class Solution:
        def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1;
        if n<0:
            n = -n
            x = 1/x
        if n%2==0:
            return self.myPow(x*x, n//2)
        else:
            return x*self.myPow(x*x, n//2)
            

