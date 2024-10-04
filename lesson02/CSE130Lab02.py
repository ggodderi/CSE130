# Python
import json

# This document implements the CSE 130 Lab 02.

def read_data_from_file(file_name):
    try:
        file_handle = open(file_name, "r")
        data = file_handle.read()
        #print(data)
        return data
    except:
        print(f'Error:  Not able to open {file_name}')
        return ''


file_data = read_data_from_file('Lab02.json')

# Convert the data to a dictionary
json_data = json.loads(file_data)

# Obtain the username and password lists from the dictionary
user_names = json_data['username']
passwords = json_data['password']

print(user_names)
print(passwords)

user_name = input('user name: ')
password = input('Password: ')

user_index = -1
user_found = False
for index, name in enumerate(user_names):
    print(index, name)
    if user_name == name:
        user_index = index
        user_found = True

if not user_found:
    print('User Not Found: NOT Authenticated')
elif user_found and password == passwords[user_index]:
    print('Authenticated')
else:
    print('Incorrect Password: NOT Authenticated')


# user_index = user_names.index(user_name)
# password_index = passwords.index(password)

# if password_index == user_index:
#     print('By Index: Authenticated')
# else:
#     print('By Index: Incorrect Password: NOT Authenticated')


count = 0
for name in user_names:
    if name == user_name:
        user_found = True
        user_index = count
    
    count += 1

if not user_found:
    print('User Not Found: NOT Authenticated')
elif user_found and password == passwords[user_index]:
    print('Authenticated')
else:
    print('Incorrect Password: NOT Authenticated')

