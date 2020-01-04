"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        ans = [root.val]
        if root.left:
            stack.append((root.left, 1))
        if root.right:
            stack.append((root.right, 1))
        while stack:
            curr = stack.pop(0)
            if not stack or curr[1] != stack[0][1]:
                ans.append(curr[0].val)
            if curr[0].left:
                stack.append((curr[0].left, curr[1]+1))
            if curr[0].right:
                stack.append((curr[0].right, curr[1]+1))
        return ans
    
# 我的解答是把每一层的元素从左往右都写出来，但是为什么不从右往左，每次只写第一个元素呢？
# ```py
# class Solution:
#     def rightSideView(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         result = []
#         self.recursive(root,1,result)
#         return result
#     def recursive(self, root, depth, result):
#         if root is None:
#             return
#         if depth > len(result):
#             result.append(root.val)
#         self.recursive(root.right,depth+1, result)
#         self.recursive(root.left,depth+1, result)
# 	```      
	
	