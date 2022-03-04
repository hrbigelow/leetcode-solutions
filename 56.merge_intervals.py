class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals, key=lambda i: i[0])
        cur_ival = intervals[0]
        
        for ival in intervals:
            if cur_ival[1] >= ival[0]: # overlaps
                cur_ival[1] = max(cur_ival[1], ival[1])
            else:
                result.append(cur_ival)
                cur_ival = ival.copy()

        result.append(cur_ival)
        
        return result
    
            
        
        
"""
6 min: first draft
9 min: finished

No issues

1. sort by start position
"""
