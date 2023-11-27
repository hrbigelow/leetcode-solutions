"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array
edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to
node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable.
It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

"""

class Solution:

    todo, pending, done = 0, 1, 2

    def dfs_visit(self, edge_map, status, parents, node):
        status[node] = self.pending
        for next_node in edge_map[node]:
            if status[next_node] == self.todo:
                parents[next_node] = node
                self.dfs_visit(edge_map, status, parents, next_node)
            elif status[next_node] == self.pending:
                assert False, 'you said it was acyclic'
            else: # done
                if parents[next_node] is None:
                    parents[next_node] = node
                pass
        status[node] = self.done

    def find_root(self, parents, node):
        while parents[node] is not None:
            node = parents[node]
        return node

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        parents = [None] * n
        status = [self.todo] * n
        edge_map = collections.defaultdict(list)
        for src, trg in edges:
            edge_map[src].append(trg)
        
        for node in range(n):
            if status[node] == self.todo:
                self.dfs_visit(edge_map, status, parents, node)
        
        return list(set(self.find_root(parents, node) for node in range(n)))




