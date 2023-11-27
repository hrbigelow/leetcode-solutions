"""
Generate all valid strings of parentheses of length 2n

What would the bottom-up or top-down approaches look like?

Virtually, one can think of the construction of each as a path
through a height-n binary tree.


What about a function that returns all possible extensions given a prefix?


"""

def gen_parens_yield(n):
    def gen(prefix, nopen, imbal):
        if nopen == 0 and imbal == 0:
            yield prefix
        if nopen > 0:
            yield from gen(prefix+'(', nopen-1, imbal+1)
        if imbal > 0:
            yield from gen(prefix+')', nopen, imbal-1)
    return list(gen('', n, 0))

def gen_parens_accu(n):
    results = []
    def gen(prefix, nopen, imbal):
        if nopen == 0 and imbal == 0:
            results.append(prefix)
        if nopen > 0:
            gen(prefix+'(', nopen-1, imbal+1)
        if imbal > 0:
            gen(prefix+')', nopen, imbal-1)
    gen('', n, 0)
    return results

def gen_parens_ret(n):
    def gen(prefix, nopen, imbal):
        results = []
        if nopen == 0 and imbal == 0:
            results.append(prefix)
        if nopen > 0:
            results.extend(gen(prefix+'(', nopen-1, imbal+1))
        if imbal > 0:
            results.extend(gen(prefix+')', nopen, imbal-1))
        return results
    return gen('', n, 0)

from functools import lru_cache
def gen_parens_catalan(n):
    @lru_cache
    def gen(k):
        if k == 0:
            return ['']
        results = []
        for i in range(k):
            left = gen(i)
            right = gen(k-i-1)
            combos = [ f'({l}){r}' for l in left for r in right ]
            results.extend(combos)
        return results
    return gen(n)










