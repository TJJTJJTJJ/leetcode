#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (53.32%)
# Total Accepted:    307.4K
# Total Submissions: 575.3K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
# method 1
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         results = []
#         self.generate_Parenthesis(n, n, '', results)
#         return results

#     def generate_Parenthesis(self, n1, n2, result, results):
#         if n1>n2:
#             return
#         if n1 < 0:
#             return  
#         if n2==0:
#             results.append(result)
#         self.generate_Parenthesis(n1-1, n2, result+'(', results)
#         self.generate_Parenthesis(n1, n2-1, result+')', results)
#         return

# method 2
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:

#         def generate(result, n1, n2):
#             if n2>=n1>=0:
#                 if not n2:
#                     yield result
#                 for val in generate(result+'(', n1-1, n2):
#                     yield val
#                 for val in generate(result+')', n1, n2-1):
#                     yield val
        
#         res = list(generate('',n,n))

#         return res

# method 3
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return ['']
        results = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                   results.append('({}){}'.format(left, right))
        return results


        
