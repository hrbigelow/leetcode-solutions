"""
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai,
bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take
course 1.  Return the ordering of courses you should take to finish all courses. If
there are many valid answers, return any of them. If it is impossible to finish all
courses, return an empty array.

This is topological sort.

DFS, and when leaving each node (about to label it black), prepend it to a linked list
of nodes.

If a cycle is detected, return False
"""

import enum
from collections import defaultdict, deque

class Color(enum.Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:

        curriculum = deque()
        color = [Color.WHITE] * n

        edges = defaultdict(list)
        for src, trg in prerequisites:
            edges[trg].append(src)  # flow of edges expresses partial flow of time

        def topo(node):
            # prepend to curriculum
            color[node] = Color.GRAY
            for nbor in edges[node]:
                if color[nbor] == Color.GRAY:
                    return False
                elif color[nbor] == Color.WHITE:
                    if not topo(nbor):
                        return False
            color[node] = Color.BLACK
            curriculum.appendleft(node)
            return True

        for node in range(n):
            if color[node] == Color.BLACK:
                continue
            if not topo(node):
                return []
        return curriculum

