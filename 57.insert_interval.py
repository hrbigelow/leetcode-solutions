class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []
        i = 0
        while i != len(intervals):
            ival = intervals[i]
            if ival[1] < newInterval[0]:
                results.append(ival) # pass through
              
            elif ival[0] <= newInterval[1]: # overlap
                newInterval[0] = min(newInterval[0], ival[0])
                newInterval[1] = max(newInterval[1], ival[1])
            
            else:
                break
            i += 1
            
        results.append(newInterval)
        results.extend(intervals[i:])
        
        return results
        
"""
10 min: first draft
13 min: finished

no issues


"""
