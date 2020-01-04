    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        for _ in range(m-1):
            pre = pre.next
        start = pre.next
        p1, p2 = start, start.next
        for _ in range(n-m):
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        pre.next = p1
        start.next = p2
        return dummy.next