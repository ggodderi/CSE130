# Python

# Program to print n!

number = int(input('Input the n of the n! function: '))

factorial = 1

for n in range(1, number + 1):
    factorial *= n
    print(f'The factorial of {n} is: {factorial}')


print(f'The factorial of {number} is: {factorial}')


factorial = 1
n = 1
while n <= number:
    factorial *= n
    print(f'The factorial of {n} is: {factorial}')
    n += 1

print(f'The factorial of {number} is: {factorial}')

factorial = 1
numbers = list(range(1, number+1, 1))
for n in numbers:
    factorial *= n
    print(f'The factorial of {n} is: {factorial}')

print(f'The factorial of {number} is: {factorial}')



