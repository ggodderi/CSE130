#

n = 10
factorial = 1

factorial = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10


print(f'Factorial is: {factorial}')

factorial = 1

for i in range(1, n+1):
    factorial = factorial * i

print(f'Factorial is: {factorial}')

i = 1
factorial = 1
while i <= n:
    factorial = factorial * i
    i += 1

print(f'Factorial is: {factorial}')

factorial = 1
numbers = list(range(1, n+1))
for n in numbers:
    factorial = factorial * n

print(f'Factorial is: {factorial}')



