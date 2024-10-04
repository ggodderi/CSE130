# Python

# This program will let the user know if they can add a hotel to Penn Avenue

# Function will determine if a house can be placed on Penn Avenue in Monopoly.
def can_purchase_hotel_for_penn_avenue():
    '''Can a hotel be placed on Penn Avenue?'''

    # local varibles 
    pa_status = 0
    nc_status = 0
    pc_status = 0
    number_of_houses_needed = 0
    number_of_houses_available = 0
    pa_houses_needed = 0
    pc_houses_needed = 0
    nc_houses_needed = 0

    # Own all green properties?
    own_all_green_properterties = input('Do you own all three of the green (Pacific, Penn, and NC) properties (y/n)? ')

    # if no, state so and return
    if own_all_green_properterties.lower() == 'n':
        print('You must own all three green properties to be able to place a hotel on Penn Avenue.')
        return False

    # Penn Avenue status
    pa_status = int(input('What is on Penn Avenue (0: nothing, 1: 1 house, 2: 2 houses, 3: 3 houses, 4: 4 houses, 5: 1 hotel): '))

    # if Penn Avenue already has a hotel, state so and end.
    if pa_status == 5:
        print('Penn Avenue already has a hotel, no need to buy one.')
        return False

    # North Carolina Status
    nc_status = int(input('What is on North Carolina (0: nothing, 1: 1 house, 2: 2 houses, 3: 3 houses, 4: 4 houses, 5: 1 hotel): '))

    # Swap houses and hotel with penn avenue if NC has a hotel and end.
    if nc_status == 5 and pa_status == 4:
        print('You can swap your NC hotel with your PA houses')
        return False

    # Pacific Avenue status
    pc_status = int(input('What is on Pacific Avenue (0: nothing, 1: 1 house, 2: 2 houses, 3: 3 houses, 4: 4 houses, 5: 1 hotel): '))

    # Swap houses and hotel with penn avenue if NC has a hotel and end.
    if pc_status == 5 and pa_status == 4:
        print('You can swap your Pacific Avenue hotel with your PA houses')
        return False

    # Now that all of the stati are known, find out how many houses are needed.
    number_of_houses_needed = 12 - pa_status - pc_status - nc_status
    pa_houses_needed = 4 - pa_status
    pc_houses_needed = 4 - pc_status
    nc_houses_needed = 4 - nc_status

    # How many houses does the bank have?
    number_of_houses_available = int(input('How many houses are there available? '))

    # If the bank doesn't have enough houses, state so and end.
    if number_of_houses_available < number_of_houses_needed:
        print(f'There are not enough houses available.  You need {number_of_houses_needed} and there are only {number_of_houses_available} availble')
        return False

    # How many hotels does the bank have?
    number_of_hotels_available = int(input('How many hotels are there available? '))

    # If there are not enough hotels in the bank, state so and end.
    if number_of_hotels_available < 1:
        print(f'There are not enough hotels available.  You need {1} hotel and there are only {number_of_hotels_available} availble')
        return False

    # Calcualte cash needed
    cash_needed = (number_of_houses_needed + 1) * 200

    # Obtain cash on hand
    cash_on_hand = int(input('How much cash do you have? '))

    # If not enough cash, state so and end.
    if cash_on_hand < cash_needed:
        print(f'You do not have enough cash to purchase the hotel.  You need ${cash_needed} and you only have ${cash_on_hand}')
        return False

    # A hotel may be purchased, tell the user the details of what is needed.
    print()
    print('Congratulations - you can purchase a hotel. \n')
    print(f'This will cost: ${cash_needed}')
    print(f'Purchase 1 hotel and {number_of_houses_needed} houses')
    print(f'{pa_houses_needed} houses needed for PA, then Put 1 hotel on Penn Avenue')
    print('Return all PA houses to the bank')


    # Output PC and NC status if needed.
    if pc_houses_needed > 0:
        print(f'Put {pc_houses_needed} houses on Pacific Avenue.')
        
    if nc_houses_needed > 0:
        print(f'Put {nc_houses_needed} houses on North Carolina')
    
    return True


while True:
    print('\n\n')
    can_purchase_hotel_for_penn_avenue()
 

