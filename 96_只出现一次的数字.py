"""
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
"""
class Solution:#异或运算：两个二进制相同为0，不同为1
    def singleNumber(self, nums: List[int]) -> int:
        #a
        #任何数字和0异或，结果都是该数字；任何数字和自己异或，结果都是0
        x=0
        for num in nums:
            x^=num
        return x
            