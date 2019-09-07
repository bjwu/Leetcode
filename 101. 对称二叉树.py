# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#  递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val == q.val:
                return helper(p.left, q.right) and helper(p.right, q.left)
            else:
                return False
        if not root:
            return True
        else:
            return helper(root.left, root.right)

#  迭代
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack_1 = [root]
        stack_2 = [root]
        while stack_1 and stack_2:
            curr_1, curr_2 = stack_1.pop(), stack_2.pop()
            if not curr_1 and not curr_2:
                continue
            elif not curr_1 or not curr_2:
                return False
            elif curr_1.val == curr_2.val:
                stack_1.append(curr_1.right)
                stack_1.append(curr_1.left)
                stack_2.append(curr_2.left)
                stack_2.append(curr_2.right)
            else:
                return False
        return True