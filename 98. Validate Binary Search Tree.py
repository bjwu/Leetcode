# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder(root):
            if not root:
                return []
            else:
                return inorder(root.left)+[root.val]+inorder(root.right)
        result = inorder(root)
        return (result == sorted(result)) and (len(result) == len(set(result)))