# Python

import json
# This file tests a json example

test_dictionary = {
    1:"This is object 1",
    2:"This is item 2",
    "age":98,
    "name":"bob",
    'city':"Paris"
}

print(test_dictionary[1])
print(test_dictionary[2])
print(test_dictionary['age'])
print(test_dictionary['name'])
print(test_dictionary['city'])


text_json = json.dumps(test_dictionary)
print(text_json, type(text_json))
with open("JSONExample.json", "w") as file_handle:
    file_handle.write(text_json)


with open('JSONExample.json', "r") as file_handle:
    file_text = file_handle.read()
    text_json = json.loads(file_text)
    print(text_json['1'])
    print(type(text_json))
