# Python

# This program will test writing and reading JSON data.
import json
test_dictionary = {
    'Name' : 'Uncle Bob',
    'Age' : 57,
    'Home': 'Rockport',
    'Hobby1': 'Rock Climbing'
}

# print (test_dictionary)
# print(test_dictionary['Home'])

# for key in test_dictionary.keys():
#     print(test_dictionary[key])

print(test_dictionary)
print(type(test_dictionary))
test_text = json.dumps(test_dictionary)
print(test_text)
print(type(test_text))
print(test_text[0])

for letter in test_text:
    print(letter, end = ' ')

print()


with open('JSONExample5.json', 'w') as file_handle:
    file_handle.write(test_text)


with open('JSONExample5.json', 'r') as file_handle:
    data_text = file_handle.read()
    print(data_text)
    print(type(data_text))
    data_dictionary = json.loads(data_text)
    print(data_dictionary)
    print(type(data_dictionary))

    print(data_dictionary['Name'])

