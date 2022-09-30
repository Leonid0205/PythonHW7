def get_operands(a_type):
    print()
    print('Float numbers are writen like: 7.7.\n'
          'Complex numbers are writen like: 7+7j or 7-7j or 7 than the imaginary "j" part wil be zero.')
    print()
    while True:
        if a_type == 1:
            try:
                a = input(f'Input a type rational OPERAND: ')
                a = float(a)
                break
            except:
                print('Incorrect input')
        else:
            try:
                a = input(f'Input a type complex OPERAND: ')
                a = complex(a)
                break
            except:
                print('Incorrect input')
        if a:
            continue
        else: 
            break
    return a
def get_type():
    print()
    print('Input "1" for rational numbers\n'
          'Input "2" for complex numbers')
    print()
    while True:
        operands_type = input(f'Input TYPE for an operand: ')
        try:
            operands_type = int(operands_type)
            if 1 <= operands_type <= 2:
                break
            else:
                print('Incorrect input')
                continue
        except:
            print('Incorrect input')
    return operands_type
def get_operation():
    print()
    print('Avaliable operations: \n'
          "'*' multiplication, '/' division, '+' sum, '-' subtraction")
    print()
    while True:
        operation = input('Input opreration: ')
        if operation == '+' or operation == '-' or operation == '/' or operation == '*':
            return operation
        else:
            print('Incorrect input')
        if operation:
            continue
        else:
            break
    return operation