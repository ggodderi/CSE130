# Python


numbers = [ 23, 1, 45, 65, 89, 23, 1, 17, -12, 99, 14, 8, 27, 3]
len_numbers = len(numbers)

for i in range(len(numbers) - 1, 0, -1):
    for j in range(0, i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        print(numbers)

print(numbers)
assert len(numbers) == len_numbers