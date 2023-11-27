
def maxrun(nums):
    n = len(nums)
    i, j = 0, 0
    alt = None
    maxlen = 0
    # init
    while j != n:
        while j != n and (nums[j] == nums[i] or alt is None):
            if nums[j] != nums[i]:
                if j + 1 < n and nums[j+1] == nums[j]:
                    alt = nums[i]
                else:
                    alt = nums[j]
            j += 1

        maxlen = max(maxlen, j-i)
        while i != j and nums[i] != alt:
            i += 1
        i += 1
        alt = None
    return maxlen


"""
[1, 1, 2, 1, 1]

i   j   alt    maxlen
0   0   -
0   1   -
0   2   2
0   3   2
0   4   2
0   5   2      5
3       -

"""

def main():
    tests = [
            ([1,1,2,1,1], 5),
            ([1,1,2,1,1,3,1,1,1,1], 7),
            ([1], 1),
            ([1,2], 2),
            ([2,1,1,1,1], 5)
            ]

    for inp, out in tests:
        ans = maxrun(inp)
        passed = 'passed' if ans == out else 'failed'
        print(f'{inp=}, {out=}, {passed}')


if __name__ == '__main__':
    main()

