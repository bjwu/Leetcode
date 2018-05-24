# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self._isSymTree(root.left, root.right)
    def _isSymTree(self, leftT, rightT):
        if leftT==None and rightT==None: 
            return True
        elif leftT==None or rightT==None:
            return False
        else:
            return leftT.val==rightT.val and self._isSymTree(leftT.left,rightT.right) and self._isSymTree(leftT.right,rightT.left)