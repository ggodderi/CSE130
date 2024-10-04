# Python

import random

def my_assert(condition, code, function_name, file):
    if not condition:
        print('assert FAILED!  Program exiting . . .')
        print(f'Assertion Code: {code}')
        print(f'Failing function name: {function_name}, \nFailing File: {file}')
        exit()


for i in range(10):
    print(i, end = '')

# print()

if __debug__:
    my_assert(i == 9, '10.20.09', 'python main', __file__)
    my_assert(i >= 10, '10.20.10', 'python main', __file__)

print('This is after the assert')


print(random.randint(1, 100))

word_list = ['bob', 'billy']
print(random.choice(word_list))