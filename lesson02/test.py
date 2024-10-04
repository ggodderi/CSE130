

test_string = 'ABCDEFGHIMJKL'

string1 = test_string[5:8]
print(string1)
string2 = test_string[8:5]
print(f'The value of string2 is: {string2}')
string3 = test_string[:3]
print(string3)


# This is a comment

'''This is a multiline
comment
that goes long
'''


tuple_one = 1, 1.1
tuple_two = (2, 2.2)

print(tuple_one, tuple_two)
print(tuple_one[0], tuple_two[1])

from datetime import datetime

today = datetime.now()
print(today)
year = today.year
print(year)
month = today.month
day = today.day
print(month, day)
hour = today.hour
minute = today.minute
second = today.second
microsecond = today.microsecond
print(hour, minute, second, microsecond)

birth_year = int(input('What year were you born? '))
age = year - birth_year
print(f'This year you will turn {age} years old.')