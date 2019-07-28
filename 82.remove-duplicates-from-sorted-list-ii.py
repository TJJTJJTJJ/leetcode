#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (32.25%)
# Total Accepted:    175.3K
# Total Submissions: 537.7K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# method 1 这算是最笨的
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head 
#         pHead = ListNode(-1)
#         pHead.next = head
#         p1 = pHead
#         while p1.next and p1.next.next:
#             if p1.next.val != p1.next.next.val:
#                 p1 = p1.next
#             else:
#                 p2 = p1.next
#                 while p2 and p2.val==p1.next.val:
#                     p2 = p2.next
#                 p1.next = p2
#         return pHead.next
# method 2 定义一个函数f(i,i+1,..,j)返回头结点，如果i!=i+1,保留i, 
# 如果i==i+1==...==j-1, 舍弃i...j-1
# 神操作
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         return self.h(head)
    
#     def h(self, head):
#         if not head or not head.next:
#             return head
#         if head.val != head.next.val:
#             head.next = self.h(head.next)
#             return head
#         else:
#             x = head.val
#             while head and head.val == x:
#                 head = head.next
#             return self.h(head)
        

# class Solution(object):
#     def deleteDuplicates(self, head):
#         return self.h(head)

#     def h(self, head):
#         if not head or not head.next: return head
#         if head.val != head.next.val:
#             head.next = self.h(head.next)
#             return head
#         x = head.val
#         cur = head.next
#         while cur and x == cur.val:
#             cur = cur.next
#         return self.h(cur)

# method 3 这个思路和 method 2 类似，主要也是f，不同点在于处理head相同的时候
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur, is_head = head.next, False
        while cur and cur.val == head.val:
            cur = cur.next
            is_head = True
        head.next = self.deleteDuplicates(cur)
        return head.next if is_head else head

