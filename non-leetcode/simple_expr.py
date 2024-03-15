def simple_expr(expr):
    term = int(expr[0])
    total = 0
    for i in range(1, len(expr), 2):
        op, num = expr[i], int(expr[i+1])
        if op == '*':
            term *= num
        else:
            total += term
            term = num
    total += term
    return total


print(simple_expr(list('2*3+4+5*6*2'))) # 70

