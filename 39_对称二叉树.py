"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:#递归，对于任意对称结点L和R，有L.val=R.val，L.left.val=R.right.val
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def recur(L,R):
            if not L and not R:return True#叶结点
            if not L or not R or L.val!=R.val:return False#L和R只有其一或两者只不等
            return recur(L.left,R.right) and recur(L.right,R.left)
        return not root or recur(root.left,root.right)
