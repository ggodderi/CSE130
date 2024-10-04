# Python


import math

def display_prime_number_list(prime_list, max_prime_number):
    '''Output the list of prime numbers '''
    assert len(prime_list) >= 2
    assert max_prime_number + 1 == len(prime_list)
    assert prime_list[2] == True
    assert max_prime_number >= 2
    print(f'The prime numbers less than {max_prime_number} are: ')
    total_prime_numbers = 0
    for i in range(2, max_prime_number + 1):
        assert i >= 1 and i < max_prime_number + 1
        if prime_list[i]:
            total_prime_numbers += 1
            print(i, end=',')
    print()
    print(f'There were: {total_prime_numbers} prime number less than {max_prime_number}')

def obtain_max_prime_number():
    '''Ask the user for the maximum prime number.
    Return the max number and its square root'''
    done = False
    while not done:
        max_prime_number = int(input('Please input the maximum prime number you wish to find: '))
        if max_prime_number < 2:
            print(f'Invalid maximum prime number.  Please enter a number >= 2')
        else:
            done = True
    
    max_sqrt_value = math.ceil(math.sqrt(max_prime_number + 1))
    return max_prime_number, max_sqrt_value


def find_prime_numbers(prime_list, max_prime_number, max_sqrt_value):
    '''Use the prime number algorithm to calculate the prime number. '''
    iterations = 0
    assert len(prime_list) >= 2
    assert len(prime_list) == max_prime_number + 1

    for i in range(2, max_sqrt_value):
        assert i >= 2 and i <= max_sqrt_value
        if prime_list[i]:
            for n in range(i * i, max_prime_number + 1, i):
                iterations += 1
                prime_list[n] = False
    
    return prime_list, iterations



max_prime_number, max_sqrt_value = obtain_max_prime_number()
prime_list = [True] * (max_prime_number + 1)

prime_list, iterations = find_prime_numbers(prime_list, max_prime_number, max_sqrt_value)
display_prime_number_list(prime_list, max_prime_number)
print(f'Max Prime number: {max_prime_number}, Iteration count: {iterations}')


