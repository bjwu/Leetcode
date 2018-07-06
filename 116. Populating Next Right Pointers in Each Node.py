# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        def helper(root):
            if not root.left or not root.right:
                return 
            else:
                root.left.next = root.right
                pleft, pright = root.left, root.right
                while pleft.right != None and pright.left != None:
                    pleft.right.next = pright.left
                    pleft, pright = pleft.right, pright.left
            helper(root.left)
            helper(root.right)
        helper(root)
        
                    