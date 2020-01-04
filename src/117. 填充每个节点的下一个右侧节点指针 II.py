"""
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 区别在于不是完全平衡树了
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 跟我自己一样的做法
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