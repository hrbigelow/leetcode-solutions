class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start_index = 0
        last_pos1 = 0
        last_pos2 = -1
        max_len = 0
        for i, ch in enumerate(s[1:], start=1):
            max_len = max(max_len, i - start_index)

            if ch == s[last_pos1]:
                last_pos1 = last_pos2
                last_pos2 = i
                
            elif last_pos2 == -1 or ch == s[last_pos2]:
                last_pos2 = i
                
            else:
                start_index = last_pos1 + 1
                last_pos1 = last_pos2
                last_pos2 = i

        max_len = max(max_len, len(s) - start_index)
        
        return max_len
    
"""
13 min:  first draft
20 min:  test  
26 min:  test (after eliminated ch1 and ch2 variables)
30 min:  test (tried to fix initialization condition for last_pos2)
35 min:  finished (after realizing logic error that last_pos1 is not always less than last_pos2)


Some test cases:

Logic error:  I got confused.  It turns out that last_pos1 is not necessarily less than last_pos2.

I failed to uphold the logical assumption that I had made.  Also, last_pos1 and last_pos2 were
poorly named variables.  They should be left/right or something else.


What happens at the end?

When encountering a character not equal to char1 or char2,
start_index = last_char1_pos + 1
last_char1_pos = last_char2_pos
last_char2_pos = i

There's a problem with the initialization.  I would like for the
switchover code to use the same code path as the initialization

If we use just a dummy initialization in which ch1 and ch2 are the same, we will
record the first (spurious) longest substring but it will only contain one character type.

But, that's okay, since it won't be maximal anyway.
"""
