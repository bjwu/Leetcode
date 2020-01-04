"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
"""

# 这个题我想了很久，之前一直想用递归来做，从上往下，没有办法估计具体的建树数目
# 所以无奈只能看解答，然后从下往上进行
# 某根节点的建树数目是他可建左子树和右子树数目的乘积


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def helper(start, end):
            all_trees = []
            if start > end:
                return [None]
            for curr in range(start, end + 1):
                # 该节点curr可建立的左子树
                left = helper(start, curr - 1)
                # 该节点curr可建立的右子树
                right = helper(curr + 1, end)
                # 依次建立树
                for l in left:
                    for r in right:
                        state = TreeNode(curr)
                        state.right = r
                        state.left = l
                        all_trees.append(state)
            return all_trees

        return helper(1, n) if n > 0 else []