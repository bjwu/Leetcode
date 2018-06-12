# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_index = inorder.index(postorder.pop())
            root = TreeNode(inorder[root_index])
            root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
            root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:])
            return root
            