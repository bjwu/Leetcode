# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        HeadNode = ListNode(None)
        HeadNode.next = head
        
        last = HeadNode
        current = head
        while current != None:
            if current.val == val:
                current = current.next
                last.next = current
            else:
                current = current.next
                last = last.next
        return HeadNode.next