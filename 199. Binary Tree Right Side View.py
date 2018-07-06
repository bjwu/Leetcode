# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ### 其实就是一个levelwise遍历的过程
        memo = []
        def helper(root, level):
            if not root:
                return
            else:
                if len(memo) == level:
                    memo.append([])
                memo[level].append(root.val)
                helper(root.left, level+1)
                helper(root.right, level+1)
        helper(root, 0)
        return [s[-1] for s in memo]
# 我的解答是把每一层的元素从左往右都写出来，但是为什么不从右往左，每次只写第一个元素呢？
# ```py
# class Solution:
#     def rightSideView(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         result = []
#         self.recursive(root,1,result)
#         return result
#     def recursive(self, root, depth, result):
#         if root is None:
#             return
#         if depth > len(result):
#             result.append(root.val)
#         self.recursive(root.right,depth+1, result)
#         self.recursive(root.left,depth+1, result)
# 	```      
	
	