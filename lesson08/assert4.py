
import math
def calculate_circle_area(radius):
    assert radius != None
    assert type(radius) == type(1.0)
    assert radius > 0
    area = math.pi * radius * radius
    assert area > 0
    assert type(area) == type(1.0)
    return area

def obtain_user_radius():
    done = False

    while not done:
        try:
            radius = float(input('Please input a radius, which must be > 0: '))
            done = True
            if radius <= 0:
                done = False
                print('Radius must be > 0.  Please enter number > 0:')
        except (TypeError, ValueError) :
            done = False
            print('Must enter a number.')
    return radius
        

def main():
    radius = obtain_user_radius()
    area = calculate_circle_area(radius)
    print(area)

main()
