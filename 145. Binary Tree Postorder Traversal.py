# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ### 递归实现
        # def helper(root):
        #     if not root:
        #         return []
        #     else:
        #         return helper(root.left)+helper(root.right)+[root.val]
        # return helper(root)
        
        # 循环实现
        stack = []
        sol = []
        curr = root
        while stack or curr:
            if curr:
                sol.append(curr.val)
                stack.append(curr.left)
                curr = curr.right
            else:
                curr = stack.pop()
        return sol[::-1]
        
        
        