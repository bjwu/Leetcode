# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root, output):
            if not root:
                return 
            helper(root.left, output)
            output.append(root.val)
            helper(root.right, output)
        sol = []
        helper(root, sol)
        return sol