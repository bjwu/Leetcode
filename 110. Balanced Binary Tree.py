# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self._TreeDepth(root.right)-self._TreeDepth(root.left))<=1
            
    def _TreeDepth(self, root):
        if root == None:
            return 0
        else:
            return max(self._TreeDepth(root.left), self._TreeDepth(root.right))+1


# 树的问题通常可以用两种方法解决：
# 一种是top down，这种方法就是从上而下的迭代或者递归
# 一种是bottom up，这种方法是利用DFS的思想

# 我用的第一种方法，但可以修改成如下形式，不用每次都求得每个node的深度，而是在每次求深度的过程中自动判断该node是否平衡：
class Solution(object):
    def isBalanced(self, root):
            
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1