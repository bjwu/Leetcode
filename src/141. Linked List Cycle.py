# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

################# Use two pointers #################
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        runningman1 = head
        runningman2 = head.next
        while runningman2 != None and runningman2.next != None:
            if runningman2 == runningman1 or runningman2.next == runningman1:
                return True
            runningman2 = runningman2.next.next
            runningman1 = runningman1.next
        return False

################ More simple #####################
# 集合里装着的应该是listnode的地址
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next