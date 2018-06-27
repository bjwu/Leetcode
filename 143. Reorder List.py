# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        llist = []
        p = pp = head
        while p != None:
            llist.append(p)
            p = p.next
        p1, p2 = 1, len(llist)-1
        while p1 < p2:
            llist[p2].next = llist[p1]
            pp.next = llist[p2]
            pp.next.next = llist[p1]
            pp = pp.next.next
            p1 += 1
            p2 -= 1
        if p1 == p2:
            pp.next = llist[p1]
            pp = pp.next
        pp.next = None
        
            