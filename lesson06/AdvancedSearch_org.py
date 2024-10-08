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
    done = False
    location = 0

    # Indexes used to search the array
    istart = 0
    iend = len(data_array)
    
    # Let the user know what we are searching for
    #print(f'Searching for {search_word}')

    # Do all comparisons in lower case
    search_word = search_word.lower()


    # Loop until the word is found or not found
    while not done:

        # Find the center of the array
        icenter = (istart + iend) // 2
        #print(istart, icenter, iend)
        num_tries += 1

        # Exit the search if the word is found.
        if search_word == data_array[icenter].lower():
            found = True
            done = True
            location = data_array.index(search_word.title())
        
        # The word is in the lower half of the array, therefore update the iend.
        elif search_word < data_array[icenter].lower():
            iend = icenter - 1
        # The word is in the upper half of the array, therefore update the istart
        elif search_word > data_array[icenter].lower():
            istart = icenter + 1
        else:
            assert False   ## SHould never get here

        # Check to see if the word was not found.
        if iend < istart or istart >= len(data_array):
            #print(f'Ending . . . Length is: {len(data_array)}')
            done = True
    
    # The word was found state so, otherwise state not found.
    if found:
        print(f'The word: {search_word} was found in the list at position {location} in {num_tries} number of searches.')
        #print(istart, icenter, iend)
    else:
        print(f'The word: {search_word} was not found in the list.  {num_tries} searches were executed.')
        #print(istart, iend, icenter)
    


# save_to_file(word_array)

# Prompt the user for the file name.
file_name = input('Input the file name for the word array: ')

# Get the data_array from the file
data_array = read_file(file_name)

# TESTING - search for each word in the array.
for word in data_array:
    advanced_search(data_array, word)

# advanced_search(data_array, 'Adam')
# advanced_search(data_array, 'Bob')
# advanced_search(data_array, 'Charlie')
# advanced_search(data_array, 'Doug')
# advanced_search(data_array, 'Elle')
# advanced_search(data_array, 'Frank')
# advanced_search(data_array, 'Guy')
# advanced_search(data_array, 'Henry')
# advanced_search(data_array, 'Igor')
# advanced_search(data_array, 'James')
# advanced_search(data_array, 'Kim')
# advanced_search(data_array, 'Larry')
# advanced_search(data_array, 'Miney')
# advanced_search(data_array, 'Nancy')
# advanced_search(data_array, 'Oscar')
# advanced_search(data_array, 'Penelopy')
# advanced_search(data_array, 'Quinn')
# advanced_search(data_array, 'Rob')
# advanced_search(data_array, 'Sam')
# advanced_search(data_array, 'Terry')
# advanced_search(data_array, 'Uche')
# advanced_search(data_array, 'Velinda')
# advanced_search(data_array, 'Wally')
# advanced_search(data_array, 'Xan')
# advanced_search(data_array, 'Yellan')
# advanced_search(data_array, 'Zack')


# Try some words that are not in the array.
advanced_search(data_array, 'aaaa')
advanced_search(data_array, 'zzzz')
advanced_search(data_array, 'eeee')

# Allow the user to search for a word
# search_word = input('For which word do you wish to search? ')

# advanced_search(data_array, search_word)


searching = True
while searching:
    search_word = input('For which word do you wish to search (q to quit)? ')
    if search_word.lower() != 'q':
        advanced_search(data_array, search_word)
    else:
        searching = False