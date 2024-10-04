# Python

import math

def my_assert(condition, code, message, function_name, file_name):
    if __debug__ and not condition:
        print(f'ASSERT FAILED: Code: {code}')
        print(f'ASSERT Message: {message}')
        print(f'Function wherein failure occurred: {function_name}')
        print(f'File name wherein assert occurred: {file_name}')
        print('Program exiting . . . ')
        exit(1)


def calculate_circle_area2(radius):
    my_assert(type(radius) == type(1.0) or type(radius) == type(1), "10.20.30", "Radius is invalid type", "calculate_circle_area2", __file__)   
    my_assert(radius > 0, "10.20.32", "Radius must be greater than 0", "calculate_circle_area2", __file__)   
    area = math.pi * radius * radius
    my_assert(area > 0, "10.20.33", "Area must be greater than 0", "calculate_circle_area2", __file__)   
    return area

def calculate_circle_area(radius):
    assert type(radius) == type(1.0) or type(radius) == type(1)  
    assert radius > 0
    area = math.pi * radius * radius
    assert area > 0
    return area


def main():
    radius = 10.1
    circle_area = calculate_circle_area(radius)
    print(f'The area of a circle with a radius of: {radius} is: {circle_area}')
    
    radius = -1
    circle_area = calculate_circle_area2(radius)
    print(f'The area of a circle with a radius of: {radius} is: {circle_area}')


main()