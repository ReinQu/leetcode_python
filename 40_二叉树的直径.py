"""
给你一棵二叉树的根节点，返回该树的 直径 。
二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
两节点之间路径的 长度 由它们之间边数表示。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:#任意节点的最长深度都是其max（左子树，右子树）
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node:Optional[TreeNode])->int:
            if node is None:
                return 0
            l_len=dfs(node.left)
            r_len=dfs(node.right)
            nonlocal ans#表明ans是一个函数外层的变量，而不是新建的
            ans=max(ans,l_len+r_len)
            return max(l_len,r_len)+1
        dfs(root)
        return ans
            
