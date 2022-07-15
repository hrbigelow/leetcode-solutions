"""
Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are
all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is
stretchy if it can be made to be equal to s by any number of applications of
the following extension operation: choose a group consisting of characters c,
and add some number of characters c to the group so that the size of the group
is three or more.

For example, starting with "hello", we could do an extension on the group "o"
to get "hellooo", but we cannot get "helloo" since the group "oo" has a size
less than three. Also, we could do another extension like "ll" -> "lllll" to
get "helllllooo". If s = "helllllooo", then the query word "hello" would be
stretchy because of these two extension operations: query = "hello" ->
"hellooo" -> "helllllooo" = s.

Return the number of query strings that are stretchy.

"""

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        nt = len(s)
        num_expr = 0
        
        for query in words:
            nq = len(query)
            
            q = 0  # index over query word
            t = 0  # index over s
            
            is_expr = True
            while t != nt and q != nq:

                qs = q # query run start
                ts = t # target run start
                
                if query[qs] != s[ts]:
                    is_expr = False
                    break
                    
                # advance t to next run start
                while t != nt and s[t] == s[ts]:
                    t += 1
                    
                tl = t - ts
                
                # advance q to next run start
                while q != nq and query[q] == query[qs]:
                    q += 1
                    
                ql = q - qs
                
                if ql > tl or (ql < tl and tl < 3):
                    is_expr = False
                    break
                
            num_expr += int(is_expr and t == nt and q == nq)
        
        return num_expr
                        
            
        
        
"""
15 min: first draft
21 min: checking and editing
30 min: forgot to check that all of the input was consumed
32 min: test (not sure what happened)
40 min: finished (my validation logic was flawed.  i didn't check for ql > tl)

At the start of while loop, qs and ts are at the start of a run
At the end, the run is validated (length difference and they are both at the start of the next run
At the end of each iteration of the while loop, the next 'run' in the query and target 
have been consumedm

Checks:

s = "abcd", words = ["abc"]



"""
