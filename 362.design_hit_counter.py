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
