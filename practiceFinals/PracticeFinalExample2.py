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

def prompt_user_for_dates():
    '''Ask the user for the birth date and the death dates
       Then return those two dates.
       Dates are a List: [day, month, year]'''
    
    birth_date = get_date('Birth Date')
    death_date = get_date('Death Date')
    #print(birth_date)
    #print(death_date)

    return birth_date, death_date

def days_in_a_month(month):
    '''Return the number of days in a given month
       Client sends in a month 1-12'''
                        #    1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12
    days_in_a_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_a_month_list[month - 1]


def calculate_days_from_a_partial_year(birth_date, death_date):
    '''Calculate the number of days between two days within the same year'''

    if birth_date[MONTH] == death_date[MONTH]:
        total_days = death_date[DAY] - birth_date[DAY]
    else:
        total_days = days_in_a_month(birth_date[MONTH]) - birth_date[DAY]
        total_days += death_date[DAY]

        if birth_date[MONTH] <= 2 and death_date[MONTH] >= 2 and is_leap_year(birth_date[YEAR]):
            total_days += 1
            
        for month in range(birth_date[MONTH] + 1, death_date[MONTH], 1):
            total_days += days_in_a_month(month)
                
    return total_days

def calculate_days_from_birth_to_end_of_year(birth_date, year):
    '''Calulate the number of days from birth date until the end of the year'''
    total_days = days_in_a_month(birth_date[MONTH]) - birth_date[DAY] 
    if birth_date[MONTH] <= 2 and is_leap_year(year):
         total_days += 1
        
    if birth_date[MONTH] != 12:
        for month in range(birth_date[MONTH] + 1, 13, 1):
            total_days += days_in_a_month(month)
            
    return total_days

def calculate_days_from_jan1_to_death(death_date, year):
    '''Calculate the number of days from january 1st to the death date'''
    total_days = death_date[DAY]
    if death_date[MONTH] >= 2 and is_leap_year(year):
        total_days += 1
    if death_date[MONTH] != 1:
        for month in range(1, death_date[MONTH], 1):
            total_days += days_in_a_month(month)

    return total_days

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
        # total_days += calculate_days_from_birth_to_end_of_year(birth_date, birth_date[YEAR])
        # total_days += calculate_days_from_jan1_to_death(death_date, death_date[YEAR])
        total_days += calculate_days_from_a_partial_year(birth_date, [31, 12, birth_date[YEAR]])
        total_days += calculate_days_from_a_partial_year([1, 1, death_date[YEAR]], death_date)

    # Born and died in the same year
    elif death_date[YEAR] == birth_date[YEAR]:
        
        # Did not die in the same month
        if death_date[MONTH] >= birth_date[MONTH] + 1:
            total_days += calculate_days_from_a_partial_year(birth_date, death_date)
            # total_days += death_date[DAY]
            # total_days += days_in_a_month(birth_date[MONTH]) - birth_date[DAY]
            # for month in range(birth_date[MONTH] + 1, death_date[MONTH], 1):
            #     total_days += days_in_a_month(month)
            #     if month == 2 and is_leap_year(year):
            #         total_days += 1
        
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

