"""
This is a confusing one.

How about iteratively?

It can be done as BFS.  The virtual tree is an n-length path.  The root has
n branches, and at each level there is one less branch.  

"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from collections import deque
        n = len(nums)
        results = []
        d = deque([[]])
        while d:
            pre = d.popleft()
            if len(pre) == n:
                results.append([nums[i] for i in pre])
                continue
                
            for i in range(n):
                if i in pre:
                    continue
                d.append(pre + [i])

        return results

"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)
        
        # sel contains i-1 selections in order
        # explore all possible permutations starting with
        # the sel sequence
        def perm_rec(i, sel):
            if i == n:
                results.append([nums[s] for s in sel])
                return
            
            sel.append(-1)
            for s in range(n):
                if s in sel:
                    continue
                sel[-1] = s
                perm_rec(i+1, sel)
            sel.pop()

        perm_rec(0, [])
        return results
"""
