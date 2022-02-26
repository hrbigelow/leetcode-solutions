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
