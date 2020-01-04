"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pphead = ListNode(0)
        pphead.next = head
        def helper(phead):
            if not phead.next or not phead.next.next:
                return
            tmp = phead.next
            phead.next = tmp.next
            tmp.next = tmp.next.next
            phead.next.next = tmp
            helper(tmp)
        helper(pphead)
        return pphead.next
        
        
        
        