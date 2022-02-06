class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        diffs = [g - c for g, c in zip(gas, cost)]
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += diffs[i]
            curr_tank += diffs[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0
        
        return starting_station if total_tank >= 0 else -1

"""
The key idea here is to think of finding a starting point in diffs such that the
running sum (with wraparound) never goes below zero.

One can segment the diffs array into a sequence of 'hills' (a segment of positive numbers followed by a 
run of negative numbers.)  The key fact is that, if any position besides the start of the hill is a valid
solution, then the start of the hill is a valid solution.  Therefore one only need consider these hill starts
as valid solutions.

A hill is either net positive or net negative, therefore one can collapse each of these hills into its
net value.  But, this collapsing yields a smaller yet identical problem, one of 'hills of hills'.  A hill of
hills is a run of net-positive hills followed by net negative hills.

In the function above, if starting_station is on a downslope of a hill, it automatically gets bumped forward.
Any run in which starting_station stays constant will be with it at the start of a hill.  And, if it
successfully completes that hill, it will remain for the next hill.  This means the first hill was net positive,
and can be regarded as the up-slope of a hill-of-hill.
"""
