"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:#反向先序遍历：右->左->根
    def flatten(self, root: TreeNode | None) -> None:
        self.prev=None
        def dfs(node):
            if not node:return
            dfs(node.right)
            dfs(node.left)
            node.left=None
            node.right=self.prev
            self.prev=node
        dfs(root)


