"""
309. 最佳买卖股票时机含冷冻期
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""
from typing import List

"""
动态规划
"""


def maxProfit(prices: List[int]) -> int:
    l = len(prices)
    if not prices:
        return 0
    if l == 1:
        return 0
    dp = [[-prices[0], 0, 0]]
    for i in range(1, l):
        r1 = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        r2 = max(dp[i - 1][1], dp[i - 1][2])
        r3 = dp[i - 1][0] + prices[i]
        dp.append([r1, r2, r3])

    return max(dp[l - 1][0], dp[l - 1][1], dp[l - 1][2])


def maxProfit_1(prices: List[int]) -> int:
    if not prices:
        return 0
    empty, empty_freeze, hold = 0, 0, -prices[0]

    for i in range(len(prices)):
        empty, empty_freeze, hold = max(empty, empty_freeze), hold + prices[i], max(empty-prices[i], hold)
    return max(empty, empty_freeze, hold)


print(maxProfit_1([1, 2, 3, 0, 2]))
