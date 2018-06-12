# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return []
        def buildTreehelper(preorder, inorder, root):
            root_index = inorder.index(preorder[0])
            if root_index != 0:
                root.left = TreeNode(preorder[1])
                buildTreehelper(preorder[1:root_index+1], inorder[:root_index], root.left)
            if root_index != len(inorder)-1:
                root.right = TreeNode(preorder[root_index+1])
                buildTreehelper(preorder[root_index+1:], inorder[root_index+1:], root.right)
        R = TreeNode(preorder[0])
        buildTreehelper(preorder, inorder, R)
        return R