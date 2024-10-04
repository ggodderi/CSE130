# Python

import json

# This program will implement the advanced search for CSE 130


# A list of words to test with
word_array = ['Adam', 'Bob', 'Charlie', 'Doug', 'Elle', 'Frank', 'Guy', 'Henry', 'Igor', 'James', 'Kim', 'Larry', 'Miney', 'Nancy', 'Oscar',\
    'Penelopy', 'Quinn', 'Rob', 'Sam', 'Terry', 'Uche', 'Velinda', 'Wally', 'Xan', 'Yellan', 'Zack']

# Convert to dictionary so may be saved as JSON file.
data_dictionary = {
    'data_array' : word_array
}

# Save the data_array as a json file
def save_to_file(data_array):
    assert type(data_array) == dict

    with open('AdvancedSearch.json', "w") as file_handle:
        json_string = json.dumps(data_dictionary)
        file_handle.write(json_string)

# Open the given file name and return the data_array
def read_file(file_name):
    with open(file_name, "r") as file_handle:
        json_string = file_handle.read()

    json_dictionary = json.loads(json_string)
    return (json_dictionary['data_array'])

# Use the advanced search algorithm to find a word in a given list of words.
def advanced_search(data_array, search_word):
    assert type(data_array) == list

    # Local variables
    num_tries = 0
    found = False
    location = 0

    # Indexes used to search the array
    istart = 0
    iend = len(data_array) - 1

    # Trace Table
    print(f'Header: {"start":>10} {"center":>10} {"end":>10}  {"found":>10} {"searches":>10}')

    # Loop until the word is found or not found
    while istart <= iend and not found:

        # Find the center of the array
        icenter = (istart + iend) // 2
        num_tries += 1

        # Trace Table
        print(f'Line 1: {istart:10} {icenter:10} {iend: 10} {found:10} {num_tries:10}')

        # Exit the search if the word is found.
        if search_word == data_array[icenter]:
            found = True
            location = icenter
        # The word is in the lower half of the array, therefore update the iend.
        elif search_word < data_array[icenter]:
            iend = icenter - 1
        # The word is in the upper half of the array, therefore update the istart
        elif search_word > data_array[icenter]:
            istart = icenter + 1
        else:
            assert False   ## SHould never get here

        # Trace Table
        print(f'Line 2: {istart:10} {icenter:10} {iend: 10} {found:10} {num_tries:10}')
    

    # Trace Table
    print(f'Line 3: {istart:10} {icenter:10} {iend: 10} {found:10} {num_tries:10}')
    # The word was found state so, otherwise state not found.
    if found:
        print(f'The word: {search_word} was found in the list at position {location} in {num_tries} searches.')
    else:
        print(f'The word: {search_word} was not found in the list.  {num_tries} searches were executed.')
    
    return found


# save_to_file(word_array)

# Prompt the user for the file name.
file_name = input('Input the file name for the word array: ')

# Get the data_array from the file
data_array = read_file(file_name)

# TESTING - search for each word in the array.
for word in data_array:
    assert(advanced_search(data_array, word) == True)

# Try some words that are not in the array.
assert(advanced_search(data_array, 'aaaa') == False)
assert(advanced_search(data_array, 'zzzz') == False)
assert(advanced_search(data_array, 'eeee') == False)
assert(advanced_search(data_array, 'ssss') == False)

# Allow the user to search for words
searching = True
while searching:
    search_word = input('For which word do you wish to search (q to quit)? ')
    if search_word.lower() != 'q':
        advanced_search(data_array, search_word)
    else:
        searching = False