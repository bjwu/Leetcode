
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(node, level):
            if not node:
                return
            else:
                if level%2==1:
                    sol[level-1].append(node.val)
                else:
                    sol[level-1].insert(0, node.val)
                if len(sol) == level:
                    sol.append([])
                helper(node.left, level+1)
                helper(node.right, level+1)
                    
                    
        sol = [[]]
        helper(root, 1)
        return sol[:-1]
        
