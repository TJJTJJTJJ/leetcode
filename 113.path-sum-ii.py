#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 1
# 异常情况返回一维列表，循环中会被忽略，正常情况返回二维列表，会自动添加
# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#         if not root:
#             return []
#         if (not root.left and not root.right) and (root.val==sum):
#             return [[root.val]]
#         if not root.left and not root.right:
#             return []
#         res = []
#         for val in self.pathSum(root.left, sum-root.val):
#             res.append([root.val]+val)
#         for val in self.pathSum(root.right, sum-root.val):
#             res.append([root.val]+val)
#         return res
# method 2 竟然用了 queue，广度优先遍历，用队列记录结点、路线和值，
# 可以的，用一个三元组很轻松地解决了重复记录或者丢失信息的问题
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            cur, val, ls = queue.pop(0)
            if not cur.left and not cur.right and val==sum:
                res.append(ls)
            if cur.left:
                queue.append((cur.left, val+cur.left.val, ls+[cur.left.val]))
            if cur.right:
                queue.append((cur.right, val+cur.right.val, ls+[cur.right.val]))
        return res


