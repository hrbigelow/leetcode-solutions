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
