
import math

def is_prime(number):
    limit = int(math.sqrt(number)) + 1

    # print(range(int(math.sqrt(100))))
    for n in range(2, limit):
        if number % n == 0:
            return False
    return True



for i in range(1, 2000):
    if is_prime(i):
        print(i)


print()

for i in range(int(math.sqrt(number))):
    print(i)