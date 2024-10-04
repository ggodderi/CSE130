# Python

import json

# Open the given file name and return the data_array
def read_file(file_name):
    try:
        with open(file_name, "r") as file_handle:
            json_string = file_handle.read()

        json_dictionary = json.loads(json_string)
        return (json_dictionary['data_array'])
    except:
        print('Invalid file name')
        return []

# Receive a list of unsorted items and sort them.
# This uses the "sort-algorithm" from CSE 130, lesson 07
# Note:  This will work with any sortable data type
def sort_word_list(data_list):

    # set pivot and largest at the end of the list
    i_pivot = len(data_list) - 1
    i_largest = i_pivot
    counter = 0

    # Loop through the entire list
    while i_pivot >= 0:

        # check will start one less than pivot and move to the left
        for i_check in range(i_pivot-1, -1, -1):
            counter += 1
            if data_list[i_check] > data_list[i_largest]:
                i_largest = i_check
        
        # Python trick - swap pivot and largest
        if data_list[i_largest] > data_list[i_pivot]:
            (data_list[i_pivot], data_list[i_largest]) = (data_list[i_largest], data_list[i_pivot])
    
        # Move pivot and largest back to the left by 1
        i_pivot -= 1
        i_largest = i_pivot

    print(f'Length: {len(data_list)}, loop counts: {counter}')

# Main function for convience
def main():

    file_name = input('Please input the name of the file containing the unsorted list of items: ')
    # read the word list
    data_list = read_file(file_name)

    if len(data_list) > 0:
        print(data_list)

        # Sort the words and print out the sorted list.
        sort_word_list(data_list)
        print(data_list)

main()