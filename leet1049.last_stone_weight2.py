"""
Approach:

Note that any sequence of smashings, eg of stones a,b,c,d,e has a residual weight
expression:

(d-(a-(b-c)))-e
d-((b-e)-(a-c))
c-((b-d)-e)

Note that, by the associative property, each of these expressions simplifies to
a sum of the weights, in which one or more of the signs is flipped.

Each smashing between a pair of stones involves one sign flip, followed by a
sum.  The result of that smashing, however, may have its sign flipped before
being smashed with another stone.  When that happens, the stone in question has
had its sign flipped twice.

With n stones, the first smashing incurs one sign flip on one stone.

For example, consider the stones: a b c

smash 2:  a - (b - c)  => +a -b +c
          (b - c) - a  => -a +b -c
          
Each smash either flips the sign of one primary stone to negative, or flips the
result of a previous smash to negative, which implies reverting one of the
smashed stones signs, and flipping the other one to negative.

What we want to prove is that any combination of signs with at least one
negative, is possible to generate with the right choice of smashing order.

There are n-1 smashings.  Each smashing either flips one stone to negative, or
reverts one to positive and and flips another to negative.

For n even, we can imagine a minimally nested grouping as follows:

((a-b) - (c-d)) - ((e-f) - (g-h)) => a -b -c +d -e +f +g -h   4 flips

A maximally nested grouping:

a - (b - (c - (d - (e - (f - (g-h))))))  => a -b +c -d +e -f +g -h  4 flips

Another maximally nested grouping:

(((((((a - b) - c) - d) - e) - f) -g) -h) => a -b -c -d -e -f -h  7 flips


So, what this says is that we are partitioning the set of stones into POS and
NEG sets, where their intersection is zero, and POS U NEG = all stones.  final
answer = sum(POS) - sum(NEG)

sum(POS) = sum(ALL) - sum(NEG)

so, final answer is:

sum(ALL) - 2 * sum(NEG)

"""

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        achievable = {0}
        low_half = total // 2
        high_half = total - low_half
        dp = [True] + [False] * total
        for w in stones:
            for i in reversed(range(w, low_half + 1)):
                dp[i] |= dp[i-w]
                
        for i in reversed(range(high_half + 1)):
            if dp[i]:
                largest_neg_sum = i
                break
        pos_sum = total - largest_neg_sum
        remain = pos_sum - largest_neg_sum
        return remain
            
        
