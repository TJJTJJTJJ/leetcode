#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (36.40%)
# Total Accepted:    158.6K
# Total Submissions: 431.1K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        pHead1, pHead2 = ListNode(-1), ListNode(-1)
        p1, p2 = pHead1, pHead2
        pNode = head
        while pNode:
            if pNode.val<x:
                p1.next, pNode = pNode, pNode.next
                p1 = p1.next
            else:
                p2.next, pNode = pNode, pNode.next
                p2 = p2.next
        p2.next = None
        p1.next = pHead2.next
        return pHead1.next

