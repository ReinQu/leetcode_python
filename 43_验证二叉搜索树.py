"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
有效 二叉搜索树定义如下：
节点的左子树只包含 严格小于 当前节点的数。
节点的右子树只包含 严格大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
class Solution1:#按照层序遍历，遍历每一个结点，判断每一个结点的左右子树是否符合题意
    def isValidBST(self, root: TreeNode | None) -> bool:
        queue=collections.deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                    if node.left.val>=node.val:return False
                if node.right:
                    queue.append(node.right)
                    if node.right.val<=node.val:return False
        return True
"""以上做法是我的错误做法，题目条件没读清楚"""
from math import inf
class Solution2:#中序遍历，则输出结果严格递增；用前驱结点比较大小
    def isValidBST(self, root: TreeNode | None) -> bool:
        pre,res=-inf,True
        def dfs(root):
            if not root:return
            dfs(root.left)
            nonlocal pre,res
            if root.val<=pre:res=False#当前结点小于前驱结点
            pre=root.val#pre记录上一个结点的值
            dfs(root.right)
        dfs(root)
        return res

        