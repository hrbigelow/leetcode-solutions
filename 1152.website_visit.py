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
