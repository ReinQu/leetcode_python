"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        dic={}
        for i,num in enumerate(inorder):
            dic[num]=i
        def recur(root,left,right):#根节点在前序遍历的索引root，子树在中序遍历的左右边界left、right
            if left>right:return
            node=TreeNode(preorder[root])
            i=dic[preorder[root]]#中序遍历的下标
            node.left=recur(root+1,left,i-1)#在前序遍历中左子树下标对应root+1
            node.right=recur(i-left+root+1,i+1,right)#在前序遍历中，右子树下标对应（根节点索引+左子树长度加1）
            return node
        return recur(0,0,len(inorder)-1)

 