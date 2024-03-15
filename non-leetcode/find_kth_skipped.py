"""
Q2. Given an array of an increasing integer sequence,
find the Kth number in the missing sequence between these integers.
Input: [2,4,7,8,9,13] -> missing number sequence is [3,5,6,10,11,12]
K = 2

Output: 5
Since 5 is the 2nd number in that missing sequence


1. keep track of num skipped
2. if num_skipped exceeds k, then it is in the last interval

Notice that, after updating num_skipped, num-1 is the `num_skipped'th number, and the
ones before that are consecutive.



"""

def find_kth(nums, k):
    assert k > 0 # problem doesn't make sense if there are no numbers skipped
    prev = nums[0] - 1 
    num_skipped = 0
    for num in nums + [nums[-1] + k + 1]:
        num_skipped += num - prev - 1
        if num_skipped >= k:
            return num - (num_skipped - k) - 1
        prev = num



tests = [
        ([2,4,7,8,9,13], 2),
        ([2,3,4,5,6,8,10,15], 4),
        ([2,3,4,5,6,8,10,15], 7),
        ]

if __name__ == '__main__':
    for nums, k in tests:
        print(f'{nums}, {k}: {find_kth(nums, k)}')





    

