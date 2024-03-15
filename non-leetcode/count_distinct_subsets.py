"""
- you have a set of items A with n unique integer values and a number S, n < 40,
  write an algorithm that counts how many distinct subsets of A have sum S 

A = [2,8,40,35,62,9]
S = 25

Count how many distinct subsets of A have sum S

First sort A
Then, recursively count

Since they are increasing, if A[i] > S then you're done

choice is to either use or don't use it.  This seems like DP

A
dp[i][s] := number of distinct subsets of A[:i] summing to s
dp[0][0] = 1 # there is one subset (the empty set) summing to 0
dp[i][s] = dp[i-1][s-nums[i]] + dp[i-1][s]

dp[i][s+nums[i]] = dp[i-1][s]

dp[s] = pre[s-num] + pre[s]

idea is you can either use or not use the current value

So, in the worst case, there are 2^n different sums

Actually, what I can do is to divide these into a partition of values

No, this won't work because you need to 




"""

def count_aux(A, S):
    # Assume elements in A are non-negative and distinct
    dp = [0] * (S+1) # number of distinct subsets
    for num in A: # O(n * k)

        pre = dict(dp)
        dp = { num + v: c for v, c in pre.items() if num + v <= S }
        for s in pre:
            if s not in dp:
                dp[s] = 0
            dp[s] += pre[s]
    return dp

def count_distinct_subsets(A, S):
    apos = [ num for num in A if num >= 0 ]
    aneg = [ -num for num in A if num < 0 ]
    counts_pos = count_aux(apos)
    counts_neg = count_aux(aneg)



A = [1,2,3,4,5,6]
S = 2

for S in range(22):
    print(f'{S}: {count_distinct_subsets(A, S)}')


            


