#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 1 暴力迁移
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         if not root:
#             return
#         if root.left:
#             node = root.left
#             while node.right:
#                 node = node.right
#             left_right = node
#             left_right.right = root.right
#             root.right = root.left
#             root.left = None
#             self.flatten(root.right)
#         else:
#             self.flatten(root.right)

# method 2:https://leetcode.com/problems/
# flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)
# 我根据自己对这段代码的理解做出一个解释，应该不是最好的解释，
# 定义函数 p=f(root): 其中p表示root的最右子节点
# 推导规则：
# Question: 怎么才能想到这种思路呢



