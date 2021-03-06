"""
You are given an array of variable pairs equations and an array of real numbers
values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai /
Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth
query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined,
return -1.0.

Note: The input is always valid. You may assume that evaluating the queries
will not result in division by zero and that there is no contradiction.
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # create adjacency list
        adj_list = {}
        for (beg, end), quot in zip(equations, values):
            if beg not in adj_list:
                adj_list[beg] = {}
            adj_list[beg][end] = quot
            
            if end not in adj_list:
                adj_list[end] = {}
            adj_list[end][beg] = 1.0 / quot
            
        # for each query, do bfs
        from collections import deque
        results = []
        dq = deque()
        visited = set()
        
        for src, trg in queries:
            if src not in adj_list:
                results.append(-1)
                continue
                
            dq.append((src, 1.0))
            visited.add(src)
            ans = -1
            
            while dq:
                node, full_quot = dq.popleft()
                if node == trg:
                    ans = full_quot
                    break
                    
                for nxt_node, quot in adj_list[node].items():
                    if nxt_node in visited:
                        continue
                    dq.append((nxt_node, full_quot * quot))
                    visited.add(nxt_node)
            
            results.append(ans)            
            visited.clear()
            dq.clear()

        return results
    
        
"""
12 min: first draft
19 min: finished

No real issues - the proofreading caught a few mistakes.  One final mistake I overlook
was dealing with variables not mentioned in the equations.

Graph with directed edges labeled as quotients.  We are given path queries.
Could do bfs for each starting node in the query.

adj_list[node][target] = quotient


"""
