# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        left = right = dummy
        for _ in range(n):
            right = right.next
        while right.next != None:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next