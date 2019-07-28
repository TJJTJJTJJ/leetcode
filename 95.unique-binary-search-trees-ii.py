#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (34.86%)
# Total Accepted:    134.7K
# Total Submissions: 380.9K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 1
# class Solution:
#     def generateTrees(self, n: int) -> List[TreeNode]:
#         if n<1:
#             return []
#         TreeList = list()
#         for i in range(1, n+1):
#             TreeList.append(TreeNode(i))
        
#         def generateTreeList(TreeList):
#             if not TreeList:
#                 return [None]
#             if len(TreeList)==1:
#                 return TreeList
#             res = list()
#             for i, val in enumerate(TreeList):
#                 for lef in generateTreeList(TreeList[:i]):
#                     for rig in generateTreeList(TreeList[i+1:]):
#                         val_tmp = TreeNode(val.val)
#                         val_tmp.left = lef
#                         val_tmp.right = rig
#                         res.append(val_tmp)
#             return res
        
#         res = generateTreeList(TreeList)
#         return res

# method2 是对method1的简化吧，列表是数字就可以了，不用非得结点
# class Solution:
#     def generateTrees(self, n: int) -> List[TreeNode]:
#         if n == 0:
#             return []
        
#         def helper(nums):
#             if not nums:
#                 return [None]
#             res = []
#             for idx, num in enumerate(nums):
#                 for l in helper(nums[:idx]):
#                     for r in helper(nums[idx+1:]):
#                         node = TreeNode(num)
#                         node.left = l
#                         node.right = r
#                         res.append(node)
#             return res
        
#         return helper(list(range(1, n+1)))

# method3 是对metho2的简化
# class Solution:
#     def generateTrees(self, n: int) -> List[TreeNode]:
    
#     def generate(first, last):
#         trees = []
#         for root in range(first, last+1):
#             for left in generate(first, root-1):
#                 for right in generate(root+1, last):
#                     node = TreeNode(root)
#                     node.left = left
#                     node.right = right
#                     trees += node,
#         return trees or [None]
#     return generate(1, n)

# or 
# def node(val, left, right):
#     node = TreeNode(val)
#     node.left = left
#     node.right = right
#     return node

# class Solution:
#     def generateTrees(self, last, first=1):
#         return [node(root, left, right)
#                 for root in range(first, last+1)
#                 for left in self.generateTrees(root-1, first)
#                 for right in self.generateTrees(last, root+1)] or [None]

# method4 添加了记录表进行剪枝
class Solution:
    def __init__(self):
        self.cache = {}
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        if n == 0:  return []
        return self.genT(1, n)
    def genT(self, start, end):
        if start > end: return [None]
        if start == end:    return [TreeNode(start)]
        if (start, end) not in self.cache:
            res = []
            for root_idx in range(start, end+1):
                for lnode in self.genT(start, root_idx-1):
                    for rnode in self.genT(root_idx+1, end):
                        root = TreeNode(root_idx)
                        root.left = lnode
                        root.right = rnode
                        res.append(root)
            self.cache[(start, end)] = res
        return self.cache[(start, end)]
 
