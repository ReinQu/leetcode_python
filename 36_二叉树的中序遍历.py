"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:#常规做法，递归
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        def dfs(node:Optional[TreeNode])->None:
            if node is None:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        ans=[]
        dfs(root)
        return ans

class Solution2:#线索二叉树，将不存在右子树的结点指向前驱
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans=[]
        while root:
            #结点存在左子树，需要往左走
            if root.left:
                pre=root.left
                #怎么找前驱：一直往右走，直到尽头，或者结点的线索
                while pre.right and pre.right is not root:
                    pre=pre.right

                if pre.right is None:
                    pre.right=root#建立线索：回到root的路
                    root=root.left
                    continue

            #root的左子树访问完毕，去掉线索，恢复原样
                pre.right=None
            #赋值
            ans.append(root.val)
            #向右遍历
            root=root.right
        return ans