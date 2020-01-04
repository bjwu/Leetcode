
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        phead = ListNode(0)
        phead.next = head
        p1, p2 = phead, phead
        for _ in range(n):
            p2 = p2.next
        while p2 != None:
            p1before = p1
            p1 = p1.next
            p2 = p2.next
        p1before.next = p1.next
        return phead.next