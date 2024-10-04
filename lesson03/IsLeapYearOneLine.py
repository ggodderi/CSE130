# Python

# Test is_leap_year one line function:

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


print(f'2000 is a leap year: {is_leap_year(2000)}')
print(f'1800 is a leap year: {is_leap_year(1800)}')
print(f'1900 is a leap year: {is_leap_year(1900)}')
print(f'2004 is a leap year: {is_leap_year(2004)}')
print(f'1984 is a leap year: {is_leap_year(1984)}')
print(f'2100 is a leap year: {is_leap_year(2100)}')
print(f'2003 is a leap year: {is_leap_year(2003)}')
