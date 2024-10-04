# Python

# Test different Loops

for i in range(3, 100, 5):
    print(i, end=' ')


i = 3
print()

while i <= 100:
    print(i, end = ' ')
    i += 5

print()

numbers = list(range(3, 100, 5))
for number in numbers:
    print(number, end = ' ')

print()

x = range(3, 100, 5)
print(list(x))