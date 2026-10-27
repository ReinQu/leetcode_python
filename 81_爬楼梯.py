"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""
class Solution:#f(0)=0,f(1)=1,f(2)=2
    def climbStairs(self, n: int) -> int:
        a,b=1,1#这里相当于从0和1开始
        for _ in range(n-1):#循环n-1次
            a,b=b,a+b#a是当前较小的状态值，b是较大的状态值
        return b
