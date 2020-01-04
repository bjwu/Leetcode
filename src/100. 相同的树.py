"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(pp, qq):
            # 都是None节点
            if not pp and not qq:
                return True
            # 如果有一个是None节点（必须写在这个位置，因为防止下面None进行操作）
            elif not pp or not qq:
                return False
            # 判断当前节点相同
            elif pp.val == qq.val:
                return helper(pp.left, qq.left) and helper(pp.right, qq.right)
            else:
                return False
        return helper(p, q)