# Ptyhon

# Calculate the powers of 2


number = int(input('Input the number of the power of 2 you wish to calcualte: '))

# Counter Controlled, use exponent/power (**) 
for n in range(number + 1):
    power = 2 ** n
    print(f'2 to the {n} power is: {power}')



# Counter Controlled - use multiplication
power = 1
for n in range(number + 1):
    if n != 0:
        power *= 2
    print(f'2 to the {n} power is: {power}')


# Event Controlled - use multiplication 
power = 1
n = 0
while n <= number:
    if n != 0:
        power *= 2
    print(f'2 to the {n} power is: {power}')
    n += 1

power = 1
# Collection controlled - use multiplication
numbers = list(range(number + 1))
for n in numbers:
    if n != 0:
        power *= 2
    print(f'2 to the {n} power is: {power}')