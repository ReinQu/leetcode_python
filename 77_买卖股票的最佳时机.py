"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""
class Solution1:#暴力枚举
    def maxProfit(self, prices: list[int]) -> int:
        res=0
        for i,num in enumerate(prices):
            if i==len(prices)-1:break
            for j in range(i+1,len(prices)):
                if prices[j]>prices[i]:
                    res=max(res,prices[j]-prices[i])
        return res

class Solution2:#贪心算法：更新前i天的最低价格cost
    def maxProfit(self, prices: list[int]) -> int:
        cost,profit=float('+inf'),0#py中的float可以将字符串inf转换为浮点数
        for price in prices:
            cost=min(cost,price)
            profit=max(price,price-cost)
        return profit