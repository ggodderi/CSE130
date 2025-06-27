import math
def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def ask_user_for_number():
    '''Return a positive integer( >= 0): '''
    while True:
        try:
            number = int(input('Please input a positive integer number (>=0): '))
            if number >= 0:
                return number
            else:
                raise ValueError
                # print('Please input a positive integer.')
        except(ValueError,TypeError):
                print('Please input a positive integer.')

def test_is_prime(number):
    prime_numbers = []

    for n in range(2, number):
        if is_prime(n):
            prime_numbers.append(n)
    
    print(prime_numbers)

def main():
    test_is_prime(100)
    number = ask_user_for_number()
    prime = is_prime(number)
    if prime:
        print(f'{number} is prime')
    else:
        print(f'{number} is not prime')


main()







# def test_is_prime(number):
#   
#   prime_numbers = []
#     for i in range(1, number + 1):
#         prime = is_prime(i)
#         if prime:
#             prime_numbers.append(i)
    
#     print(prime_numbers)