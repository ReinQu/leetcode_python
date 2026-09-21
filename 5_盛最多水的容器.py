"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
"""

class Solution1:#暴力的解法，方案可行但是时间复杂度，也是自己做出来的第一道题
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        result=0
        for i in range(0,n):
            for j in range(i+1,n):
                volume=(j-i)*min(height[i],height[j])
                result=max(result,volume)

        return result

class Solution2:#核心：移动高度小的那条边，因为本来就会变窄，大变小知会更小
    def maxArea(self,height:list[int])->int:
        n=len(height)
        left=0
        right=n-1
        result=0
        while left<right:
            volume=(right-left)*min(height[left],height[right])
            result=max(result,volume)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return result

def main():
    height=[1,8,6,2,5,4,8,3,7]
    sol1=Solution1()
    sol2=Solution2()
    print(sol1.maxArea(height))
    print(sol2.maxArea(height))

if __name__=="__main__":
    main()





