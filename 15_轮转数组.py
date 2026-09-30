"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
"""
class Solution1:暴力枚举，但是要注意k可能很大，如果k打一轮的话就不行，所以要重新定义k
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        for i in range(k):
            for j in range(len(nums) - 1, 0, -1):#每次将最后一个元素移到最前面就行
                temp = nums[j - 1]
                nums[j - 1] = nums[j]
                nums[j] = temp

    
class Solution2:#数组翻转，三翻法
    def rotate(self, nums: list[int], k: int) -> None:
        k=k%len(nums)
        nums.reverse()
        nums[0:k]=nums[0:k][::-1]
        nums[k:]=nums[k:][::-1]

