from view import *
from operations import operations_a_b as op
from logger import *
from check import *
def button_click():
    print('Welocome to calculator app)')
    while True:
        a = get_operands(get_type())
        b = get_operands(get_type())
        operation = get_operation()
        if check_operation(b, operation):
            print('ZeroDivision Error\n'
                  'You need to input numbers agin')
            continue
        else:
            res = op(operation, a, b)
            print()
            print(f'Expression: {a} {operation} {b} = {res}')
            print()
            result_logger(operation, res, a, b)
        print('To exit the app press "q".\n'
          'To continue press any button')
        action = input()
        if action == 'q':
            break
        else:
            continue