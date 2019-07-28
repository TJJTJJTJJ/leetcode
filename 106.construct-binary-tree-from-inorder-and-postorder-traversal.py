#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# # method 1 traditional
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         if not postorder:
#             return None
#         root = TreeNode(postorder.pop())
#         for i, val in enumerate(inorder):
#             if val==root.val:
#                 break
#         root.left = self.buildTree(inorder[:i], postorder[:i])
#         root.right = self.buildTree(inorder[i+1:], postorder[i:])
#         return root

# method 2 new
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        ind = inorder.index(postorder.pop())
        root = TreeNode(inorder[ind])
        root.right= self.buildTree(inorder[ind+1:], postorder)
        root.left = self.buildTree(inorder[:ind], postorder)
        return root

