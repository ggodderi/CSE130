
import math
import inspect
import traceback


def my_assert(expression, message, code, filename, line_number, function_name):
    if not expression and __debug__:
        print(message)
        print(f'Error Code: {code}')
        print(f'File name: {filename}')
        print(f'Line Number: {line_number}')
        print(f'Function Name: {function_name}')
        traceback.print_stack()
        print('Exiting the program . . .')
        exit(1)

def calculate_circle_area(radius):
    my_assert(radius > 0, "Bad radius", "49.38.07", __file__,
              inspect.currentframe().f_lineno,
              inspect.currentframe().f_code.co_name)
    assert radius > 0
    assert type(radius) == type(1.0)
    area = math.pi * radius * radius
    assert type(area) == type(1.0)
    assert area > 0
    assert area > radius
    return area

def main():
    # print(calculate_circle_area(10))

    radius = float(input('Please input a radius: '))
    # assert radius > 0
    # assert type(radius) == type(1.0)
    print(calculate_circle_area(radius))

main()