#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (43.31%)
# Total Accepted:    287.3K
# Total Submissions: 661.5K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# method 1
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         pHead = ListNode(0)
#         pHead.next = head
#         p1 = pHead
#         if not p1.next:
#             return head
#         p2 = p1.next
#         while p2.next:
#             p2 = p2.next
#             p1.next.next = p2.next
#             p2.next = p1.next
#             p1.next = p2
#             if p2.next and p2.next.next:
#                 p1, p2 = p1.next.next, p2.next.next
#             else:
#                 break     
#         head = pHead.next
#         return head

# method 2

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         pHead = ListNode(0)
#         pHead.next = head
#         p1 = pHead
#         while p1.next and p1.next.next:
#             p2, p3 = p1.next, p1.next.next
#             p1.next, p2.next, p3.next = p3, p3.next, p2
#             p1 = p2

#         head = pHead.next
#         return head


# method 3

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pHead = ListNode(0)
        pHead.next = head
        p1 = pHead
        while p1.next and p1.next.next:
            p0, p1, p2 = p1, p1.next, p1.next.next
            p0.next, p1.next, p2.next = p2, p2.next, p1
        head = pHead.next
        return head


