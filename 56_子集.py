"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""
class Solution1:#回溯＋dfs
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        ans=[]
        path=[]

        def dfs(i:int)->None:
            if i==n:#说明前面的都选完了，子集构造完毕
                ans.append(list(path))
                return
            #先不选
            dfs(i+1)
            #再选：把当前数字放进path，再处理下一个数字
            path.append(nums[i])
            dfs(i+1)
            path.pop()
        dfs(0)
        return ans
#回溯的标准结构：1、做出选择2、递归探索3、撤销选择


