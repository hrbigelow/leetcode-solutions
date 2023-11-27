"""
Approach:

Traditional DFS, returning depth (or inf if cycle detected)

"""

class Solution:
    todo = 0
    pend = 1
    done = 2

    def dfs_visit(self, edge_list, status, depths, node):
        depth = 1
        status[node] = self.pend
        for next_node in edge_list[node]:
            if status[next_node] == self.todo:
                self.dfs_visit(edge_list, status, depths, next_node)
            elif status[next_node] == self.pend:
                depth = float('inf')
            else: # done
                pass
            depth = max(depth, depths[next_node] + 1)
        status[node] = self.done
        depths[node] = depth

    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        edge_list = collections.defaultdict(list)
        for prev_course, next_course in relations:
            edge_list[next_course - 1].append(prev_course - 1)
        
        status = [self.todo] * n
        depths = [0] * n
        for node in range(n):
            if status[node] == self.todo:
                self.dfs_visit(edge_list, status, depths, node)
        
        max_depth = max(depths)
        if max_depth == float('inf'):
            return -1
        return max_depth

