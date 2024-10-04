# Python

# This file will implement the solution to the second practice final
# for CSE 130.  This is the number of days between birth and death days

# The date is a list with the format of: [Day, Month, Year]

DAY = 0
MONTH = 1
YEAR = 2

def get_date(date_string):
    '''Ask the user for a Day, Month, and Year of the "date_string"
       Return a list of: [Day, Month, Year]'''
    day_list = []
    day_list.append(int(input(f'Input the {date_string} day (1-31):  ')))
    day_list.append(int(input(f'Input the {date_string} month (1-12): ')))
    day_list.append(int(input(f'Input the {date_string} year (YYYY): ')))

    return day_list

def valid_dates(birth_date, death_date):
    '''Ensure dates are correct - Death date >= Birth Date '''
    if death_date[YEAR] < birth_date[YEAR]:
        return False
    elif birth_date[YEAR] == death_date[YEAR]:
        if death_date[MONTH] < birth_date[MONTH]:
            return False
        elif birth_date[MONTH] == death_date[MONTH]:
            if death_date[DAY] < birth_date[DAY]:
                return False
            
    return True

def prompt_user_for_dates():
    '''Ask the user for the birth date and the death date
       Then return those two dates.
       Dates are a List: [day, month, year]'''
    
    done = False

    # Loop until the user enters valid dates (i.e., birth date <= death date)
    while not done:
        birth_date = get_date('Birth Date')
        death_date = get_date('Death Date')

        if not valid_dates(birth_date, death_date):
            print('\n\nDates are invalid, please enter valid dates: \n\n')
        else:
            done = True

    return birth_date, death_date

def is_leap_year(year):
    '''Return True if a year is a leap year'''
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def days_in_a_month(month):
    '''Return the number of days in a given month
       Client sends in a month 1-12'''

    assert 1<= month <= 12

                        #    1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12
    days_in_a_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_a_month_list[month - 1]


def calculate_days_from_a_partial_year(start_date, end_date):
    '''Calculate the number of days between two days within the same year'''

    # Start and end in the same month
    if start_date[MONTH] == end_date[MONTH]:
        total_days = end_date[DAY] - start_date[DAY]
    else:
        # Add in the days from the start month and end month
        total_days = days_in_a_month(start_date[MONTH]) - start_date[DAY]
        total_days += end_date[DAY]

        # Handle leap year case
        if start_date[MONTH] <= 2 and end_date[MONTH] > 2 and is_leap_year(start_date[YEAR]):
            total_days += 1
            
        # Finally - add in the days from each of the full months
        for month in range(start_date[MONTH] + 1, end_date[MONTH], 1):
            total_days += days_in_a_month(month)
                
    return total_days



def calculate_days_between_dates(birth_date, death_date):
    '''Calulate the number of days between the birth and death dates'''
    
    total_days = 0

    # Did not die in the same year as was born
    if death_date[YEAR] >= birth_date[YEAR] + 1:
        # Calculate days from the full years
        for year in range(birth_date[YEAR] + 1, death_date[YEAR], 1):
            total_days += 365
            if is_leap_year(year):
                total_days += 1
            
        # Add in the days from the two parital years
        total_days += calculate_days_from_a_partial_year(birth_date, [31, 12, birth_date[YEAR]])
        total_days += calculate_days_from_a_partial_year([1, 1, death_date[YEAR]], death_date)

    # Born and died in the same year
    elif death_date[YEAR] == birth_date[YEAR]:
        
        # Did not die in the same month
        if death_date[MONTH] >= birth_date[MONTH] + 1:
            total_days += calculate_days_from_a_partial_year(birth_date, death_date)
        
        # Born and died the same month
        elif death_date[MONTH] == birth_date[MONTH]:
            total_days = death_date[DAY] - birth_date[DAY]
        
        # Should never happen
        else:
            assert False
    # Should never happen
    else:
        assert False
    
    return total_days

birth_date, death_date = prompt_user_for_dates()
print(birth_date)
print(death_date)

total_days = calculate_days_between_dates(birth_date, death_date)
print(f'The total days between: {birth_date}, and {death_date}, is: {total_days}')

