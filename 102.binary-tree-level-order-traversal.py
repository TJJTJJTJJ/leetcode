#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (47.16%)
# Total Accepted:    364K
# Total Submissions: 757.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 1 循环，用二维列表先记录node，然后转换成node.val
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         res = list()
#         res.append([root])
#         while res[-1]:
#             res.append(list())
#             for val in res[-2]:
#                 if val.left:
#                     res[-1].append(val.left)
#                 if val.right:
#                     res[-1].append(val.right)
#         res = [[ j.val for j in i] for i in res]
#         return res[:-1]

# method 2 还是先用循环，需要用两个队列来记录当前层和下一层的node，感觉比较繁琐
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         res, level = list(), [root]
#         while level:
#             res.append(list())
#             next_level = list()
#             for node in level:
#                 res[-1].append(node.val)
#                 if node.left:
#                     next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)
#             level = next_level
#         return res    

# method 3 献祭出神器 递归，层遍历的递归的本质就是把node.val放入相应的层即可
# 看来递归还是慢一些
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         def dfs(node, level):
#             if not node:
#                 return 
#             if len(res)<level+1:
#                 res.append([])
#             res[level].append(node.val)
#             dfs(node.left, level+1)
#             dfs(node.right, level+1)
#         res = []
#         dfs(root, 0)
#         return res

# method 4 充分利用了列表生成式，很棒，可以理解成method2的精简版
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, level = list(), [root]
        while level:
            res.append( [node.val for node in level])
            level = [ (node.left, node.right) for node in level]
            level = [ val for lr in level for val in lr if val]
            # level = [ kid for node in level for kid in (node.left, node.right) if kid]
        return res


