#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (40.56%)
# Total Accepted:    211.5K
# Total Submissions: 511.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
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

# 两种方法：循环和递归
# 循环
# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         res, level, count = list(), [root], 1
#         while level:
#             if count==1:
#                 res.append([node.val for node in level])
#                 count=0
#             else:
#                 res.append([node.val for node in level[::-1]])
#                 count=1
#             level = [ kid for node in level for kid in (node.left, node.right) if kid]
#         return res
# 递归
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = list()

        def dfs(root, level):
            if not root:
                return
            if len(res)<level+1:
                res.append([])
            # 还是别人牛逼，我这里都想不出怎么写才好
            # 这应该算是一个队首队尾指针的队列
            if level%2==0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return res

# 在zigzag中，我们可以看出，对二叉树的遍历顺序并没有发生变化，
# 发生改变的只是如何把值放进res中，循环中用了reverse，
# 递归中用了队首指针 insert(0)


