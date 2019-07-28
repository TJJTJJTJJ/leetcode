#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (55.19%)
# Total Accepted:    441.2K
# Total Submissions: 787.4K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 1 刚开始以为给的是一个序列，还在考虑怎么把一个序列变成一个树
# 先用迭代做做，自己毕竟不熟这些
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = list()
#         def helper(root):
#             if not root:
#                 return 
#             helper(root.left)
#             res.append(root.val)
#             helper(root.right)
#         helper(root)
#         return res

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         def helper(root):
#             if not root:
#                 return []
#             return helper(root.left) + [root.val] + helper(root.right)
#         return helper(root)

# method 2 尝试用辅助栈实现递归
# stack1记录cur之前的递归体
# cur表示当前的递归体，有两层含义，即将入栈的递归体和出栈的递归体
# 进递归体等价于入栈
# 递归体内部的操作不变
# 出递归体表示出栈
# 最好是画一个递归体的出栈入栈图，并理解其出入栈的条件和递归体的转移
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack1 = list()
        res = list()
        cur = root
        # cur表示即将入栈型
        while cur or stack1:
            if cur:
                # 这里的递归体属于即将入栈型
                stack1.append(cur)
                cur = cur.left
                # 这里隐含省略了continue
            else:
                # 这里的递归体属于出栈型
                cur = stack1.pop()
                res.append(cur.val)
                cur = cur.right
                # 这里隐含省略了continue
        return res


