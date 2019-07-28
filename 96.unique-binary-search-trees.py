#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (45.20%)
# Total Accepted:    194.2K
# Total Submissions: 423.8K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
# 
# Example:
# 
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#
# method1 在题95的基础上进行了修改
class Solution:
    def __init__(self):
        self.numdict = dict()
    def numTrees(self, n: int) -> int:
        if n == 0:
            return []
        
        def helper(nums):
            if not nums:
                return 1
            res = 0
            for num in range(1, nums+1):
                if num-1 not in self.numdict:
                    self.numdict[num-1] = helper(num-1)
                lef = self.numdict[num-1]
                if nums-num not in self.numdict:
                    self.numdict[nums-num] = helper(nums-num)
                rig = self.numdict[nums-num]
                res=res+lef*rig
            return res
        
        return helper(n)

# method2 用公式，也是6666，卡特兰公式，神奇

# h(n) = h(n) = h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)h(0) (其中n>=2)h(0)=h(1)=1

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n+1)]
        for i in range(2, n+1):
            s = 0
            for k in range(i):
                s += dp[k]*dp[i-k-1]
            dp[i] = s
        return dp[-1]


