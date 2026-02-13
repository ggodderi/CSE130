import json

my_friend = {
    "Name" : "Jeannie",
    "Phone" : 8675309,
    "Address" : "555 Cherry Lane",
    "Friends" : ['Bob', 'Betty', 'Bubba', 'Alice']
}

print(my_friend)

print(my_friend['Name'])


with open('JSONExample9.json', 'wt') as file_handle:
    json_data = json.dumps(my_friend)
    print(json_data)
    file_handle.write(json_data)
    # json.dump(my_friend, file_handle)

    # data = file_handle.read()

with open('JSONExample9.json', 'rt') as file_handle:
    # json_data = file_handle.read()
    # my_dictionary = json.loads(json_data)
    my_dictionary = json.load(file_handle)
    print(my_dictionary['Friends'])
    

