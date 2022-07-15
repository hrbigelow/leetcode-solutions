"""
Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.

"""

"""
The insight into this to notice the commutativity of the bitwise xor operation:

a ^ b = b ^ a

So, for each bit position in an integer representation of an integer, if we
start with zero, then do xor with some integer, we get that integer.  If we
then do another xor with the same integer, we get zero again.  And, if we have
any collection of 1s and 0s, in which the number of 1s is even and the number
of 0s is even, because of commutation, we can express it as:

(1 ^ 1) ^ (1 ^ 1) ... ^ (0 ^ 0) ^ (0 ^ 0)

with:

0 ^ 0 = 0
1 ^ 1 = 0

This expression represents the collection of all pairs of numbers in the set.
The final, single number will appear as a lone 0 or a lone 1 in that
expression.

Thus, the final rule will give:

p : result of paired bitwise operation (= 0)
s : bit of the singleton number
p ^ s = s

in every position

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
