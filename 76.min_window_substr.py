class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        budget = Counter(t)
        
        i, j = 0, 1
        if s[i] in budget:
            budget[s[i]] -= 1
            
        min_i, min_j, min_len = -1, -1, n + 1

        while True:
            # moving i forward
            while all(v <= 0 for v in budget.values()):
                if j - i < min_len:
                    min_i, min_j, min_len = i, j, j - i
                    
                if s[i] in budget:
                    budget[s[i]] += 1
                i += 1
            
            if j == n:
                break
                    
            while j != n and any(v > 0 for v in budget.values()):
                if s[j] in budget:
                    budget[s[j]] -= 1
                j += 1
            
        return s[min_i:min_j]
                
            

"""
Solved in 23 minutes.  Four attempts.  Logic was sound.
"""


