# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        ### merge sort recursion
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            ### find the middle
            p1 = p2 = dummy
            while p2 != None and p2.next != None:
                p2 = p2.next.next
                p1 = p1.next
            ### divide into two and return the sorted
            head2 = self.sortList(p1.next)
            p1.next = None
            head1 = self.sortList(dummy.next)
            ### sort the two parts
            rhead = dummyrhead = ListNode(0)
            while head1 != None and head2 != None:
                if head1.val < head2.val:
                    rhead.next = head1
                    head1 = head1.next
                else:
                    rhead.next = head2
                    head2 = head2.next
                rhead = rhead.next
            if head1 == None:
                rhead.next = head2
            else:
                rhead.next = head1
            return dummyrhead.next