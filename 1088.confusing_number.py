class Solution:
    def confusingNumberII(self, n: int) -> int:
        def rotate(num):
            return int(str(num)[::-1].replace('6', 't').replace('9', '6').replace('t', '9'))

        def dfs(num):
            if num > n:
                return 0
            ans = 0
            if num != rotate(num):
                ans += 1
            for d in [0, 1, 6, 8, 9]:
                ans += dfs(num * 10 + d)
            return ans

        return sum(dfs(i) for i in [1, 6, 8, 9])


""" I could not solve this in 40 minutes and just gave up.  I was looking for a
non-brute-force solution and thought about breaking up the range [1, n] into
sub-ranges with 1, 2, log(n) digits and adding the result.

However, the left-over portion of numbers was prohibitively complicated to
evaluated formulaically.

But, what seems like the "brute force" solution, note that only 5 digits
are considered when counting up to n.  So, the number of such numbers is

5 ^ log_10(n) = 5 ^ log_5(log_2(n)) = log_2(n)
"""
