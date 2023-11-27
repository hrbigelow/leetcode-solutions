"""
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai,
bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take
course 1.  Return true if you can finish all courses. Otherwise, return false.


this is just a detect-cycles in a graph problem

Do DFS starting from each node.  

This requires the tri-color labeling of nodes:  white, gray, black
See p 546 CLRS middle
"""
from collections import defaultdict
import enum

class Color(enum.Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge_map = defaultdict(list)
        for src, trg in prerequisites:
            edge_map[src].append(trg)

        n = numCourses
        color = [Color.WHITE] * n
        def cyclic(node):
            color[node] = Color.GRAY
            for nbor in edge_map[node]:
                if color[nbor] == Color.GRAY:
                    return True
                elif color[nbor] == Color.WHITE:
                    if cyclic(nbor):
                        return True
            color[node] = Color.BLACK
            return False

        for node in range(n):
            if color[node] == Color.BLACK:
                continue
            if cyclic(node):
                return False
        return True


