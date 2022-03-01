def fibonacci(n):
    if n < 3:
        return 1
    else:
        a = fibonacci(n-1)
        b = fibonacci(n-2)
        ret = a + b
        return ret


class CallState:
    # represents the calling state
    def __init__(self, inp, addr, a, b, ret):
        self.inp = inp   # input to the function
        self.addr = addr # where the function was called from
        self.a = a       # temporary variable a
        self.b = b       # temporary variable b
        self.ret = ret   # return value

    def __repr__(self):
        return f'{self.inp}-{self.addr}-{self.a}-{self.b}-{self.ret}'


import time

def fibonacci_stack(n):
    
    st = [CallState(n, 'top', None, None, None)]

    while st:
        cs = st[-1]
        print('   ' * (len(st)-1), cs)
        
        if cs.inp < 3:
            cs.ret = 1

        elif cs.a is None:
            st.append(CallState(cs.inp - 1, 'first', None, None, None))
        elif cs.b is None:
            st.append(CallState(cs.inp - 2, 'second', None, None, None))
        
        else:
            cs.ret = cs.a + cs.b

        if cs.ret is not None:
            print('   ' * (len(st)-1), cs, ' (return)')
            st.pop()
            if cs.addr == 'first':
                st[-1].a = cs.ret
            elif cs.addr == 'second':
                st[-1].b = cs.ret



    return cs.ret

