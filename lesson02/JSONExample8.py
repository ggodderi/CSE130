# 
import json

my_friend = {"Name" : "Jeannie", 
             "Phone": "8675309", 
             "Address" : "555 Cherry Lane", 
             "Email" : "jeannielucas@gmail.com"}

# print(my_friend)

with open('JSONExample8.json', "wt") as filehandle:
    # data_json = json.dumps(my_friend)
    # print(data_json)
    # filehandle.write(data_dictionary)
    json.dump(my_friend, filehandle)

with open('JSONExample8.json', "rt") as filehandle:
    # data = filehandle.read()
    # # print(data)
    # data_dictionary = json.loads(data)
    data_dictionary = json.load(filehandle)
    print(data_dictionary['Name'])
    print(data_dictionary['Phone'])