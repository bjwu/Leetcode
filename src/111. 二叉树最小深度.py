"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root:
            dep_l, dep_r = self.minDepth(root.left), self.minDepth(root.right)
            # 关键在这一步要注意
            # 可能出现根节点只有一个子树的问题
            if not root.left or not root.right:
                return dep_l + dep_r + 1
            return min(dep_l, dep_r) + 1
        return 0