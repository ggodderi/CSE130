

import math
def Calculate_circle_area(radius):
    assert type(radius) == type(1.0) or type(radius) == type(1)
    assert radius > 0
    assert radius != None
    area = math.pi * radius * radius
    assert area > 0
    assert type(area) == type(1.0)
    return area

def main():
    radius = float(input('Please input the radius: '))
    circle_area = Calculate_circle_area(radius)
    print(f'Circle area is: {circle_area}')

main()