

import math
import inspect
import traceback

def my_assert(expression, message, error_code, file_name,
              line_number, function_name):
    if not expression and __debug__:
        print(f'Assert Failed.')
        print(f'File Name: {file_name}')
        print(f'Function Name: {function_name}')
        print(f'Line Number: {line_number}')
        print(f'Assert Message: {message}')
        print(f'Assert Error Code: {error_code}')
        print()
        traceback.print_stack()
        print('Program Exiting . . .')
        exit(1)

def calculate_circle_area(radius):
    assert radius != None
    assert type(radius) == float or type(radius) == int
    assert radius > 0
    area = math.pi * radius * radius
    assert area > 0.0
    assert type(area) == type(0.0)
    return area

def obtain_user_radius():
    done = False

    while not done:
        try:
            radius = float(input('Please input a radius, which is > 0: '))
            if radius > 0:
                done = True
            else:
                print('Please enter a value > 0')
        except (TypeError, ValueError, ZeroDivisionError):
            print('Invalid valud, please input a number > 0.')

    return radius

def main():
    # if __debug__:
    my_assert(1>2, "Hey Bob", "49.38.07", __file__, 
              inspect.currentframe().f_lineno,
              inspect.currentframe().f_code.co_name)
    # radius = obtain_user_radius()
    radius = 10
    print(calculate_circle_area(radius))
    # print(calculate_circle_area(radius))


main()