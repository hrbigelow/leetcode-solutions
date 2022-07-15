"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit
signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or
'+'. Read this character in if it is either. This determines if the final
result is negative or positive respectively. Assume the result is positive if
neither is present.
Read in next the characters until the next non-digit character or the end of
the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no
digits were read, then the integer is 0. Change the sign as necessary (from
step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then
clamp the integer so that it remains in the range. Specifically, integers less
than -231 should be clamped to -231, and integers greater than 231 - 1 should
be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of
the string after the digits.

"""

"""
The winning submissions 


"""
# 28 ms
class Solution:
    def myAtoi(self, str: str) -> int:
        n = len(str)
        if n == 0:
            return 0
        
        # eat up whitespace
        for i in range(n):
            if str[i] != ' ':
                break
        else:
            return 0

        # parse possible sign
        sign = 1
        if str[i] in ('+', '-'):
            if str[i] == '-':
                sign = -1
            i += 1

        # loop only executes for digits
        pos_val = 0
        while i != n and str[i] >= '0' and str[i] <= '9':
            pos_val = pos_val * 10 + int(str[i])
            i += 1

        int_max = 2**31 - 1
        int_min = -2**31
        
        val = sign * pos_val
        
        return max(int_min, min(int_max, val))

# 16 ms
class Solution:

    def myAtoi(self, str: str) -> int:
        ls = list(str.strip())
        if len(ls) == 0:
            return 0
        if len(str) == 0:
            return 0

        sign = -1 if ls[0] == "-" else 1
        if ls[0] in ['-', '+']:
            del ls[0]

        ret = 0
        i = 0

        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1

        return max(-2**31, min(ret * sign, 2**31-1))


class Solution:
    aviable_list=['0','1','2','3','4','5','6','7','8','9']
    def myAtoi(self, str: str) -> int:
        str=list(str)
        if not str:
            return 0
        while str[0]==' ':
            str.pop(0)
            if not str:
                return 0
        
        if str[0]=='-':
            sign_digit=-1
            str.pop(0)
        elif str[0]=='+':
            sign_digit=1
            str.pop(0)
        elif not (str[0] in self.aviable_list):
            return 0
        else:
            sign_digit=1
            
        res=0
        if not str:
            return 0
        s=str.pop(0)
        while s in self.aviable_list:
            temp=self.aviable_list.index(s)
            res=res*10+temp
            if str:
                s=str.pop(0)
            else:
                break
        out = res*sign_digit
        if out>2**31-1:
            return 2**31-1
        elif out<-2**31:
            return -2**31
        else:
            return res*sign_digit

