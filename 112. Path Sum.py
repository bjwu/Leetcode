# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.stack = Stack()
        self.count = 0
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        self.stack.push(root.val)
        self.count += root.val
        ## leaf node
        if not root.left and not root.right:
            if self.count == sum:
                return True
            else:
                self.count -= self.stack.pop()
                return False
        if root.left and self.hasPathSum(root.left, sum):
            return True
        if root.right and self.hasPathSum(root.right, sum):
            return True
        ## 所有该结点下的路径都遍历完毕后
        self.count -= self.stack.pop()
        
        if self.stack.is_empty():
            return False
            
            
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

            
# 这道题我用的是DFS的思想，但是才baet了25%的伙伴。在看discussion的过程中，发现人的智商真是无限的。

# 下面的代码采用up down的形式，相当于把树🌲的每一层都隔绝，是一个贪心问题。

# **贪心算法**通常都是自顶向下的设计，做出一个选择，然后求解剩下的那个子问题。

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        ## 如果是叶结点
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)