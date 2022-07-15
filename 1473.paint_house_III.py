"""

There is a row of m houses in a small city, each house must be painted with one
of the n colors (labeled from 1 to n), some houses that have been painted last
summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with
the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2},
{3,3}, {2}, {1,1}].  Given an array houses, an m x n matrix cost and an integer
target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.

cost[i][j]: is the cost of paint the house i with the color j + 1.

Return the minimum cost of painting all the remaining houses in such a way that
there are exactly target neighborhoods. If it is not possible, return -1.

"""

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        pre = [[0] + [float('inf')] * (target-1) for _ in range(n)]
        dp = [p.copy() for p in pre]
        
        for i, color, prices in zip(range(m), houses, cost):
            for j in range(n):
                # the max neighborhood can be only i (zero-based)
                for k in range(min(i+1, target)):
                    if color == 0 or j == color-1:
                        labor = prices[j] if color == 0 else 0
                        
                        same_cost = pre[j][k]
                        if k > 0:
                            new_cost = min(pre[_j][k-1] for _j in range(n) if _j != j)
                        else:
                            new_cost = float('inf')
                            
                        dp[j][k] = min(same_cost, new_cost) + labor
                    else:
                        dp[j][k] = float('inf')
            # print(dp)

            for j in range(n):
                for k in range(min(i+1, target)):
                    pre[j][k] = dp[j][k]
            
        ret = min(p[-1] for p in pre)
        return ret if isinstance(ret, int) else -1

"""
Assume i, j, and k are all zero-based

dp[i][j][k]: minimum cost to paint house i color j, such that house i is in the k-th neighborhood
i: house number      (m houses)
j: color  (total n colors)
k: number of neighborhoods  (exactly target neighborhoods at the end)

dp[j][k] should be the min between either changing hoods from previous hood, or same hood

same_hood:  dp[j][k] = pre[j][k]

This was really hard.

Mistakes made:

1. Initialization problems in which pre[*][>0] should be inf, but was zero instead
2. Adding prices[_j] instead of prices[j]
3. Misreading the problem, mistakenly tallying the price for an already-painted house
4. Forgetting to convert the inf to -1 at the end


"""
