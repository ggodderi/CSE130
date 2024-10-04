# Python

DAY_INDEX = 0
MONTH_INDEX = 1
YEAR_INDEX = 2


def get_int_input_value(min, max, message):
    '''Return an integer value that is between min and max.
    Display the message from the caller as part of the input.'''

    assert type(min) == type(1)
    assert type(max) == type(1)
    assert type(message) == type('')
    assert min <= max
    assert min > 0
    assert max > 0
    
    received_correct_input = False
    
    while not received_correct_input:
        try:
            value = int(input(message))

            if value < min or value > max:
                print(f'{value} is invalid - value must be between: {min} and {max}')
            else:
                received_correct_input = True
        except ValueError as ve:
            print(f'Invalid input - must input an integer.  Error message {ve}')    
    assert min <= value <= max
    return value

def is_leap_year(year):
    '''Return true if year is a leap year'''

    assert year > 1752
    
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def validate_dates(start_date, end_date):
    '''Make sure start_date <= end_date'''

    assert len(start_date) == 3
    assert len(end_date) == 3
    assert len(start_date) == len (end_date)
    assert type(start_date[DAY_INDEX]) == type(1)
    assert type(start_date[MONTH_INDEX]) == type(1)
    assert type(start_date[YEAR_INDEX]) == type(1)
    assert type(end_date[DAY_INDEX]) == type(1)
    assert type(end_date[MONTH_INDEX]) == type(1)
    assert type(end_date[YEAR_INDEX]) == type(1)

    # Start year must be <= end year
    if start_date[YEAR_INDEX] > end_date[YEAR_INDEX]:
        return False
    # if the years are the same, the start month <= end month
    elif start_date[YEAR_INDEX] == end_date[YEAR_INDEX] and \
         start_date[MONTH_INDEX] > end_date[MONTH_INDEX]:
            return False
    # if the year and month are the same, then the start day <= end day
    elif start_date[YEAR_INDEX] == end_date[YEAR_INDEX] and \
         start_date[MONTH_INDEX] == end_date[MONTH_INDEX] and \
         start_date[DAY_INDEX] > end_date[DAY_INDEX]:
         return False
    
    assert start_date[YEAR_INDEX] <= end_date[YEAR_INDEX]
    
    return True

def get_dates():
    '''Ask the user for valid start and end date.  Loop until 
    valid dates are received.'''
     
    received_valid_dates = False

    while not received_valid_dates:

        # Get the Start day
        start_day = get_int_input_value(1, 31, "Input Start Day: ")
        start_month = get_int_input_value(1, 12, "Input Start Month: ")
        start_year = get_int_input_value(1753, 9999999, "Input Start Year: ")

        start_date = (start_day, start_month, start_year)

        # Get the end day
        end_day = get_int_input_value(1, 31, "Input End Day: ")
        end_month = get_int_input_value(1, 12, "Input End Month: ")
        end_year = get_int_input_value(1753, 9999999, "Input End Year: ")
        end_date = (end_day, end_month, end_year)
        
        received_valid_dates = validate_dates(start_date, end_date)
        if not received_valid_dates:
            print(f'dates are invalid:  Start date: {start_date}, end date: {end_date}')

    return start_date, end_date

def days_in_month(month, year):
    '''Return the number of days in a month - include 29 days for february on leap years.'''
    month -= 1 # In this function, months are 0 to 11.
    #             J   F   M   A   M   J   J   A   S   O   N   C
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    assert month >= 0 and month <= 11
    assert year > 1752
    leap_year_add = 0
    
    # add one day to the month of february for leap years
    if is_leap_year(year) and month == 1:
        leap_year_add += 1
    return month_days[month] + leap_year_add


def calculate_days_partial_year(start_month, end_month, year):
    '''Calculate the number of days from the start month to the end month (inclusive)
    of the specified year.'''
    number_of_days = 0
    assert start_month >= 1 and start_month <= 12
    assert end_month >= 1 and end_month <= 12
    assert start_month <= end_month

    for month in range(start_month, end_month + 1, 1):
        number_of_days += days_in_month(month, year)
    assert number_of_days >= 0
    return number_of_days


def calculate_number_of_days(start_date, end_date):
    '''Calculate the number of days between the start_date and the end_date.'''

    assert validate_dates(start_date, end_date) == True

    # From the same month
    if start_date[YEAR_INDEX] == end_date[YEAR_INDEX] and \
       start_date[MONTH_INDEX] == end_date[MONTH_INDEX]:
        number_of_days = end_date[DAY_INDEX] - start_date[DAY_INDEX]
    # From the same year
    elif start_date[YEAR_INDEX] == end_date[YEAR_INDEX]:
        number_of_days = days_in_month(start_date[MONTH_INDEX], start_date[YEAR_INDEX]) - start_date[DAY_INDEX]
        number_of_days += calculate_days_partial_year(start_date[MONTH_INDEX] + 1, end_date[MONTH_INDEX] - 1,\
                                                      start_date[YEAR_INDEX])
        number_of_days += end_date[DAY_INDEX]
    # Different years
    else:
        # Days from starting year:
        number_of_days = days_in_month(start_date[MONTH_INDEX], start_date[YEAR_INDEX]) - start_date[DAY_INDEX]
        number_of_days += calculate_days_partial_year(start_date[MONTH_INDEX] + 1, 12, start_date[YEAR_INDEX])

        # Days from the full years
        for year in range(start_date[YEAR_INDEX] + 1, end_date[YEAR_INDEX], 1):
            number_of_days += 365
            if is_leap_year(year):
                number_of_days += 1
        
        # Days from ending year
        number_of_days += calculate_days_partial_year(1, end_date[MONTH_INDEX], end_date[YEAR_INDEX])
        number_of_days += end_date[DAY_INDEX]
    
    assert number_of_days >= 0
    return number_of_days



def main():
    '''Main Program - get the start and end dates and display the number of days between.'''
    start_date, end_date = get_dates()

    print(f'The start date is: {start_date[DAY_INDEX]}/{start_date[MONTH_INDEX]}/{start_date[YEAR_INDEX]}')
    print(f'The start date is: {end_date[DAY_INDEX]}/{end_date[MONTH_INDEX]}/{end_date[YEAR_INDEX]}')

    number_of_days = calculate_number_of_days(start_date, end_date)
    print(f'The number of days between: {start_date} and {end_date} is: {number_of_days}')

main()