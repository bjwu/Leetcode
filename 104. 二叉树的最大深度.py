# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 用回溯的思路
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(p, level):
            if not p:
                return level
            return max(helper(p.left, level+1), helper(p.right,level+1))
        return helper(root, 0)