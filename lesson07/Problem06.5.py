# Python

# Problem 06.5 - Automatic Trace
print('Program to find the sum of number:  e.g., 3->  1 + 2 + 3 = 6.')
number = int(input('Please input a postive number for which the sum will be calculated: '))

total = 0
# Trace
print(f'{"Trace Table":12} {"n":>4} {"total":>7}')

for n in range(1, number):
    # Trace
    print(f'{"Line 1":12} {n:4} {total:7}')
    total += n
    # Trace
    print(f'{"Line 2":12} {n:4} {total:7}')

# Trace
print(f'{"Line 3":12} {n:4} {total:7}')

print(f'The sum of {number} is: {total}')