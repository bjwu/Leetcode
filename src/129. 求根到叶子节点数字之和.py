"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        sol = []
        def helper(root, path):
            if not root:
                return
            if not root.left and not root.right:  # leaf node
                print(path+str(root.val))
                sol.append(int(path+str(root.val)))
                return
            helper(root.left, path+str(root.val))
            helper(root.right, path+str(root.val))
        helper(root, '')
        return sum(sol)