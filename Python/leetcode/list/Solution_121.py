from typing import List


def maxProfit( prices: List[int]) -> int:
    minprice = float('inf')
    print(minprice)
    maxprofit = 0
    for price in prices:
        minprice = min(minprice, price)
        maxprofit = max(maxprofit, price - minprice)
    return maxprofit


print(maxProfit([7,1,5,3,6,4]))