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

