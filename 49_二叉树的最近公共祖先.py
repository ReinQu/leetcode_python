"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #没找到就返回空，找到pq返回pq的结点
        if not root:return None
        if root==p or root==q:return root
        #前序遍历，直到找到pq，从底部往上返回父节点
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        #如果pq分别在该父节点的左右子树，返回该父节点
        if left and right:return root
        #只有一侧找到，就继续向上传递结果
        if left:return left
        else:return right

