"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:#平衡二叉树定义：每个节点的左子树和右子树的高度差都不超过 1
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None
        m=len(nums)//2
        left=self.sortedArrayToBST(nums[:m])
        right=self.sortedArrayToBST(nums[m+1:])
        return TreeNode(nums[m],left,right)