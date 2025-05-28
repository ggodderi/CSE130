# Python Review

# Comments - doc strings/multiline strings
''' This is  my multiline
comment that I can use.'''
'This is a a single line comment.'

# print(comment)
# print(comment2)

# Variables
# end_of_data = 115
# for i in range(end_of_data):

# if i == end_of_data:
# x = 10
# x = 'Bob'


# Data Types - bool, int, float, string, list, etc


# Expressions
# x = 10 + 20 * 3

# # Operator precedence 
# x = (10 + 20) / 3 * 5 % (1 ** 3 + 1)
# y = 11
# x = y == 10

# Shortened notation

# x = 10
# # x =+ 1
# x += 1
# -=, *=, /=, %=, //=

# If statements
x = 10

# if x == or x != 11:
#     print(f'We know what X is.{x}')
y = 19
# if x == 10 or x == 11 and y == 20:
#     pass
# elif x == 11:
#     pass
# else:
#     pass

# Loops - For count, for in list, while

# correct_input_received = False
# while not correct_input_received:
#     age = int(input('Please input yoru age: '))
#     if age >= 0 and age <= 125:
#         correct_input_received = True


# for n in range(5, 100, 10):
#     print(n)

# colors = ['blue', 'orange', 'pink', 'black', 'white']
# for color in colors:
#     print(color)

# Lists/Arrays - print entire array, first three, last three, etc

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# print(alphabet[10:15])
# print(alphabet[-5:-3])
# print(alphabet[:-5])
# print(alphabet[5])

# Functions, parameters, arguments, return values
# def add_numbers(a, b, c, d=10):
#     total = a + b + c + d
#     return total

# total = add_numbers(1, 2, 3)
# print(total)
# total = add_numbers(1, 2, 3, 4)
# print(total)

# Input/output

# Write and Read from a text file
# with open('my_data_file.txt', 'wt+') as filehandle:
#     filehandle.write('He bob, how are you?')

# with open('my_data_file.txt', 'rt') as filehandle:
#     data = filehandle.read()
#     print(data)


# Dictionaries

my_data = {'Name' : 'Jeannie', 'Address': '555 Cherry Lanes', 'Phone' : 7675309}

# print(my_data['Name'])

my_data['Email'] = 'Jeannie@msn.com'

# print(my_data)

# my_data['Name'] = 'Bob'
# print(my_data)

# print(my_data.keys())
# for key in my_data.keys():
#     print(my_data[key])

# JSON

import json
with open('my_data.json', 'wt') as filehandle:
    json_data = json.dumps(my_data)
    filehandle.write(json_data)


with open('my_data.json', 'rt') as filehandle:
    json_data = filehandle.read()
    dictionary_data = json.loads(json_data)
    print(dictionary_data['Name'])

with open('Lab02.json', 'rt') as filehandle:
    json_data = filehandle.read()
    dictionary_data = json.loads(json_data)
    print(dictionary_data['password'])
