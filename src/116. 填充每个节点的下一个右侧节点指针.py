"""
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = []
        if root.left:
            stack.append((root.left, 1))
        if root.right:
            stack.append((root.right, 1))
        while stack:
            curr = stack.pop(0)
            if stack and curr[1] == stack[0][1]:
                curr[0].next = stack[0][0]
            if curr[0].left: # if not leaf
                stack.append((curr[0].left, curr[1]+1))
            if curr[0].right:
                stack.append((curr[0].right, curr[1]+1))
        return root
# 自己的代码占用空间过多
# 这个算法简直奇特
# 要善于发现规律啊
def connect(self, root: 'Node') -> 'Node':
    if not root:
        return
    if root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
    self.connect(root.left)
    self.connect(root.right)
    return root

#
# 作者：powcai
# 链接：https: // leetcode - cn.com / problems / populating - next - right - pointers - in -each - node / solution / di - gui - he - die - dai - by - powcai - 4 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#