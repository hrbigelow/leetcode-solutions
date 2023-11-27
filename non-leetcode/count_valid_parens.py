"""
Return the total number of valid parentheses strings of length 2n
that could be formed

T1 = 1  # ()
T2 = 2  # T1.T1 or Wrap(T1)
T3 = ?  # T1.T2 or T2.T1 or Wrap(T2)

The problem is the double-counting

T1.T1.T1 will be counted twice in the T3 formula





"""

def count_parens(n):
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]

    return dp[n]


