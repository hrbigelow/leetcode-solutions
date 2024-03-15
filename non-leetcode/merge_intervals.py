"""
Q1. Given a collection of intervals, merge all overlapping intervals.

Input:  [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""

def merge_intervals(ivals):
    ivals = sorted(ivals)
    merged = []
    for ival in ivals:
        if merged and merged[-1][1] >= ival[0]:
            merged[-1][1] = max(merged[-1][1], ival[1])
        else:
            merged.append(ival)
    return merged

tests = [
        [[1,3],[2,6],[8,10],[15,18]]
        ]

if __name__ == '__main__':
    for test in tests:
        print(f'{test}: {merge_intervals(test)}')

   
