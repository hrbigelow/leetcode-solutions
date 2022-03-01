"""

1. The while loop represents the function body.  But, unlike with recursion,
when a function call returns to its calling function, it returns to the address
where it was called.  In contrast, in the while-loop stack-based solution, the
'function' call returns to the top of the while loop.  The mechanism of
'returning' to the call address is implemented by storing a logical (symbolic)
call address as one of the components of the stack cell.  This address is then
consulted inside of the while loop to jump to the appropriate part of the while
loop body.

Therefore, one full 'execution' of the function which calls itself recursively
k times consists of k+1 passes through the while loop.  Each pass has a
different address.

2. The items on the explicit stack consist of all function arguments, temporary
variables, and return values.  The effect of the while loop is to manipulate
the state of the top of the stack.  These k+1 passes through the while loop
which correspond to a particular stack item in turn change the state k+1 times.
The final pass populates the return value components of the stack.

Is it possible to have two addresses in the stack?  Yes, the second
one should be an execution address.

"""


def fibonacci(n):
    # loc 1
    if n < 3:
        return 1
    else:
        a = fibonacci(n-1)

        # loc 2
        b = fibonacci(n-2)

        # loc 3
        ret = a + b
        return ret


class CallState:
    # represents the calling state
    def __init__(self, inp, call_addr):
        self.inp = inp   # input to the function
        self.call_addr = call_addr # where the function was called from
        self.at = 1  # where the function currently is in its execution
        self.a = None       # temporary variable a
        self.b = None       # temporary variable b
        self.ret = None     # return value

    def __repr__(self):
        names = ['top', 'first', 'second', 'third']
        return f'{self.inp}-{names[self.call_addr]}-' \
                + f'{names[self.at]}-{self.a}-{self.b}-{self.ret}'


import time

def fibonacci_stack(n):
    
    st = [CallState(n, 0)]

    while st:
        cs = st[-1]
        print('   ' * (len(st)-1), cs)
        
        if cs.at == 1 and cs.inp < 3:
            cs.a = 0
            cs.b = 1
            cs.at = 3  

        elif cs.at == 1 and cs.inp >= 3:
            st.append(CallState(cs.inp - 1, cs.at))
            cs.at = 2

        elif cs.at == 2:
            st.append(CallState(cs.inp - 2, cs.at))
            cs.at = 3
        
        elif cs.at == 3:
            cs.ret = cs.a + cs.b
            print('   ' * (len(st)-1), cs, ' (return)')
            st.pop()
            if cs.call_addr == 0:
                return cs.ret
            elif cs.call_addr == 1:
                st[-1].a = cs.ret
            elif cs.call_addr == 2:
                st[-1].b = cs.ret


