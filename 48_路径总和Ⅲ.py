"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:#回溯+前缀和+哈希表
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #key：从根到node的节点值之和
        #value：节点值之和的出现次数
        cnt=defaultdict(int)#初始化哈希表
        cnt[0]=1
        ans=0

        #s表示从根到node的父亲节点值之和（node的结点未计入）
        def dfs(node:Optional[TreeNode],s:int)->None:
            if node is None:return
            nonlocal ans
            s+=node.val
            ans+=cnt[s-targetSum]
            cnt[s]+=1
            dfs(node.left,s)
            dfs(node.right,s)
            cnt[s]-=1

        dfs(root,0)
        return ans
