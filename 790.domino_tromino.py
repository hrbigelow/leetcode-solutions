class Solution:
    from functools import lru_cache
    def numTilings(self, n: int) -> int:
        blunt, overhang, underhang = 0, 1, 2
        modu = 10**9 + 7
        
        @lru_cache
        def rec(col, kind):
            if col == 0:
                return int(kind == blunt)
                
            if col < 0:
                return 0
            
            if kind == blunt:
                return (rec(col-1, blunt) + rec(col-1, overhang) + rec(col-1, underhang) + rec(col-2, blunt)) % modu

            elif kind == overhang:
                return (rec(col-2, blunt) + rec(col-1, underhang)) % modu
            
            elif kind == underhang:
                return (rec(col-2, blunt) + rec(col-1, overhang)) % modu
            
        return rec(n, blunt)
    
    
"""
Took 1.5 hours.  My first consideration was to do bottom-up.  But, this is tricky since
it takes careful planning to know which states to calculate first.  Top-down with caching
avoids all of that, but is not as memory efficient.

We can create these tilings progressively, and represent the end board state by its
furthest occupied column.  Let's call it Overhang, Underhang, or Blunt, and let 

Note that we can disallow the 2-staggered state, since if this occurs, we must place the second
2-tile to fill it, leaving the Both state.

dp[0][Blunt] = 1

What are all the ways?

Blunt -> Blunt  (place 2-tile vertically)
Blunt -> Overhang (place 3-tile top-heavy)
Blunt -> Underhang (place 3-tile bottom-heavy)
Overhang -> Blunt (place 3-tile bottom-heave in reverse)
Overhang -> Underhang (place 2-tile horizontally on bottom)
Underhang -> Blunt (place 3-tile top-heavy in reverse)
Underhang -> Overhang (place 2-tile horizontally on top)

Challenge now is, how to populate the dp array.  Top-down would be easiest.

dp[k][Kind] means number of ways to tile such that at column k (ones-based) we have the Kind pattern.

"""
