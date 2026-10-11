"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（k 从 1 开始计数）。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:#二叉搜索树一定符合左子树<结点<右子树的定义，中序遍历的第k个结点
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if not root:return
            dfs(root.left)
            if self.k==0:return
            self.k-=1
            if self.k==0:self.res=root.val
            dfs(root.right)

        self.k=k#如果用普通k而不是self.k，def中没法读取函数外的k
        dfs(root)
        return self.res


