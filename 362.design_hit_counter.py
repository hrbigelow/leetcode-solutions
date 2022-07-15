"""
Design a hit counter which counts the number of hits received in the past 5
minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and
you may assume that calls are being made to the system in chronological order
(i.e., timestamp is monotonically increasing). Several hits may arrive roughly
at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.

void hit(int timestamp) Records a hit that happened at timestamp (in seconds).
Several hits may happen at the same timestamp.

int getHits(int timestamp) Returns the number of hits in the past 5 minutes
from timestamp (i.e., the past 300 seconds).
"""

class HitCounter:

    def __init__(self):
        self.hits = []
        
    def _discard(self, expired):
        while self.hits and self.hits[0] <= expired:
            self.hits.pop(0)

    def hit(self, timestamp: int) -> None:
        self._discard(timestamp - 300)
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        self._discard(timestamp - 300)
        return len(self.hits)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

"""
Solved in 8 minutes.  Looking through the other solutions, should use
collections.deque instead of a list
"""
