"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""

class Solution1:#单调栈
    def trap(self, height: list[int]) -> int:
        result=0
        stack=list()
        n=len(height)
        for i,h in enumerate(height):
            while stack and h>height[stack[-1]]:#当前值大于栈顶元素
                top=stack.pop()
                if not stack:
                    break
                left=stack[-1]
                currWidth=i-1-left
                currHeight=min(height[i],height[left])-height[top]
                result+=currWidth*currHeight
            stack.append(i)

        return result

class Solution2:#双指针，哪边低就算哪边的水
    def trap(self,height:list[int])->int:
        left,right=0,len(height)-1
        leftMax=rightMax=0
        result=0
        while left<right:
            leftMax=max(leftMax,height[left])
            rightMax=max(rightMax,height[right])
            
            if height[left]<height[right]:
                result+=leftMax-height[left]
                left+=1
            else:
                result+=rightMax-height[right]
                right-=1
        return result


def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol1=Solution1()
    sol2=Solution2()
    print(sol1.trap(height))
    print(sol2.trap(height))

if __name__=="__main__":
    main()





        



