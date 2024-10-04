# Python


import math


def my_assert(condition, error_code, function_name, file_name, message):
    # print(condition)
    if not condition:
        print(f"ASSERT fired, exiting")
        print(f'The error code is: {error_code}')
        print(f'Failing function: {function_name}')
        print(f'Failing file name: {file_name}')
        print(f'Assert Message: {message}')
        exit()


def calculate_circle_area(radius):
    my_assert(radius > 0, "10.20.32", 'calculate_circle_area', __file__, "Radius MUST be > 0")
    area = math.pi * radius * radius
    return area

# def calculate_circle_area(radius):
#     assert type(radius) == type(1.0) or type(radius) == type(1), "radius is NOT correct type."
#     assert radius > 0, 'Radius MUST be > 0'
#     area = math.pi * radius * radius
#     assert area >= 0
#     return area

def main():
    radius = 0
    circle_area = calculate_circle_area(radius)
    assert circle_area != None
    print(f'The area of a circle of radius: {radius} is: {circle_area}')

main()