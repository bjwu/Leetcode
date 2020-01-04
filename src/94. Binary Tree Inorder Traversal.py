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
        # 递归算法
        # def helper(root, output):
        #     if not root:
        #         return 
        #     helper(root.left, output)
        #     output.append(root.val)
        #     helper(root.right, output)
        # sol = []
        # helper(root, sol)
        # return sol
        
        # 循环算法
        stack = []
        sol = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                sol.append(curr.val)
                curr = curr.right
        return sol