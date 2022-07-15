"""
Given an array of meeting time intervals intervals where intervals[i] =
[starti, endi], return the minimum number of conference rooms required.

"""
class Solution:
    import heapq
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda i: i[0])
        
        ends = []
        for b, e in intervals:
            # meeting starts before the earliest availability of any scheduled room
            if not ends or ends[0] > b:
                heapq.heappush(ends, e)
            else:
                heapq.heapreplace(ends, e)

        return len(ends)
        
"""
21 min: finished

Got really lucky, on a hunch, this idea worked

"""
