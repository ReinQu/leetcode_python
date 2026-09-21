"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        slow=0
        n=len(height)
        result=0
        prev=list()
        count=0
        for fast in range(n):
            if slow==fast:
                continue
            if prev==[]:
                prev.append(height[fast])
                count+=1
                continue
            if height[fast]>max(prev) and height[slow]>max(prev):



