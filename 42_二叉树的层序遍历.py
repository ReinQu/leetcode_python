"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):         
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:return []
        res,queue=[],collections.deque()
        queue.append(root)
        while(queue):
            tmp=[]
            for _ in range(len(queue)):#循环的次数固定，即使后面加入新值也无关
                node=queue.popleft()
                #Python 中使用 collections 中的双端队列 deque() ，其 popleft() 方法可达到 O(1) 时间复杂度
                tmp.append(node.val)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            res.append(tmp)
        return res
        
