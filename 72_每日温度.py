"""
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
"""
class Solution1:#从左到右
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0]*n
        st=[]#stack存下标
        for i,t in enumerate(temperatures):
            while st and t>temperatures[st[-1]]:#为什么是while：i对应j之前的栈也要清空
                j=st.pop()
                ans[j]=i-j
            st.append(i)
        return ans

class Solution2:#从右到左
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            t=temperatures[i]
            while st and t>=temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i]=st[-1]-i
            st.append(i)
        return ans

