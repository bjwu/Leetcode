# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            return min(self._TreeDepth(root.left), self._TreeDepth(root.right)) + 2
    
    def _TreeDepth(self, root):
        # 无意义
        if not root:
            return float('inf')
        # leaf node
        if not root.left and not root.right:
            return 0
        else:
            return min(self._TreeDepth(root.left), self._TreeDepth(root.right))+1
        