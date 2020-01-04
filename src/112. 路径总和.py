"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        def helper(root, sum):
            if not root:
                return True if sum == 0 else False
            if (not root.left and not root.right) or (root.left and root.right):
                return helper(root.left, sum-root.val) or helper(root.right, sum-root.val)
            elif not root.left:
                return helper(root.right, sum-root.val)
            elif not root.right:
                return helper(root.left, sum-root.val)
        return helper(root, sum)

# 以上是我的解法，但是真的是跟💩一样，其实主要是没有太考虑是否是根节点的问题
# 叶节点求法：（在这种回溯法的题目中，一定要记住，且一定要判断）
# if not root.left and not root.right:

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 这一步很关键啊，因为叶节点压根就不会到这一步来
        # 这一步就可以针对某节点只有一个子树的情况了
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。