
n = int(input('Please input a postive integer <= 20): '))

total_sum = 0
factorial = 1
power_of_two = 1
for i in range(1, n + 1):
    total_sum += i
    factorial *= i
    power_of_two *= 2


print(total_sum, factorial, power_of_two)

total_sum = 0
factorial = 1
power_of_two = 1
count = 1
while count < n+1:
    total_sum += count
    factorial *= count
    power_of_two *= 2
    count += 1
print(total_sum, factorial, power_of_two)


total_sum = 0
factorial = 1
power_of_two = 1
count = 1
done = False
while not done:
    total_sum += count
    factorial *= count
    power_of_two *= 2
    count += 1
    if count >= n+1:
        done = True
print(total_sum, factorial, power_of_two)


