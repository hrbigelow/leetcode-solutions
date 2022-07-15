"""
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.

"""

"""
Given a set of prices of a stock, return the maximum possible profit
you can make by one buy/sell transaction.

Approach:



"""

def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0
    minval = prices[0]
    max_profit = 0
    for i in range(1, n):
        max_profit = max(max_profit, prices[i] - minval)
        minval = min(minval, prices[i])
    return max_profit


    buy = float('-inf')
    sell = 0
    for p in prices
