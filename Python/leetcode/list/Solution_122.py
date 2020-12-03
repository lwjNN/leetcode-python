from typing import List


def maxProfit_dp(prices: List[int]) -> int:
    dp = [[0, -prices[0]]]
    for i in range(1, len(prices)):
        res = []
        res.append(max(dp[i - 1][1] + prices[i], dp[i - 1][0]))
        res.append(max(dp[i - 1][0] - prices[i], dp[i - 1][1]))
        dp.append(res)
    return dp[len(prices) - 1][0]


def maxProfit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0

    profit = 0
    for i in range(1, len(prices)):
        if (prices[i] - prices[i - 1] > 0):
            profit += prices[i] - prices[i - 1]
    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 4, 5]))
