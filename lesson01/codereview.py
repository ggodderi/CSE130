# Python Code review

my_string = '''This is a long
multline
comment

asdf
a
fd
a'''

# print(my_string)

my_string = "It's a small world after all."

# Comments - one line and tripple quoted

# Varibles - Int, Bool, String, Float, List, Dictionary

my_data = [2, 3, 34, 390, 3433]
my_tuple = (2, 3, 5, 99)
my_data_dictionary = {1 : "bob", 2: 'Billy'}

# user input

# Output

# Math Operators

# Operator Precedence

x = (10 + 20) * 3

# Shorthand Operators

#  x += 1
# x = x + 1
#  -=, /=, *=

# If statements, if, elif, else, and, or

# x = 9
# if x == 10 or 11:


# Loops
# for index in range(-10, 101, 5):
#     print(index)    

for index in range(10, 20, 2):
    print(index)
# Functions

import math
def calculate_circle_area(radius):
    area = math.pi * radius * radius # (radiux ** 2)
    r = radius ** 3.42
    math.sqrt()
    return area

circle_area = calculate_circle_area(10)
print(f'The area of the circle is: {circle_area}')