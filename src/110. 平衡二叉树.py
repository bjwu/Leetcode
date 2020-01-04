"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 这里注意两点
# 1. 这里的result变量没法在depth函数里使用，必须加self
# 2. 求二叉树的深度要记住
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.result = True
        def depth(root):
            if root:
                dep_left, dep_right = depth(root.left), depth(root.right)
                if abs(dep_left - dep_right) >= 2:
                    self.result = False
                return max(dep_left, dep_right) + 1
            else:
                return 0
        depth(root)
        return self.result
