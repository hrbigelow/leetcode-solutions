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
