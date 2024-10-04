# Python

# This program will test writing and reading JSON data.
import json
test_dictionary = {
    'Name' : 'Uncle Bob',
    'Age' : 57,
    'Home': 'Rockport',
    'Hobby1': 'Rock Climbing'
}



with open('JSONExample6.json', 'w') as file_handle:
    json.dump(test_dictionary, file_handle)


with open('JSONExample5.json', 'r') as file_handle:
    data_dictionary = json.load(file_handle)
    print(data_dictionary)
    print(type(data_dictionary))

    print(data_dictionary['Name'])

