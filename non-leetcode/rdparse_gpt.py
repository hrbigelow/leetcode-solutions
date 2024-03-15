def parse_expression(tokens):
    """
    Parses an expression, which is a sequence of terms separated by '+' or '-'.
    """
    node = parse_term(tokens)

    while tokens and tokens[0] in '+-':
        op = tokens.pop(0)
        right = parse_term(tokens)
        node = [op, node, right]

    return node

def parse_term(tokens):
    """
    Parses a term, which is a sequence of factors separated by '*' or '/'.
    """
    node = parse_factor(tokens)

    while tokens and tokens[0] in '*/':
        op = tokens.pop(0)
        right = parse_factor(tokens)
        node = [op, node, right]

    return node

def parse_factor(tokens):
    """
    Parses a factor, which can be a number or an expression in parentheses.
    """
    token = tokens.pop(0)

    if token == '(':
        node = parse_expression(tokens)
        if tokens.pop(0) != ')':
            raise ValueError("Missing closing parenthesis")
        return node

    elif token.isdigit():
        return token

    else:
        raise ValueError(f"Invalid token: {token}")

def parse(tokens):
    """
    Initiates the parsing process and checks for any remaining tokens after parsing.
    """
    if not tokens:
        raise ValueError("Empty token list")

    node = parse_expression(tokens)

    if tokens:
        raise ValueError("Unexpected tokens after parsing")

    return node

# Example usage
expression1 = ['2', '-', '3', '+', '1']
expression2 = ['2', '-', '(', '3', '+', '1', ')']

print("Parse Tree for First Expression:", parse(expression1))
print("Parse Tree for Second Expression:", parse(expression2))


