"""
Q2. Given an integer array nums, find the subarray with the largest sum, and return
its sum.

Oh, this is a direct DP solution

Let largest[i] be the largest sum subarray in nums whose last element is nums[i]
Then, the largest is just max(largest)

The recurrence is easy:

largest[i] = max(nums[i], nums[i] + largest[i-1])

also, we can optimize for space by not actually storing largeset but only the largest
element of largest_at_i seen 


"""

def largest_sum_subarray(nums):
    result = -float('inf')
    largest_at_end = -float('inf')
    for num in nums:
        if largest_at_end < 0:
            largest_at_end = num
        else:
            largest_at_end += num
        result = max(result, largest_at_end)

    return result

if __name__ == '__main__':
    tests = [
            [5,-2,8,4,0,1,3,-6,2],
            ]

    for test in tests:
        print(f'{test}: {largest_sum_subarray(test)}')




