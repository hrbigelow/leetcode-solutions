"""
You are given an integer array prices where prices[i] is the price of a given
stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k
transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).

"""

"""

Another, simpler way to encode this:

account[j][i]:
    the highest account balance after executing j transactions on prices[:i].
    where the transaction is buy, sell, buy, sell, alternating.

account[0][i] = 0 
account[1][0] = -inf
account[1][i] = max(account[1][i-1], -prices[i]) # buy the cheapest available

account[2][i] = max(account[2][i-1], account[1][i-1] + prices[i])

The maximal account value after two transactions over [0, i] timesteps is
achieved by either 1) not making a purchase at time i, in which case your
maximal account value at timestep i-1 is used.  Or, you can take your maximal
account value after one purchase and over [0, i-1], and then make a sale.

account[3][i] = max(account[3][i-1], account[2][i-1] - prices[i])

To maximize your account after three transactions (buy, sell, buy) and over [0,
i], you either stick with your maximal three-transaction account value from [0,
i-1], or you take your maximal two-transaction account value from [0, i-1] and
perform a buy.

In general:

acct[0][i] = 0
acct[j][i] = max(acct[j][i-1], acct[j-1][i-1] + prices[i])  # j even, 
acct[j][i] = max(acct[j][i-1], acct[j-1][i-1] - prices[i])  # j odd

To condense these into just one array, we have:


"""
def maxProfit(self, k: int, prices: List[int]) -> int:
    n = len(prices)
    n_nonoverlapping = n // 2 # max number of non-overlapping buy/sell

    # if you can make as many trades as you want, then the optimal
    # strategy is to include all increasing intervals.  Since a pair
    # of consecutive increasing intervals can be merged into one, the
    # strategy of simply summing consecutive increasing intervals
    # works.
    if k >= n_nonoverlapping:
        return sum(max(0,prices[i] - prices[i-1]) for i in range(1,n))
    
    # acct[j] is the account value after making j transactions
    # (a buy or a sell is a transaction)
    max_buy_sell = min(k, n_nonoverlapping)
    max_transactions = max_buy_sell * 2 # buy or sell

    acct = [0,-float('inf')] * max_buy_sell + [0]
    for price in prices:
        buy = True
        for j in range(1, max_transactions + 1):
            delta = price if buy else -price
            acct[j] = max(acct[j], acct[j-1] + delta)
            buy = not buy
        #print(acct)
    return acct[-1] 
