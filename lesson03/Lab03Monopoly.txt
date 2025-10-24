# Python

# This program will let the user know if they can add a hotel to Penn Avenue

# True if there is still the option to buy a hotel
continue_on = True

# Local variables
pa_status = 0
nc_status = 0
pc_status = 0
number_of_houses_needed = 0
number_of_houses_available = 0
pa_houses_needed = 0
pc_houses_needed = 0
nc_houses_needed = 0


# Own all properties?
own_all_green_properterties = input('Do you own all three of the green (Pacific, Penn, and NC) properties (y/n)? ')

# If not, state so and end
if own_all_green_properterties.lower() == 'n':
        print('You must own all three green properties to be able to place a hotel on Penn Avenue.')
        continue_on = False

# What is on Penn Avenue
if continue_on:
    pa_status = int(input('What is on Penn Avenue (0: nothing, 1: 1 house, 2: 2 houses, 3: 3 houses, 4: 4 houses, 5: 1 hotel): '))
    # If already have a hotel, state so and end
    if pa_status == 5:
        print('Penn Avenue already has a hotel, no need to buy one.')
        continue_on = False

# What is on North Carolina?
if continue_on:
    nc_status = int(input('What is on North Carolina (0: nothing, 1: 1 house, 2: 2 houses, 3: 3 houses, 4: 4 houses, 5: 1 hotel): '))
    # If hotel, swap with Penn Avenue
    if nc_status == 5 and pa_status == 4:
        print('You can swap your NC hotel with your PA houses')
        continue_on = False

# What is on Pacific Avenue?
if continue_on:
    pc_status = int(input('What is on Pacific Avenue (0: nothing, 1: 1 house, 2: 2 houses, 3: 3 houses, 4: 4 houses, 5: 1 hotel): '))
    # If hotel, swap with Penn Avenue
    if pc_status == 5 and pa_status == 4:
        print('You can swap your Pacific Avenue hotel with your PA houses')
        continue_on = False

# Now that all three status are known, calculate the number of houses needed.
if continue_on:
    number_of_houses_needed = 12 - pa_status - pc_status - nc_status
    pa_houses_needed = 4 - pa_status
    pc_houses_needed = 4 - pc_status
    nc_houses_needed = 4 - nc_status

    # Find out how many houses the bank has
    number_of_houses_available = int(input('How many houses are there available? '))
    # If the bank doesn't have enough houses, state so and end.
    if number_of_houses_available < number_of_houses_needed:
        print(f'There are not enough houses available.  You need {number_of_houses_needed} and there are only {number_of_houses_available} availble')
        continue_on = False

# Find out how many hotels the bank has.
if continue_on:
    number_of_hotels_available = int(input('How many hotels are there available? '))

    # If there are not enough hotels, state so and end.
    if number_of_hotels_available < 1:
        print(f'There are not enough hotels available.  You need {1} hotel and there are only {number_of_hotels_available} availble')
        continue_on = False


# Still have the option to buy, calculate cost and get cash on hand
if continue_on:
    cash_needed = (number_of_houses_needed + 1) * 200
    cash_on_hand = int(input('How much cash do you have? '))

    # If don't have enough money, state so and end.
    if cash_on_hand < cash_needed:
        print(f'You do not have enough cash to purchase the hotel.  You need ${cash_needed} and you only have ${cash_on_hand}')
        continue_on = False

# At this point, we can purchase a hotel.  Tell the user the details.
if continue_on:

    print()
    print('Congratulations - you can purchase a hotel. \n')
    print(f'This will cost: ${cash_needed}')
    print(f'Purchase 1 hotel and {number_of_houses_needed} houses')
    print(f'{pa_houses_needed} houses needed for PA, then Put 1 hotel on Penn Avenue')
    print('Return all PA houses to the bank')

    # Check the individual needs of Pacific and NC
    if pc_houses_needed > 0:
        print(f'Put {pc_houses_needed} houses on Pacific Avenue.')
        
    if nc_houses_needed > 0:
        print(f'Put {nc_houses_needed} houses on North Carolina')
 

