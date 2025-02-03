# Python 
# Json example

import json

my_data = {
    'Name':'Jeanny Bob',
    'Address': '555 Cherry Lane',
    'Phone': '8675309',
    'Email' : 'jeannybob@mns.com'
}


with open('JSONExample7.json', "wt") as filehandle:
    json_string = json.dumps(my_data)
    print(json_string)
    filehandle.write(json_string)


with open('JSONExample7.json', 'rt') as filehandle:
    data = filehandle.read()
    data_dictionary = json.loads(data)
    print(data_dictionary['Name'])
    print(data_dictionary)

with open('JSONExample7s.json', "wt") as filehandle:
    json.dump(my_data, filehandle)


with open('JSONExample7s.json', 'rt') as filehandle:
    data_dictionary = json.load(filehandle)
    print(data_dictionary['Name'])
    print(data_dictionary)

with open('Lab02.json', 'rt') as filehandle:
    data_dictionary = json.load(filehandle)
    print(data_dictionary['username'])
    print(data_dictionary['password'])
