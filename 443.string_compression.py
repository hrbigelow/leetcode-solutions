class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        wp = 0 # write-pointer
        rs = 0 # run-start
        
        for i in range(n):
            if i ==  n - 1 or chars[i] != chars[i+1]:
                chars[wp] = chars[i]
                wp += 1
                rl = i - rs + 1 # runlength
                if rl > 1:
                    q = str(rl)
                    chars[wp:wp+len(q)] = q
                    wp += len(q)
                
                rs = i + 1
        
        return wp
    
"""
I had one failed attempt after 2 hours.  The next day,
I realized there was a cleaner approach.  There were two insights.
The first was that I could use the character at the *end* of a run of same characters
as the one to write into the new place.  This is much more convenient than using the character
at the beginning, because the moment you want to write it is the moment you reach the end of the run.

Secondly, there were two main approaches with indexing.  In one, you do the writing when i reaches the
beginning of a run.  But this means you need a special case to summarize the last run, and also a special 'empty' case
at the beginning of the main loop.

If instead you do the writing at the end of a run, you have the information you need at hand.  The only awkward thing is that
the test for 'end of run' needs to peek ahead one position, and if at the end, do a test for the end.
"""

