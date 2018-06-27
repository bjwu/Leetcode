# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ### 经典的回溯法无疑了
        def helper(root, currsum, path, sol):
            if not root.left and not root.right:
            ###is leaf?
                if currsum+root.val == sum:
                    sol.append(path+[root.val])
                return 
            if root.left != None:
                helper(root.left, currsum+root.val, path+[root.val], sol)
            if root.right != None:
                helper(root.right, currsum+root.val, path+[root.val], sol)
        sol=[]
        if not root:
            return []
        helper(root, 0, [], sol)
        return sol
                 
            
        