s = 'abcdefghij'
n = len(s)

"""
None   None                                          None
Neg    -11  -10  -9  -8  -7  -6  -5  -4  -3  -2  -1  ?
Pos      ?    0   1   2   3   4   5   6   7   8   9  10
  s     null  a   b   c   d   e   f   g   h   i   j  null


For the expression s[beg:end:step], assume that:

if step<0, then [beg, end) goes from right to left.
if step>0, then [beg, end) goes from left to right

Which of the following combinations of styles are valid?
"""


for b in (1, -9):
    for e in (4, -6):
        print(f's[{b}:{e}] = {s[b:e]}')

print('\n\nbeg is the first element')
for b in (None, 0, -10):
    for e in (4, -6):
        print(f's[{b}:{e}] = {s[b:e]}')

print('\n\nend is the end') 
for b in (1, -9):
    for e in (None, 10):
        print(f's[{b}:{e}] = {s[b:e]}')


print('\n\nNegative step')
for b in (5, -5):
    for e in (0, -10):
        print(f's[{b}:{e}:-1] = {s[b:e:-1]}')

print('\n\nend is the end')
for b in (5, -5):
    for e in (-11, None):
        print(f's[{b}:{e}:-1] = {s[b:e:-1]}')

print('\n\nbeg is the first element (of reverse array)')
for b in (None, -1):
    for e in (0, -10):
        print(f's[{b}:{e}:-1] = {s[b:e:-1]}')









