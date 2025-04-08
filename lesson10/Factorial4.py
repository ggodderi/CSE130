#

number = 10

number = int(input('Please input the number: '))

factorial = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10

print(factorial)

base = 1

for i in range(1, number+1):
    base *= i 
    print(base)

result = 1
i = 1
while i <= number:
    result *= i
    i += 1
    print(result)

numbers_list = list(range(1, number+1))

base = 1
for number in numbers_list:
    base *= number
    print(base)