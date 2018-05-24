# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ## find the mid
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        ## reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        ## compare two halves
        while node:
            if node.val == head.val:
                node = node.next
                head = head.next
            else:
                return False
        return True
            