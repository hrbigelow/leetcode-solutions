"""
Q1. Given an array of integers, return boolean true/false whether the array is
monotonic (either it never increases or it never decreases).

Examples if needed:

// True: [1, 2, 3, 4, 5, 6]
// True:  [1, 2, 5, 5, 8]
// True:  [9, 4, 4, 2]
// False: [1, 4, 6, 3]



"""

def is_monotonic(nums):
    pre = nums[0]
    maybe_up, maybe_down = True, True
    # a horizontal is compatible with both
    for num in nums:
        if pre < num:
            if not maybe_up:
                return False
            maybe_down = False
        elif pre == num:
            continue
        else:
            if not maybe_down:
                return False
            maybe_up = False
        pre = num
    return True


tests = [
    ([1, 2, 3, 4, 5, 6], True),
    ([1, 2, 5, 5, 8], True),
    ([9, 4, 4, 2], True),
    ([1, 4, 6, 3], False)
    ]

if __name__ == '__main__':
    for input, expected in tests:
        result = is_monotonic(input)
        print(f'{input}: correct? {expected==result}')


