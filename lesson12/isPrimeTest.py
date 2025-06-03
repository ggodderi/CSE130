import math
# Check to see if a number is a prime number.

def is_number_prime(number):
    '''Return true if a number is Prime.
    Only have to test up to the square root of a number.'''
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

def test_is_number_prime():
    assert is_number_prime(101) == True
    assert is_number_prime(1) == False
    assert is_number_prime(2) == True
    assert is_number_prime(-1) == False
    assert is_number_prime(0) == False
    assert is_number_prime(17) == True
    assert is_number_prime(8) == False


    assert is_number_prime(18_700_530_018) == False
    assert is_number_prime(18_700_530_019) == False

    # assert is_number_prime('Bob') == True
    # assert is_number_prime(1.234) == False

    # assert is_number_prime(100) == True

    print('All tests passed!')


def test_is_number_prime_all_numbers(limit):
    for i in range(limit):
        if is_number_prime(i):
            print(f'{i} is prime')
    

def main():

    test_is_number_prime()
    test_is_number_prime_all_numbers(10000)
    # if __debug__:
    #     print(is_number_prime(101))
    #     while 12:
    #         number = int(input('Please inptut a number to test for primeness:'))
    #         print(f'{number} is prime: {is_number_prime(number)}')

main()