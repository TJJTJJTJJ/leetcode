#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 1 recursion，每次取中间的结点作为root，这样也不用判断什么的了
# class Solution:
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         mid = self.findMiddle(head)
#         # 0 个结点
#         if not mid:
#             return None
#         root = TreeNode(mid.val)
#         # 1 个结点
#         if head==mid:
#             return root
#         root.left = self.sortedListToBST(head)
#         root.right = self.sortedListToBST(mid.next)
#         return root

#     def findMiddle(self, head):
#         if not head:
#             return None
        
#         prev, slow, fast = None, head, head
#         while fast and fast.next:
#             prev = slow
#             slow = slow.next
#             fast = fast.next.next
#         if prev:
#             prev.next = None 
#         return slow

# method 2 思路和method 1 整体相似，空间换时间
# class Solution:
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         vals = self.ListNode2List(head)
#         def List2BST(l, r):
#             # 没有元素时
#             if l>r:
#                 return None
#             mid = (l+r)//2
#             root = TreeNode(vals[mid])
#             root.left = List2BST(l, mid-1)
#             root.right = List2BST(mid+1, r)
#             return root
#         root = List2BST(0, len(vals)-1)
#         return root

#     def ListNode2List(self, head):
#         vals = list()
#         while head:
#             vals.append(head.val)
#             head = head.next
#         return vals

# method 3 完全换了个思路，利用二叉搜索树的中序遍历和链表一样的性质
# <https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solution/>
# 中序遍历: Linked_list = f(root)=f(root.left)+root.val+f(root.right)
# 链表解析: f(l,r) =f(l, mid-1)+head.val+f(mid+1, r)
# 定义f(l,r)表示l-r的链表解析成平衡二叉搜索树
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        r = -1
        node = head
        while node:
            r+=1
            node = node.next
        node = head
        def Lrt2BST(l, r):
            # 空 结束条件
            nonlocal head
            if l>r:
                return None
            mid = (l+r)//2
            left = Lrt2BST(l, mid-1)
            root = TreeNode(head.val)
            head = head.next
            right = Lrt2BST(mid+1, r)
            root.left = left
            root.right = right
            return root
        root = Lrt2BST(0, r)
        return root

