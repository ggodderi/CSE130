# Python

# Use Recursion to calculate the Francois number, which is:
# F(1) = 2
# F(2) = 1
# F(n) = F(n-1) + F(n-1)
iterations = 0

def calculate_francois(number):
    ''' Calculate the franscoi number.'''
    assert number >= 1
    
    # keep track of the number of iterations
    global iterations
    iterations += 1

    # F(1) = 2, F(2) = 1
    if number == 1:
        return 2
    elif number == 2:
        return 1
    # F(n) = F(n-1) + F(n-2)
    else:
        return calculate_francois(number - 1) + calculate_francois(number - 2)



# Loop until the user gives a valid positive number.
done = False
while not done:
    number = int(input('Enter the Francois Number to Calculate: '))
    if number > 0:
        done = True
    else:
        print(f'{number} is invalid, please enter a valid number > 0.')

assert number >= 1
francois_number = calculate_francois(number)

print(f'{number}:  Francois number:{francois_number}, took: {iterations} iterations to complete.')