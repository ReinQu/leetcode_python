"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans=[[1]]
        init=[1]
        for _ in range(numRows-1):
            if len(init)==1:
                init.append(1)
            else:
                tmp=[]
                for i in range(len(init)-1):
                    tmp.append(init[i]+init[i+1])
                tmp.append(1)
                init=[1]+tmp
                #不可以写成init[1:]=tmp，因为这没有对init的引用进行修改，在后续的append(init)中会默认为最后一次修改的init
            ans.append(init)
        return ans