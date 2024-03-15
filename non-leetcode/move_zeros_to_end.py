"""
Q1. Given an array of ints, move all nonzeros to the front of the array. Do it in
place. Return the number of nonzero elements.  

nums = [1, 0, 2, 0, 3, 4]

Analysis:

Let p = number of nonzero elements in the array

1. Clearly, after the loop, the first p elements consist of the non-zero elements
in-order.  This is because next_write is only ever incremented after a write of
ary[i].  And ary[i] is always non-zero, and next_write is then incremented after the
write.

What's less obvious is why should we assign ary[i] to zero?  This ensures that there
is a conservation of values.  By only performing swaps, we ensure that the total
content of the array doesn't change.  So, by process of elimination, we can reason
that the remaining part of the array is all zeros.

"""

def compact_array(ary):
    next_write = 0
    for i in range(len(ary)):
        if ary[i] != 0:
            ary[next_write], ary[i] = ary[i], ary[next_write]
            next_write += 1
    return next_write

