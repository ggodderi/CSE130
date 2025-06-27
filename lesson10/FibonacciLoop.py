# Python

count = 0
# Calculate the Fibonacci Sequence

fib_number_to_calculate = int(input('Input the fibonacci number to calculate:  '))

numbers = [0] * (fib_number_to_calculate+1)
for fib_number in range(fib_number_to_calculate + 1):

    numbers[0] = 0
    numbers[1] = 1
    n = fib_number
    count = 0
    for i in range(1, n):
        count += 1
        numbers[i+1] = (numbers[i-1] + numbers[i])

    fibonacci_total = numbers[n]
    # print(f'The Fibonacci of: {fib_number} is: {fibonacci_total}, the iteration count is: {count}')
print(numbers)



fib_number_to_calculate = int(input('Input the fibonacci number to calculate:  '))

for fib_number in range(fib_number_to_calculate + 1):

    numbers = [0, 1]
    n = fib_number
    count = 0
    for i in range(1, n):
        count += 1
        numbers.append(numbers[i-1] + numbers[i])

    fibonacci_total = numbers[n]
    # print(f'The Fibonacci of: {fib_number} is: {fibonacci_total}, the iteration count is: {count}')
print(numbers)



fib_number_to_calculate = int(input('Input the fibonacci number to calculate:  '))

for fib_number in range(fib_number_to_calculate + 1):

    numbers = [0, 1]
    n = fib_number
    count = 0
    for i in range(n):
        count += 1
        numbers[i % 2] = numbers[0] + numbers[1]

    fibonacci_total = numbers[n % 2]
    print(f'The Fibonacci of: {fib_number} is: {fibonacci_total}, the iteration count is: {count}')



# calculating_n1 = True
# calculating_n2 = True
# fibonacci_total = 0

# while n > 0:
#     fibonacci_total += 1
#     n2 = n - 1
#     count += 1
#     while n2 > 0: 
#         fibonacci_total += 1
#         count += 1
#         n2 -= 1
#     n -= 1

# while calculating_n1:
#     if n <= 1:
#         calculating_n1 = False
#         fibonacci_total += 1
#     else:
#         count += 1
#         fibonacci_total += 1

#         n2 = n - 1
#         calculating_n2 = True
#         while calculating_n2:
#             if n2 <= 1:
#                 calculating_n2 = False
#                 fibonacci_total += 1
#             else:
#                 count += 1
#                 fibonacci_total += 1
#             n2 -= 1
#     n -= 1


#print(f'The Fibonacci of: {fib_number} is: {fibonacci_total}, the iteration count is: {count}')