#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (34.12%)
# Total Accepted:    187.6K
# Total Submissions: 542.9K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# method 在实际写的时候才发现一些问题，p2, p3, p4中p3总是指向翻转列表的末尾，这样可以避免p4越界
# 其中p3表示当前节点，p2为了保证p3.next能找到节点，p4为了保证整个过程向前进行
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if (not head) or m==n:
            return head
        pHead = ListNode(0)
        pHead.next = head
        p1 = pHead
        for i in range(m-1):
            p1 = p1.next
        p1_prev, p1 = p1, p1.next
        p2, p3, p4 = p1_prev, p1_prev.next, p1_prev.next.next
        for i in range(n-m):
            p2, p3, p4 = p3, p4, p4.next
            p3.next = p2
        p1_prev.next, p1.next = p3, p4
        return pHead.next

