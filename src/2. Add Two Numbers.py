"""
这道题是简单的初等数学题，用链表按照正常数学思路可以解决
主要注意两个问题：
1. 进位的英文名：carry
2. python的if语法的一句写法两种形式：
    if l1: l1 = l1.next  # or l1 = l1.next if l1 else None
    n1 = l1.val if l1 else 0
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)   ### 哨兵
        nsum = head
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            nnew = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10
            nsum.next = ListNode(nnew)
            nsum = nsum.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return head.next
