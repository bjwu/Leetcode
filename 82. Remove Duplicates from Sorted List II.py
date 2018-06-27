# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float('inf'))
        dummy.next = head
        left = dummy
        middle = right = head
        while right != None:
            if right.next == None or right.val != right.next.val:
                if right == middle:
                    left.next = right
                    left = right
                elif right.next == None:
                    left.next = None
                right = right.next
                middle = right
            else:
                right = right.next
        return dummy.next