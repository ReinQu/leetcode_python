"""
给定一个二叉树 root ，返回其最大深度。
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:#后序遍历，树的深度等于max（左子树深度，右子树深度）+1，一直到叶结点，其深度为1
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.left))+1

class Solution2:#层序遍历，队列
    def maxDepth(self, root: TreeNode | None) -> int: 
        if not root:return 0
        queue,res=[root],0
        while queue:
            tmp=[]
            for node in queue:
                if node.left:tmp.append(node.left)
                if node.right:tmp.append(node.right)
            queue=tmp
            res+=1
        return res