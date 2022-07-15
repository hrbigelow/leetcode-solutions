"""
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:

Split the string into two non-empty substrings at a random index, i.e., if the
string is s, divide it to x and y where s = x + y.

Randomly decide to swap the two substrings or to keep them in the same order.
i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.

Given two strings s1 and s2 of the same length, return true if s2 is a
scrambled string of s1, otherwise, return false.

"""

def isScramble(a: str, b: str) -> bool:
    memo = { }
    def helper(*args):
        if args in memo:
            return memo[args]
        a1, a2, b1, b2 = args
        n = a2 - a1
        if n == 1:
            return a[a1] == b[b1]
        elif a[a1:a2] == b[b1:b2]:
            return True
        else:
            for k in range(1, n):
                if (
                    helper(a1, a1+k, b1, b1+k) and helper(a1+k, a2, b1+k, b2) or
                    helper(a1, a1+k, b2-k, b2) and helper(a1+k, a2, b1, b2-k)
                ):
                    memo[args] = True
                    return True
        memo[args] = False        
        return False

    ans = helper(0, len(a), 0, len(b))
    for k, v in memo.items():
        print('{}: {}'.format(k, v))

    return ans 
