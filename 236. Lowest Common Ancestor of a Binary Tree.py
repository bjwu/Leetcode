# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    #     这个方法可以借鉴很多题目：
    # 1、p和q是tree中的结点，可以直接对它使用left，right等操作
    # 2、完全可以生成一个parent字典，生成方法如题目，很方便啊哈哈
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q



    # DP算法top-bottom，超时
    #     if root.val == p.val or root.val == q.val:
    #         return root
    #     if (q.val in self.inorder(root.left) and p.val in self.inorder(root.right)) or (q.val in self.inorder(root.right) and p.val in self.inorder(root.left)):
    #         return root
    #     if q.val in self.inorder(root.left) and p.val in self.inorder(root.left):
    #         return self.lowestCommonAncestor(root.left,p,q)
    #     if q.val in self.inorder(root.right) and p.val in self.inorder(root.right):
    #         return self.lowestCommonAncestor(root.right,p,q)
    # def inorder(self,root):
    #     if not root:
    #         return []
    #     return self.inorder(root.left)+[root.val]+self.inorder(root.right)
    
        # dfs

            
            
            