"""
Q2. Given an array of distinct ints, return True if any of the 3 elements add up to
zero, False otherwise.  

nums = [3, 8, -11]  => return True

Can we do it without sorting?

With sorting, one can do a nested i,j loop where i<j<n-1, and then step k back until
you find one.

Without sorting, some form of hashing would be required.



"""
from bisect import bisect_left

def three_zero_sum(ary):
    ary = sorted(ary)
    n = len(ary)
    if n < 3:
        return False

    for i in range(n-2):
        for j in range(n-1):
            target = - ary[i] - ary[j]
            idx = bisect_left(ary, target)
            if j+1 <= idx < n and ary[idx] == target:
                return True
    return False


tests = [
        [-3, 0, 3],
        [-4, 0, 1, 3],
        [-5, -2, 2, 8]
        ]

if __name__ == '__main__':
    for test in tests:
        print(f'{test}: {three_zero_sum(test)}')

             

