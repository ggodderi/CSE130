# Python

import math
# Check to see if a number is a prime number.

def is_number_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:            
        is_prime = True

        end_condition = math.ceil(math.sqrt(number))
        #print(end_condition)

        for counter in range(2, end_condition + 1, 1):
            is_prime = is_prime and number % counter != 0
    return is_prime


def ask_user_for_number():
    done = False
    while not done:
        number = int(input('Please input the number for which the is prime test will be conducted: (0 to quit) '))

        is_prime = is_number_prime(number)
        if is_prime:
            print(f'{number} is a Prime number')
        else:
            print(f'{number} is a NOT Prime number')
        
def test_is_number_prime():
    prime_numbers = []
    for n in range(1, 1001):
        is_prime = is_number_prime(n)
        if is_prime:
            prime_numbers.append(n)
    
    print(f'The prime numbers below 1000 is: {prime_numbers}')

def main():
    test_is_number_prime()
    ask_user_for_number()

main()
