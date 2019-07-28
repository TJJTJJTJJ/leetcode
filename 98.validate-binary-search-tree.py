#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (25.28%)
# Total Accepted:    389.5K
# Total Submissions: 1.5M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# Example 1:
# 
# 
# Input:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's
# value
# is 5 but its right child's value is 4.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 1 最笨的方法，挨个判断
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         if not root:
#             return True

#         def isValidLeRi(root, left, right):
#             if not root:
#                 return True
#             if (left and root.left and left>=root.left.val) or (root.left and root.left.val>=root.val):
#                 return False
#             else:
#                 le = isValidLeRi(root.left, left, root.val)
#             if (right and root.right and root.right.val>=right) or (root.right and root.val>=root.right.val):
#                 return False
#             else:
#                 ri = isValidLeRi(root.right, root.val, right)
#             return  le and ri
        
#         res = isValidLeRi(root, None, None)
#         return res
        
# method2 用中序遍历，也是常见的方法

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         res = list()
#         def inorder(root):
#             if not root:
#                 return
#             inorder(root.left)
#             res.append(root.val)
#             inorder(root.right)
#         inorder(root)
#         for i in range(1, len(res)):
#             if res[i].val<=res.[i-1].val:
#                 return False
#         return True

# method3 和method1同样的思路，别人写的代码就是短很多，我的是每次判断左右，他是直接判断当前结点，
# 自己应该多学学这种思维，因为左右到了下一层也是当前，自己总是忽略这一点。

# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         import sys
#         def valid(root, smallest, largest):
#             if not root:
#                 return True
#             if smallest >= root.val or largest <= root.val:
#                 return False
#             return valid(root.left, smallest, root.val) and valid(root.right, root.val, largest)
#         if not root:
#             return True
#         return valid(root, -sys.maxsize, sys.maxsize)

# method 4 我去，这就开始循环形式的中序遍历了啊，
# 念一遍口诀：中序遍历，cur入栈指左，cur出栈指右
# 前序遍历，cur右入栈指左，cur出栈指cur

class Solution(object):
    def isValidBST(self, root):
        stack = list()
        pre = None
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if pre is not None and pre>=node.val:
                    return False
                pre = node.val
                node = node.right
        return True
        

