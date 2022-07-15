class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        
        while i != -1 and carry:
            carry, d = divmod(digits[i] + carry, 10)
            digits[i] = d
            i -= 1
        
        if i == -1 and carry:
            digits.insert(0, carry)
            
        return digits
        
        
"""
Finished in 9 minutes.  Four attempts

At the start, ever element is in [0, 9].  Then, iterate:

add 1, then decompose the result into carry, and digit
if carry is non-zero, repeat the process on the next digit
if i == 0, pre-pend carry to the array

"""
