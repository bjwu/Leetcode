class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        else:
            maxprofit = 0
            minbuy = float('inf')
            for p in prices:
                maxprofit = max(maxprofit,p-minbuy)
                minbuy = min(minbuy,p)
            return maxprofit