"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left). Each
asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids
meet, the smaller one will explode. If both are the same size, both will
explode. Two asteroids moving in the same direction will never meet.

"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        
        for ast in asteroids:
            # ast is moving forward, no collisions
            if ast > 0:
                st.append(ast)
                continue

            # ast is moving backward.  destroy all backward smaller asteroids
            while st and 0 < st[-1] < -ast:
                st.pop()

            # the left neighbor of ast either doesn't exist or is equal or greater
            if st and st[-1] == -ast:
                # exists and is equal - mutual anihilation
                st.pop()
            
            elif not st or st[-1] < 0:
                # doesn't exist, or is moving left - no collision
                st.append(ast)
                
        return st
        
"""
Solved in 32 minutes.  The tricky thing was keeping track of all branch options.
In general I have a problem with 1) recognizing when there is a danger that I'll lose track
of the mutually exclusive branch options, and 2) when I do recognize it, I panic instead of
writing out the options.

"""
