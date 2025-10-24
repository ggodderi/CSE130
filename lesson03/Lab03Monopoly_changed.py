#!/usr/bin/env python3
"""Lab03Monopoly - validated and refactored version for creating a hotel on Penn Avenue."""

HOUSE_COST = 200

def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ('y', 'n'):
            return ans
        print("Please enter 'y' or 'n'.")

def get_int_in_range(prompt, min_v, max_v):
    while True:
        try:
            v = int(input(prompt))
            if min_v <= v <= max_v:
                return v
            print(f"Please enter an integer between {min_v} and {max_v}.")
        except ValueError:
            print("Please enter a valid integer.")

def get_nonneg_int(prompt):
    while True:
        try:
            v = int(input(prompt))
            if v >= 0:
                return v
            print("Please enter a non-negative integer.")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    # Ownership
    own = get_yes_no('Do you own all three of the green (Pacific, Penn, and NC) properties (y/n)? ')
    if own == 'n':
        print('You must own all three green properties to be able to place a hotel on Penn Avenue.')
        return

    # Status inputs (0..5 where 5 means a hotel)
    pa_status = get_int_in_range('What is on Penn Avenue (0: nothing, 1-4: houses, 5: hotel): ', 0, 5)
    if pa_status == 5:
        print('Penn Avenue already has a hotel, no need to buy one.')
        return

    nc_status = get_int_in_range('What is on North Carolina (0: nothing, 1-4: houses, 5: hotel): ', 0, 5)
    pc_status = get_int_in_range('What is on Pacific Avenue (0: nothing, 1-4: houses, 5: hotel): ', 0, 5)

    # Handle other hotels and possible swap
    other_with_hotel = []
    if nc_status == 5:
        other_with_hotel.append('North Carolina')
    if pc_status == 5:
        other_with_hotel.append('Pacific Avenue')

    if other_with_hotel:
        names = ' and '.join(other_with_hotel)
        if pa_status == 4:
            print(f'You can swap your {names} hotel(s) with your PA houses')
            return
        else:
            print(f'Another property ({names}) already has a hotel. You must have 4 houses on Penn Avenue to swap; cannot proceed.')
            return

    # Houses needed to bring each property to 4 houses
    pa_needed = 4 - pa_status
    pc_needed = 4 - pc_status
    nc_needed = 4 - nc_status
    total_houses_needed = pa_needed + pc_needed + nc_needed

    houses_available = get_nonneg_int('How many houses are there available? ')
    if houses_available < total_houses_needed:
        print(f'There are not enough houses available. You need {total_houses_needed} and there are only {houses_available} available')
        return

    hotels_available = get_nonneg_int('How many hotels are there available? ')
    if hotels_available < 1:
        print(f'There are not enough hotels available. You need 1 hotel and there are only {hotels_available} available')
        return

    cash_needed = (total_houses_needed + 1) * HOUSE_COST
    cash_on_hand = get_nonneg_int('How much cash do you have? ')
    if cash_on_hand < cash_needed:
        print(f'You do not have enough cash to purchase the hotel. You need ${cash_needed} and you only have ${cash_on_hand}')
        return

    # Success: print instructions
    print()
    print('Congratulations - you can purchase a hotel.\n')
    print(f'This will cost: ${cash_needed}')
    print(f'Purchase 1 hotel and {total_houses_needed} houses')
    print(f'{pa_needed} houses needed for PA, then put 1 hotel on Penn Avenue')
    print('Return all PA houses to the bank')

    if pc_needed > 0:
        print(f'Put {pc_needed} house{"s" if pc_needed != 1 else ""} on Pacific Avenue.')
    if nc_needed > 0:
        print(f'Put {nc_needed} house{"s" if nc_needed != 1 else ""} on North Carolina.')

if __name__ == '__main__':
    main()