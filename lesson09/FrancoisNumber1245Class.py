# Python


QUIT_TOKEN = 0


#################################################################
def ask_user_for_number():
    '''Ask the user for the Francois number to calculate. '''
    done = False

    # Loop until a valid number is obtained.
    while not done:
        francois_number_to_calculate = int(input(f'Please input the Francois Number you wish to calculate (>{QUIT_TOKEN}, {QUIT_TOKEN} to end): '))
        if francois_number_to_calculate >= QUIT_TOKEN:
            done = True
        else:
            print(f'{francois_number_to_calculate} is invalid, please try again.')
    
    assert francois_number_to_calculate >= QUIT_TOKEN
    assert type(francois_number_to_calculate) == type(1)
    return francois_number_to_calculate


##############################################################
def calculate_francois_number(francois_number):
    ''' Calculate the Francois Number, which is:
        F(1) = 2
        F(2) = 1
        F(n) = F(n-1) + F(n-2)
        
        RETURNS:  calculated francois number AND iteration count 
        '''

    assert francois_number >= 1
    iteration_count = 0

    # Array used to hold the Francois numbers.
    # Note: F(1) = 2 and F(2) = 1.
    number_array = [2, 1]

    # Handle the first and second francois numbers.
    if francois_number == 1:
        return number_array[0], 0
    elif francois_number == 2:
        return number_array[1], 0
    
    # Calculate the number.
    for i in range(2, francois_number):
        iteration_count += 1
        assert 2 <= i < francois_number

        # Cleverly use the array of two numbers to hold the calulated number.
        number_array[i % 2] = number_array[0] + number_array[1]
        #print(number_array[i%2])

    assert 2 <= i < francois_number
    assert iteration_count >= 0
    # Return the latest number AND the iteration count it took to calculate the number.
    return number_array[i % 2], iteration_count


############################################################
def main():
    ''' Main routine to perform Francois calculation. 
    Loop until the user wants to quit.'''
    francois_number_to_calculate = 1

    # Loop until the user wants to quit (enters a 0)
    while francois_number_to_calculate != QUIT_TOKEN:
        francois_number_to_calculate = ask_user_for_number()

        # If the user wants a valid Francois number, calculate it.
        if francois_number_to_calculate > QUIT_TOKEN:
            francois_number, iteration_count = calculate_francois_number(francois_number_to_calculate)
            assert francois_number >= 0
            assert iteration_count >= 0

            print(f'The {francois_number_to_calculate} of the Francois Sequence is: {francois_number}')
            print(f'It took {iteration_count} iterations to calculate the number.')

main()