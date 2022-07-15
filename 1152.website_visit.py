"""
 You are given two string arrays username and website and an integer array
 timestamp. All the given arrays are of the same length and the tuple
 [username[i], website[i], timestamp[i]] indicates that the user username[i]
 visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and
["luffy", "luffy", "luffy"] are all patterns.  The score of a pattern is the
number of users that visited all the websites in the pattern in the same order
they appeared in the pattern.

For example, if the pattern is ["home", "away", "love"], the score is the
number of users x such that x visited "home" then visited "away" and visited
"love" after that.  Similarly, if the pattern is ["leetcode", "love",
"leetcode"], the score is the number of users x such that x visited "leetcode"
then visited "love" and visited "leetcode" one more time after that.
Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of
users x such that x visited "luffy" three different times at different
timestamps.  Return the pattern with the largest score. If there is more than
one pattern with the same largest score, return the lexicographically smallest
such pattern.

"""
class Solution:
    from collections import defaultdict
    
    def mostVisitedPattern(self, user: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        uw = [(u, w) for u, _, w in sorted(zip(user, timestamp, website), key=lambda triple: triple[1])]
        u = [u for u, _ in uw]
        w = [w for _, w in uw]
        
        n = len(uw)
        d = defaultdict(set)
        
        for l in range(n-2):
            ul = u[l]
            for m in range(l+1, n-1):
                um = u[m]
                for r in range(m+1, n):
                    if ul == um and um == u[r]:
                        d[(w[l], w[m], w[r])].add(ul)
        
        max_ct = max(len(s) for s in d.values())
        return min(list(k) for k, v in d.items() if len(v) == max_ct)
        
        
"""
Alright, what are some brute force solutions?

1. Do a triple-nested loop over the 50 positions.  Maintain a dictionary with triplets whose value is the set of
   users who have exhibited that pattern.  After that, sort the dictionary in reverse by set size, then by
   lexicographical order of the triplet.

Took 52 minutes.  I looked for awhile for a non-brute force solution but couldn't find one.
I made some error in forgetting to take the length of the user set.

"""
