# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这两个题的核心思想就是先找递归的时候先找根节点，分别从前序遍历的开头和后序遍历的结尾找

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if postorder:
            val = postorder[-1]
            root = TreeNode(val)
            idx_inorder = inorder.index(val)
            left_in, right_in = inorder[:idx_inorder], inorder[idx_inorder+1:]
            left_post, right_post = postorder[:len(left_in)], postorder[len(left_in):-1]
            root.left = self.buildTree(left_in, left_post)
            root.right = self.buildTree(right_in, right_post)
            return root
        else:
            return None