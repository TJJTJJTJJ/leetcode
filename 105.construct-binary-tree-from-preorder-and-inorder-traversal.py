#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (39.61%)
# Total Accepted:    216.7K
# Total Submissions: 533.2K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if len(preorder)!=len(inorder):
#             return None
#         if not preorder:
#             return None
#         root = TreeNode(preorder[0])
#         # index = inorder.index(preorder[0])
#         for index, val in enumerate(inorder):
#             if val==root.val:
#                 break
#         root.left = self.buildTree(preorder[1:index+1], inorder[:index])
#         root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
#         return root

# method 2 相当于对 method 1 的升级版，用了preorder.pop，避免了preorder的偏移量
# 这里对preorder的处理很微妙，因为当处理完左子树后，preorder中是左子树的元素都会被pop掉，不再需要偏移量
# 或者换个思路想，其实是依次弹出preorder的元素，只是不知道弹出的元素是位于上一个结点的左子树还是右子树，
# 需要通过inorder来判断元素位于左子树还是右子树
# 这个思路也还是有问题，只能理解成对mothod1的遍历过程中发现preorder在处理right时，left已经全部处理结束
# 这里 preorder 相当于一个全局变量
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return 
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root

