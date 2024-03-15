"""
Problem:  decompress a string such as:

3{ab}        => ababab
2{ab2{cd}x}  => abcdcdxabcdcdx

(you get the idea)

The age-old challenge of writing a recursive function.

The recursive function evolves in iterative fashion.  First, you specify the main
task it should perform.  In this case, accept a compressed string s and return the
decompressed string.  Second, you imagine how you could accomplish this task if you
already can solve sub-problems.  What auxiliary information do you need the recursive
calls to return besides the solution to the subproblems?  This auxiliary information
is needed for two reasons.  First, it might be needed to assemble the solutions to
the sub-problems together.  Second, it might be needed as arguments to the recursive
calls.

In this case, it is needed for arguments to the recursive calls.

The deciding of what auxiliary information is needed is also an iterative process.
As you contemplate how you would assemble sub-solutions together, you notice certain
information you might need.  But, then, depending on how the coding goes, you might
notice you need additional auxiliary information.

The really tricky bit here was dealing with the close bracket '}'.  It doesn't seem
intuitive at all.
"""

def decompress(s, i):
    # decompress as much available of s[i:]
    # return decompressed part and index of first non-consumed part of s 
    if i == len(s):
        return '', i

    elif s[i].isalpha():
        ch = s[i]
        sub, i = decompress(s, i+1)
        return ch + sub, i

    elif s[i].isdigit():
        d = int(s[i])
        sub, i = decompress(s, i+2) # skip digit and '{'
        sub2, i = decompress(s, i)
        return d * sub + sub2, i
    else:
        assert s[i] == '}'
        return '', i+1 # '}' has no content, but we consume it 

tests = [
        '3{ab}',
        '2{ab2{cd}x}',
        ]

if __name__ == '__main__':
    for test in tests:
        print(f'{test}: {decompress(test, 0)[0]}')


