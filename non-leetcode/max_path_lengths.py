"""
From interviewing.io The Grey Dictaphone

https://start.interviewing.io/interview/QhtikYCB0XMo/replay

Given a directed graph with n nodes, 0,n-1, find the length of the longest path from
ALL nodes 


This is DFS, modified to return current height and store in a global array



"""
from collections import defaultdict

white, gray, black = 0, 1, 2

def dfs(num_vertices, edge_list):
    color = [white] * num_vertices
    edges = defaultdict(list)
    depth = [0] * num_vertices

    for src, trg in edge_list:
        edges[src].append(trg)

    for node in range(num_vertices):
        if color[node] == white:
            dfs_visit(color, depth, edges, node)

    return depth

def dfs_visit(color, depth, edges, node):
    color[node] = gray
    for nbor in edges[node]:
        if color[nbor] == white:
            dfs_visit(color, depth, edges, nbor)
        elif color[nbor] == gray:      # special logic: cycle detection
            depth[node] = float('inf')
        else:  # black
            pass
        depth[node] = max(depth[node], depth[nbor] + 1)  # special logic: depth calc 
    color[node] = black

tests = [
        (5, [[0,1], [1,2], [2,3], [4,3]]),
        (5, [[0,1], [1,2], [3,2], [4,3]]),
        (5, [[0,1], [1,2], [3,4], [4,3]])
        ]

if __name__ == '__main__':
    for nv, edges in tests: 
        ans = dfs(nv, edges)
        print(f'{nv=}, {edges=}, {ans=}')




