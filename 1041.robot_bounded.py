"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the
robot never leaves the circle.  

"""

from collections import Counter

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        c = Counter(instructions)
        if abs(c['L'] - c['R']) % 4 != 0: return True
        
        # test whether displacement is zero
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        x, y = 0, 0
        d = 0
        for inst in instructions:
            if inst == 'L':
                d = (d - 1) % 4
            elif inst == 'R':
                d = (d + 1) % 4
            else:
                x += dirs[d][0]
                y += dirs[d][1]
        
        return x == 0 and y == 0
        
    
        
        
"""
Finished in 13 minutes

Quickly deduced that any list which had a net steering would create a loop.
But, with no net steering, needed to compute the total displacement, and if that is zero,
it is bounded as well

"""
