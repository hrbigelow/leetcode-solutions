"""

"""
# 25 ms 
class Solution:
    def countSubstrings(self, s: str) -> int:
        i, j = 0, 0
        start = 0
        total = 0
        while i < len(s):
            j,k = i,i
            total+=1
            while(k<len(s)-1 and s[k]==s[k+1]):
                k+=1
                total+=(k-j+1)
            i = k+1
            while (j>0 and k<len(s)-1 and s[j-1]==s[k+1]):
                total+=1
                j-=1
                k+=1
        return total


"""
If we start at some position and iterate forward and backward at the same time,
we need each position to be centered


This is basically a brute-force approach to count all
odd-length palindromes, and then even-length palindromes.


"""

# 140 ms (my solution)
class Solution:
    def countSubstrings(self, s: str) -> int:
        # odd-length palindromes
        n = len(s)
        npal = 0
        for i in range(n):
            npal += 1
            d = 1
            while i-d >= 0 and i+d < n:
                if s[i+d] == s[i-d]:
                    npal += 1
                else:
                    break
                d += 1

        # print(npal)
        for i in range(n-1):
            if s[i] == s[i+1]:
                npal += 1
                d = 1
                while i+d+1 < n and i-d >= 0:
                    if s[i-d] == s[i+1+d]:
                        npal += 1
                    else:
                        break
                    d += 1

        return npal
