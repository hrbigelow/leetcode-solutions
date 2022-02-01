def isScramble(a: str, b: str) -> bool:
    memo = { }
    def helper(*args):
        if args in memo:
            return memo[args]
        a1, a2, b1, b2 = args
        n = a2 - a1
        if n == 1:
            return a[a1] == b[b1]
        elif a[a1:a2] == b[b1:b2]:
            return True
        else:
            for k in range(1, n):
                if (
                    helper(a1, a1+k, b1, b1+k) and helper(a1+k, a2, b1+k, b2) or
                    helper(a1, a1+k, b2-k, b2) and helper(a1+k, a2, b1, b2-k)
                ):
                    memo[args] = True
                    return True
        memo[args] = False        
        return False

    ans = helper(0, len(a), 0, len(b))
    for k, v in memo.items():
        print('{}: {}'.format(k, v))

    return ans 
