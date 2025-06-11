

import math

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
    # radius = obtain_user_radius()
    radius = 10
    print(calculate_circle_area(radius))
    # print(calculate_circle_area(radius))

main()