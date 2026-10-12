"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其 最大路径和 。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from math import inf
class Solution:#因为路径是单向的，分别输出左子树和右子树最大长度，依旧先序遍历
    def maxPathSum(self, root: TreeNode | None) -> int:
        ans=-inf
        def dfs(node:Optional[TreeNode])->int:
            if not node:return 0
            l_sum=dfs(node.left)
            r_sum=dfs(node.right)
            nonlocal ans
            ans=max(ans,l_sum+r_sum+node.val) 
            return max(0,max(l_sum,r_sum)+node.val)#最长的一条边，不然会有两个方向

        dfs(root)
        return ans

