# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        
        if leftDepth == rightDepth:
        # 如果左右子树深度相等，则左子树为完全二叉树，返回左子树+rootnode结点树，然后对右子树进行递归    
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)
    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)