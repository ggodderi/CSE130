# Python

# Solution for the Monopoly program.
# Question to answer is:  Can I put a hotel on Penn Avenue?

def can_place_hotel_on_penn_avenue():

    own_all_green_properterties = input('Do you own all three of the green (Pacific, Penn, and NC) properties (y/n)? ')
    if own_all_green_properterties.lower() == 'n':
        print('You must own all three green properties to be able to place a hotel on Penn Avenue.')
        return False

    pa_status = int(input('What is on Penn Avenue (0: nothing, 1: 1 house, 2: 2 houses, 3: 3 houses, 4: 4 houses, 5: 1 hotel): '))
    if pa_status == 5:
        print('Penn Avenue already has a hotel, no need to buy one.')
        return False

    nc_status = int(input('What is on North Carolina (0: nothing, 1: 1 house, 2: 2 houses, 3: 3 houses, 4: 4 houses, 5: 1 hotel): '))
    if nc_status == 5 and pa_status == 4:
        print('You can swap your NC hotel with your PA houses')
        return False

    pc_status = int(input('What is on Pacific Avenue (0: nothing, 1: 1 house, 2: 2 houses, 3: 3 houses, 4: 4 houses, 5: 1 hotel): '))
    if pc_status == 5 and pa_status == 4:
        print('You can swap your Pacific Avenue hotel with your PA houses')
        return False

    
can_place_hotel_on_penn_avenue()