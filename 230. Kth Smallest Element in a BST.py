# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # # 第一种，采用堆栈的方法 (beats 22%)
    # def kthSmallest(self, root, k):
    #     """
    #     :type root: TreeNode
    #     :type k: int
    #     :rtype: int
    #     """
    #     stack = []
    #     sol = []
    #     def helper(root):
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         if len(stack) > 0:
    #             curr = stack.pop()
    #             sol.append(curr.val)
    #             helper(curr.right)
    #     helper(root)
    #     return sol[k-1]
    
    # # 第二种，inorder (beats 55%)
    # def kthSmallest(self, root, k):
    #     def helper(root):
    #         if not root:
    #             return []
    #         return helper(root.left) + [root.val] + helper(root.right)
    #     return helper(root)[k-1]
    
    # 第三种，带标签的stack (beats 97%)
    def kthSmallest(self, root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right    
    
        
            