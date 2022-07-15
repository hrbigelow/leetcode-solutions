"""
Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).

"""

class PointDist():
    def __init__(self, idx, x, y):
        self.idx = idx
        self.dist = math.sqrt(x**2 + y**2)
    
    def __lt__(self, other):
        return self.dist > other.dist

    def __repr__(self):
        return f'{self.idx}, {self.dist:3.2f}'
    
import heapq as hq
    
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [PointDist(i, x, y) for i, (x, y) in enumerate(points[:k])]
        hq.heapify(h)
        
        for i in range(k, len(points)):
            x, y = points[i]
            if abs(x) > h[0].dist or abs(y) > h[0].dist:
                continue
            p = PointDist(i, x, y)
            if p.dist < h[0].dist:
                hq.heapreplace(h, p)
        
        print(h)
        return [points[pd.idx] for pd in h]
    
"""
I knew the solution but it took a little fiddling.  Counterintuitively,
since we want to find the k smallest quantities, we need to maintain a *max*
heap, replacing the max every time a smaller item is found.
"""
