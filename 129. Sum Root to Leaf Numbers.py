# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, path, sol):
            if not root:
                return
            else:
                path = path + str(root.val)
                if not root.left and not root.right:
                    sol.append(int(path))
                else:
                    helper(root.left, path, sol)
                    helper(root.right, path, sol)
        sol = []
        helper(root, '', sol)
        return sum(sol)