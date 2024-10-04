# Python

# This program will test writing and reading JSON data.
import json
test_dictionary = {
    'Name' : 'Uncle Bob',
    'Age' : 57,
    'Home': 'Rockport',
    'Hobby1': 'Rock Climbing'
}

with open('JSONExample4.json', 'w') as file_handle:
    json_data = json.dumps(test_dictionary)
    print(type(json_data))
    file_handle.write(json_data)


with open('JSONExample4.json', 'r') as file_handle:
    text_string = file_handle.read()
    json_dictionary = json.loads(text_string)

    print(json_dictionary['Name'])
    print(json_dictionary)
    print(json_dictionary['Age'])