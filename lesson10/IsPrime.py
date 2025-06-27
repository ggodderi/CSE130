# Python

import math
# Check to see if a number is a prime number.

# def is_number_prime(number):
#     if number <= 1:
#         return False
#     elif number == 2:
#         return True
#     else:            
#         is_prime = True

#         end_condition = math.ceil(math.sqrt(number))
#         #print(end_condition)

#         for counter in range(2, end_condition + 1, 1):
#             is_prime = is_prime and number % counter != 0
#     return is_prime

def is_number_prime2(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:            
        is_prime = True

        end_condition = math.ceil(math.sqrt(number))
        #print(end_condition)

        for counter in range(2, end_condition + 1, 1):
            if number % counter == 0:
                return False
    return True



def ask_user_for_number():
    done = False
    number = 0
    while not done:
        try:
            number = int(input('Please input the number for which the is prime test will be conducted: (0 to quit) '))
            if number >= 0:
                done = True
            else: 
                raise TypeError
        except (ValueError,TypeError):
            print('Please input an integer number. ')
    return number

def output_number_is_prime(number):
    is_prime = is_number_prime2(number)
    if is_prime:
        print(f'{number} is a Prime number')
    else:
        print(f'{number} is a NOT Prime number')

def test_is_number_prime(number):
    prime_numbers = []
    for n in range(1, number):
        is_prime = is_number_prime2(n)
        if is_prime:
            prime_numbers.append(n)
    
    print(f'The prime numbers below 1000 is: {prime_numbers}')

def main():
    test_is_number_prime(10001)
    number = -1

    while number != 0:
        number = ask_user_for_number()
        if number != 0:
            output_number_is_prime(number)

main()
