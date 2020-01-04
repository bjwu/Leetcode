"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        newprices = [prices[0]]
        for i in range(1, len(prices)):
            if prices[i] != prices[i-1]:
                newprices.append(prices[i])
        prices = newprices
        if len(prices) < 2:
            return 0
        # 找到局部极大极小值就行
        condition = 1  # 1为找买价，0为找卖价
        buy, sell = [], []
        if prices[0] < prices[1]:
            buy.append(prices[0])
            condition = 0  # 1为找买价，0为找卖价
        for i in range(1, len(prices)-1):
            if condition and prices[i]<prices[i-1] and prices[i]<prices[i+1]:
                condition = 0
                buy.append(prices[i])
                continue
            if not condition and prices[i]>prices[i-1] and prices[i]>prices[i+1]:
                condition=1
                sell.append(prices[i])
                continue
        if not condition:
            if prices[-1] > prices[-2]:
                sell.append(prices[-1])
            else:
                buy.pop()
        print(buy,sell)
        return sum(sell) - sum(buy)

# 这道题把东西搞复杂了，我要找的是波峰和波谷，但是完全没有必要这么找
# 下面的代码就挺好的

 # while (i < prices.length - 1) {
 #    之所以下面用while，就是为了到达最后一个相等的元素
 #    while (i < prices.length - 1 && prices[i] >= prices[i + 1])
 #        i++;
 #    valley = prices[i];
 #    while (i < prices.length - 1 && prices[i] <= prices[i + 1])
 #        i++;
 #    peak = prices[i];
 #    maxprofit += peak - valley


                
####### 之前看到的，真是牛逼
# 这个题目只要还是要发现这个算法的独特性。在list中，任意两数相减等于这两数中间的数依次相减之和

def maxProfit2(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))

    