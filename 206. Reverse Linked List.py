# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


## 递归是这样的            
class Solution(object):
    def reverseList(self, head, prev=None):
        if not head:
          return prev
  
        curr, head.next = head.next, prev
        return self.reverseList(curr, head)
	
