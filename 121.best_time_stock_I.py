class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we must start in a state of 'not holding', so both of these
        # states are disallowed
        pre_hold, pre_done = -float('inf'), -float('inf')
        profit = 0
        
        for p in prices:
            hold = max(pre_hold, - p)
            done = max(pre_done, pre_hold + p)
            profit = max(profit, done)
            pre_hold, pre_done = hold, done
            
        return profit
        
"""
The DP state is H = {holding, not holding, done} and D = {0, 1, 2, ..., n}

The start state is:

not holding


The transitions can be:

not holding -> not holding
not holding -> holding  ('buy')
holding -> holding
holding -> done   ('sell')
done -> done


"""
