class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rs = [0]
        for e in nums:
            rs.append(rs[-1] + e)
        
        ct = Counter(rs)
        tot = 0
        for s in rs:
            ct[s] -= 1
            tot += ct[k + s]

        return tot
    
"""
First we compute the running sum rs[i] = sum(nums[:i]) (note this is an n+1 length array)
Then, compute the number of occurrences of each value of the running sum.

At each iteration, we want to (virtually) compute the new counts for the running sums starting
at the next position.  This is going to be the same, except that the keys will be different by
the value s.  Also, the number of occurrences of s is deducted by 1 since it is excluded.

"""
