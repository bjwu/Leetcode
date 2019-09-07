"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。
"""

# 记录最小值和当前遍历的之前所有效果

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        minbuy = prices[0]
        prices[0] = 0
        for i in range(1, len(prices)):
            curr = max(prices[i-1], prices[i]-minbuy)
            if prices[i] < minbuy:
                minbuy = prices[i]
            prices[i] = curr
        return prices[-1]