"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
#  跟链表有关的题要注意用哨兵

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 这道题其实就是数组的变形（108题）
# 其实就找到该链表的中间位置就行，其他的递归跟108题一样

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 使用两个指针来判断单链表的中间位置
        if head:
            soldier = ListNode(0)
            soldier.next = head
            p0, p1, p2 = soldier, soldier, soldier
            while p2 and p2.next:
                p0 = p1
                p1 = p1.next
                p2 = p2.next.next
            # p2到达终点，p1到达中点
            root = TreeNode(p1.val)

            p0.next = None
            root.left = self.sortedListToBST(soldier.next)
            root.right = self.sortedListToBST(p1.next)
            return root
        else:
            return None