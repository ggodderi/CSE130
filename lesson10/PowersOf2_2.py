


number = int(input('Please input a number: '))

for i in range(number + 1):
    # power = 2 ** i
    # print(power)
    print(2**i)


power = 1
for i in range(number):
    print(power)
    power *= 2

print(power)