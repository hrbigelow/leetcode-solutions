from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.times = defaultdict(lambda: [0, 0]) # (beg, end) => (tot, ct)
        self.starts = defaultdict(lambda: {}) # (id, beg) => time
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.starts[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, begTime = self.starts.pop(id)
        
        trip = (startStation, stationName)
        self.times[trip][0] += t - begTime
        self.times[trip][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, num_trips = self.times[(startStation, endStation)]
        return total_time / num_trips

    
