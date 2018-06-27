# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedListToBST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    def helper(head, root, position):
        if head == None:
            return
        dummyNode = ListNode(0)
        dummyNode.next = head
        prep1 = ListNode(0)
        p1 = p2 = dummyNode
        prep1.next = p1
        while p2 != None and p2.next != None:
            p2 = p2.next.next
            prep1 = p1
            p1 = p1.next
        if position == 'left':
            root.left = TreeNode(p1.val)
            newroot = root.left
        else:
            root.right = TreeNode(p1.val)
            newroot = root.right
        helper(p1.next, newroot, 'right')
        prep1.next = None
        helper(dummyNode.next, newroot, 'left')
    dummy = TreeNode(0)
    helper(head, dummy, 'left')
    return dummy.left

h = ListNode(-10)
h.next = ListNode(3)    
h.next.next = None
sortedListToBST(h)
            
        