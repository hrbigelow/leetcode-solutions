"""
The difference is that the 20 ms solution doesn't rely on a prev_digit
assignment.  I'm not exactly sure why the second solution is really faster.

"""
# 44 ms My solution
class Solution:
    def romanToInt(self, s: str) -> int:
        vals = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        total = 0
        prev_digit = 100000
        for c in s:
            digit = vals[c]
            total += digit
            if prev_digit < digit:
                total -= 2 * prev_digit
            prev_digit = digit

        return total


# 20 ms solution 
class Solution:
    def romanToInt(self, s: str) -> int:
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
