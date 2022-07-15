"""
You are given an array prices where prices[i] is the price of a given stock on
the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions
as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).

"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pre_hold, pre_free = -float('inf'), 0
        for p in prices:
            hold = max(pre_hold, pre_free - p)
            free = max(pre_free, pre_hold + p - fee)
            pre_hold, pre_free = hold, free
        
        return free
            
"""
Finished in 4 minutes, correct on the first try!
This is the same case, with states hold and free.  The recurrence requires paying the fee.
"""
