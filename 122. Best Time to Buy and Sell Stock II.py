class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy = prices[0]
        wholeprofit = 0
        maxprofit = 0
        for i,p in enumerate(prices):
            maxprofit = max(maxprofit, p-buy)
            if (maxprofit > (p-buy)) or (i == len(prices)-1):
                buy = p
                wholeprofit += maxprofit
                maxprofit = 0
        return wholeprofit
                
                
# 这个题目只要还是要发现这个算法的独特性。在list中，任意两数相减等于这两数中间的数依次相减之和

def maxProfit2(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))

    