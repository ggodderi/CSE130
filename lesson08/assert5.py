

import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

def obtain_user_radius():
    return 10

def main():
    radius = obtain_user_radius()
    print(calculate_circle_area(radius))

main()