

number = -1

while number < 0:
    number = int(input('Please input a positive number: '))

n2 = number
total = number
while number > 0:
    total += number - 1
    number -= 1
15
print(total)

total = 1
factorial = 1
for i in range(1, n2+1, 1):
    total += i
    factorial *= i


print(total)
print(factorial)