def operations_a_b(oper, a, b):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '/':
        return a / b
    elif oper == '*':
        return a * b
    else:
        return 'Incorrect operation'