"""
给定一个二叉树，原地将它展开为链表。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 其实就是先序遍历，下面采用迭代的方法
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head = TreeNode(0)
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                stack.append(curr.right)
                stack.append(curr.left)
                curr.left = None
                curr.right = None
                head.right = curr
                head = curr

# 这个是用后序遍历使用的递归方法
# 后序遍历由于可以先处理左子树和右子树，根节点在最后处理。所以先找到左子树的最右节点，然后再把右子树插到左子树的最右节点后，最后将
# 根节点的右子树变为当前的左子树，依次递归。
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root1):
            if not root1:
                return
            else:
                helper(root1.left)
                helper(root1.right)
                # 找到左子树的最右节点
                curr = root1.left
                if curr:
                    while curr:
                        pre = curr
                        curr = curr.right
                    pre.right = root1.right
                    root1.right = root1.left
                    root1.left = None
        helper(root)

