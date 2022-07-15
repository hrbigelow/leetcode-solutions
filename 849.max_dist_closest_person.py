"""
You are given an array representing a row of seats where seats[i] = 1
represents a person sitting in the ith seat, and seats[i] = 0 represents that
the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the
closest person to him is maximized.

Return that maximum distance to the closest person.

"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left_dist = [None] * n
        prev_occu = -float('inf')
        for i, occu in enumerate(seats):
            if occu:
                prev_occu = i
            left_dist[i] = i - prev_occu

        max_dist = 0
        prev_occu = float('inf')
        for i in reversed(range(n)):
            if seats[i]:
                prev_occu = i
            dist = min(left_dist[i], prev_occu - i)
            max_dist = max(max_dist, dist)
        
        return max_dist
    
"""
9 min: first draft
11 min: finished


1. compute max distance from left neighbor in forward pass
2. do backward pass virtually, computing min between distance to left and right neighbor

Initialize left_dist[0] = -float('inf') if seats[0] == 0 else 0


"""
