class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,5,3,6,4]
        #  l  r
        #sliding window

        l = 0
        r = 1
        maxP = 0

        while r < len(prices):
            profit = 0
            if prices[l] > prices[r]:
                l = r

            profit = prices[r] - prices[l]

            maxP = max(maxP, profit)
            r += 1
        
        return maxP

            





        