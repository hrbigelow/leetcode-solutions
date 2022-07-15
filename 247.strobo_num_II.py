"""
Given an integer n, return all the strobogrammatic numbers that are of length
n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).
"""

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        results = []
        def extend_strobo(seed, remain):
            if remain == 0:
                if seed[0] != '0' or len(seed) == 1:
                    results.append(seed)
            elif remain % 2 == 1:
                for singlet in '018':
                    extend_strobo(singlet, remain - 1)
            else:
                for left, right in [('0', '0'), ('1', '1'), ('6', '9'), ('9', '6'), ('8', '8')]:
                    extend_strobo(left + seed + right, remain - 2)

        extend_strobo('', n)
        return results
        
"""
20 min: first draft
23 min: test (forgot to filter out numbers with leading zeros)
24 min: finished


I believe I've done this before.  Only five digits: 0, 1, 6, 8, 9 are rotatable.  So, the total possible number of them
would be 5**14, or 6 billion.

So, one option is just count up from '0' * n to '9' * n.  Any others?

Could simply construct each by adding a pair of digits to either side

Base cases are the empty string, or a single digit of 0, 1, or 8.

Then, you can construct it recursively by adding a compatible pair:

0 0
1 1
6 9
9 6
8 8



"""
