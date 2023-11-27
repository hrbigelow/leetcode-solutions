"""

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a
list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge
between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false
otherwise.

Approach:  perform a single DFS recursion starting at an arbitrary node.
Detect whether there is a cycle
If no cycle, check that the single recursion has visited all nodes.

Care must be taken not to backtrack on the immediate parent of a node since
these are undirected edges and so we need to have two entries in the adjacency list,
which might look like a cycle.

"""
from collections import defaultdict

class Solution:

    white = 0
    gray = 1
    black = 2

    def dfs_visit(self, edge_map, color, parent, node):
        color[node] = self.gray
        for nbor in edge_map[node]:
            if color[nbor] == self.white:
                parent[nbor] = node
                is_tree = self.dfs_visit(edge_map, color, parent, nbor)
                if not is_tree:
                    return False # short circuit
            elif color[nbor] == self.gray:
                if nbor == parent[node]:
                    continue
                return False
            else: # black
                pass
        color[node] = self.black
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edge_map = defaultdict(list)
        for src, trg in edges:
            edge_map[src].append(trg)
            edge_map[trg].append(src)
        
        color = [self.white] * n
        parent = [None] * n

        is_tree = self.dfs_visit(edge_map, color, parent, 0)
        return is_tree and all(color[node] == self.black for node in range(n))


