# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = Queue()
        output = []
        if root:
            queue.enqueue(root)
            output.append([root.val])
        while not queue.is_empty():
            levelout = []
            for _ in range(queue.size()):
                node = queue.dequeue()
                if node.left != None:
                    levelout.append(node.left.val)
                    queue.enqueue(node.left)
                if node.right != None:
                    levelout.append(node.right.val)
                    queue.enqueue(node.right)
            if levelout:
                output.insert(0,levelout)
        return output

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items ==[]
    # input在前，output在后
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def show(self):     
        return self.items


# 这道题用queue我觉得还是要好理解一点，但是唯一的坏处就是在插入的时候结果的限制，不能append，只能insert，所以时间变长。
# 如果用stack的话，可以给每一个node加一个level标签，如下代码：
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        closed = []
        if not root:
            return closed
        stack = [(root, 0)]
        tl = -1
        while stack:
            t, level = stack.pop(0)
            if t:
                if  level > tl:
                    tl += 1
                    closed.insert(0, [])
                closed[0].append(t.val)
                level += 1
                stack.append((t.left, level))
                stack.append((t.right, level))
           
        return closed