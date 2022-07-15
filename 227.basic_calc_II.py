"""
Given a string s which represents an expression, evaluate this expression and
return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate
results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings
as mathematical expressions, such as eval().

"""


import re

class Solution:
    def calculate(self, s: str) -> int:
        toks = re.findall('\d+|[\*\/\+-]', s+'+0')
        
        # a op1 b op2 c
        a, b = 0, int(toks[0])
        op1 = '+'
    
        i = 1
        while i != len(toks):
            op2 = toks[i]
            c = int(toks[i+1])
            i += 2

            if op2 in '+-':
                a = a + b if op1 == '+' else a - b
                op1, b = op2, c
                
            else:
                b = b * c if op2 == '*' else b // c
                
        return a

"""
The evaluation consists of a number of pairwise reductions of the form p op q.
It cannot quite be done left to right because a (+ or -) b (* or /) c must first combine
b and c.  However, knowing five tokens, one can guarantee one reduction.  It is convenient
to store a current state of a op b, and then parse the expression as a set of (op, v) pairs.

The final '+0' forces the last p op q reduction to take place before the while loop exits.
"""
