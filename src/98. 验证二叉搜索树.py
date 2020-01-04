"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 判断中序遍历是否是有序的
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            if root:
                return inorder(root.left) + [root.val] + inorder(root.right)
            else:
                return []
        inord = inorder(root)
        for i in range(1, len(inord)):
            if inord[i-1] >= inord[i]:
                return False
        return True

# 中序遍历也可以用迭代，这样就不用保存一个中序的数组了
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        curr = -float('inf')
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val > curr:
                    curr = root.val
                else:
                    return False
                root = root.right
        return True
