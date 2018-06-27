# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        left, right = dummy, dummy.next
        while right != None and right.next != None:
            left.next = right.next
            left = right
            right = right.next.next
            left.next.next = left
            left.next = right 
        return dummy.next
            
        
        
        
        
        