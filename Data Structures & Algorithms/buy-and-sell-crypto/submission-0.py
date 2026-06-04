class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num = len(prices)
        maxprofit = 0
        for i in range(num-1):
            for j in range(i+1,num):
                if prices[i] < prices[j]:
                    if maxprofit <= (prices[j]-prices[i]):
                        maxprofit = (prices[j]-prices[i])
        return maxprofit