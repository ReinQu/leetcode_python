"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
"""
class Solution:#递归+回溯+原地交换
    def permute(self, nums: list[int]) -> list[list[int]]:
        res=[]
        def dfs(x):
            if x==len(nums)-1:
                res.append(list(nums))#需要注意 res.append(list(nums)) 这一行代码中的 list(nums) 操作，这里相当于对 nums 进行了一次浅拷贝，然后放到 res 这个 list 中。如果不使用 list(nums)，而是直接 res.append(nums)，这里传入的 nums 对象会在后续对 nums 的操作中发生变化，导致最后每个 res 中的 nums 都是同一个 list.
                return
            for i in range(x,len(nums)):
                nums[i],nums[x]=nums[x],nums[i]
                dfs(x+1)
                nums[i],nums[x]=nums[x],nums[i]#回溯：撤销本轮选择，让数组恢复到进入本轮选择之前的状态。
        dfs(0)
        return res

