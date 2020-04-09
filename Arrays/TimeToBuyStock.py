# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one
# share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

class Solution:
    def maxProfit(self, prices):
    	"""
    	:type prices: List[int]
    	:rtype: int
    	"""
        numTimes = len(prices)
        if numTimes == 0 or numTimes == 1:
            return 0
        
        else:
            profitList : List[int] = []
            profitList.append(0)
            # value of doing nothing
            currTrade : int = 0
            maxTrade : int = 0
            for i in range(1, numTimes):
                trade = prices[i] - prices[i-1]
                if(profitList[i-1] > 0):
                    currTrade = profitList[i-1] + trade
                    profitList.append(currTrade)
                    if currTrade > maxTrade:
                        maxTrade = currTrade
                else:
                    currTrade = trade
                    profitList.append(currTrade)
                    if currTrade > maxTrade:
                        maxTrade = currTrade
            return maxTrade