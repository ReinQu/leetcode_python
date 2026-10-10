"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:#递归法，对于任意结点，其镜像就是简单的交换左右子树
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:return
        tmp=root.left
        root.left=self.invertTree(root.right)
        root.right=self.invertTree(tmp)
        return root

class Solution2:#栈
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:return
        stack=[root]
        while stack:
            node=stack.pop()#pop默认最后一个参数
            if node.left:stack.append(node.left)
            if node.right:stack.append(node.right)
            node.left,node.right=node.right,node.left
        return root