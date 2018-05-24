# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        BST = TreeNode(nums[len(nums)//2])
        self._subTree(nums[0:len(nums)//2], nums[len(nums)//2+1:], BST)
        return BST
    def _subTree(self, leftT, rightT, BST):
        ## len(rightT) - len(leftT) = 0/-1
        if not rightT and not leftT:
            return None
        elif not rightT:
            BST.left = TreeNode(leftT[0])
        else:
            BST.left = TreeNode(leftT[len(leftT)//2])
            BST.right = TreeNode(rightT[len(rightT)//2])
            self._subTree(leftT[0:len(leftT)//2], leftT[len(leftT)//2+1:], BST.left)
            self._subTree(rightT[0:len(rightT)//2], rightT[len(rightT)//2+1:], BST.right)

                     
 
#  这个问题虽然我打败了98%的人，但是代码太复杂，完全没有必要再加一个函数
# 所以这个回答我觉得很好


    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root