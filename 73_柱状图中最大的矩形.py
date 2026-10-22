"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(-1)#看下面
        st=[-1]#用于最左边的柱子的高度计算
        ans=0
        for right,h in enumerate(heights):
            while len(st)>1 and heights[st[-1]]>=h:#当前柱子h是第一个小于栈顶柱子
                i=st.pop()#弹出柱子对应的下标
                left=st[-1]#新的栈顶就是它左侧比他矮的第一个柱子，因为比他大的会先弹出
                ans=max(ans,heights[i]*(right-left-1))
            st.append(right)#处理完之后，当前柱子的高度就严格大于其余柱子的高度
        return ans