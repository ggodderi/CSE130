
import math


def my_assert(expression, code, function_name):
    if not expression:
        print(f'Assertion Failed. Assert Code: {code}, in function: {function_name}')
        print('Stopping Program')
        exit()


def calculate_circle_area(radius):
    assert radius > 0
    area = math.pi * radius * radius
    assert area > 0
    return area


def main():
    area = calculate_circle_area(10)
    print(f'Area is: {area}')
    x = 4
    my_assert(x > 10, "10.20.30", "main")

    age = int(input('Please input your age: '))
    print(f'Your age is: {age}')

main()

