"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 这似乎就是经典的回溯法了，因为需要遍历所有的路径
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        sol = []
        def helper(root, sum, path):
            if not root:
                return
            sum -= root.val
            if not root.left and not root.right: # reach the leaf
                if sum == 0:
                    sol.append(path+[root.val])
                else:
                    return
            else:
                helper(root.left, sum, path+[root.val])
                helper(root.right, sum, path+[root.val])
        helper(root, sum, [])
        return sol