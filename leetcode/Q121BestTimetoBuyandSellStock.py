from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        else:
            minPriceMapping = [prices[0] for i in range(len(prices))]
            maxGap = 0
            for i in range(1,len(prices)):
                price = prices[i]
                minPrice = min(price,minPriceMapping[i-1])
                minPriceMapping[i] = minPrice
                maxGap = max(maxGap,price-minPrice)
            return maxGap


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
