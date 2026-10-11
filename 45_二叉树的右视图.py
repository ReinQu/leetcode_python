"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
class Solution:#层序遍历，输出最右端的值
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return[]
        queue,p=collections.deque(),[]
        queue.append(root)
        while queue:
            tmp=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
                tmp.append(node)
            p.append(tmp)
        res=[]
        for i in range(len(p)):
            res.append(p[i][-1].val)
        return res



        