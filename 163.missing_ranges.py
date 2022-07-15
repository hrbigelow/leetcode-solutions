"""
You are given an inclusive range [lower, upper] and a sorted unique integer
array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is
not in nums.

Return the smallest sorted list of ranges that cover every missing number
exactly. That is, no element of nums is in any of the ranges, and each missing
number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        results = []
        augmented = [lower-1] + nums + [upper+1]
        n = len(augmented)
        
        for i in range(1, n):
            beg = augmented[i-1] + 1
            end = augmented[i] - 1
            if beg == end:
                results.append(str(beg))
            elif beg < end:
                results.append(str(beg) + '->' + str(end))
        
        return results
        
"""
8 min  first draft
10 min finished

Ranges between two elements nums[i] and nums[j] are just:

beg = nums[i] + 1
end = nums[i+1] - 1

if beg == end:
    output beg
elif beg < end:
    output "beg->end"
else:
    nothing
    
the last range is as if you appended upper+1 to the array
the first range is as if you pre-pended lower-1 to the array



"""
