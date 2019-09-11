"""
根据一棵树的前序遍历与中序遍历构造二叉树。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder:
            val = preorder[0]
            root = TreeNode(val)
            idx_inorder = inorder.index(val) #根节点在中序遍历中的索引
            left_in, right_in = inorder[:idx_inorder], inorder[idx_inorder+1:]
            left_pre, right_pre = preorder[1:len(left_in)+1], preorder[len(left_in)+1:]
            root.left = self.buildTree(left_pre, left_in)
            root.right = self.buildTree(right_pre, right_in)
            return root
        else:
            return None