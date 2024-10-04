# Python

import json

def read_file(file_name):
    ''' Open the given file name and return the data_array '''
    try:
        assert file_name != None
        #with open(file_name, "r") as file_handle:
        file_handle = open(file_name, 'r')
        #print(file_handle)
        #print('Open Succeeded')
        json_string = file_handle.read()
        assert json_string != None
        #print('Read Succeeded')
        #print(json_string)

        json_dictionary = json.loads(json_string)
        assert json_dictionary != None
        return (json_dictionary['data_array'])
    except:
        print(Exception)
        print('Invalid file name')
        return []

def sort_word_list(data_list):
    ''' Receive a list of unsorted items and sort them.
        This uses the "sort-algorithm" from CSE 130, lesson 07
        Note:  This will work with any sortable data type '''

    assert len(data_list) >= 0

    # set pivot and largest at the end of the list
    i_pivot = len(data_list) - 1
    i_largest = i_pivot
    iterations = 0

    # Loop through the entire list
    while i_pivot >= 1:
        assert 0 <= i_pivot <= len(data_list) - 1

        # check will start one less than pivot and move to the left
        for i_check in range(i_pivot-1, -1, -1):
            assert 0 <= i_check <= i_pivot
        #for i_check in range(1, i_pivot):
            iterations += 1
            assert type(data_list[i_check] == type(data_list[i_largest]))
            if data_list[i_check] > data_list[i_largest]:
                i_largest = i_check
                assert 0 <= i_largest <= i_pivot
        
        # Python trick - swap pivot and largest
        if data_list[i_largest] > data_list[i_pivot]:
            assert type(data_list[i_pivot] == type(data_list[i_largest]))
            (data_list[i_pivot], data_list[i_largest]) = (data_list[i_largest], data_list[i_pivot])
    
        # Move pivot and largest back to the left by 1
        i_pivot -= 1
        assert i_pivot >= 0
        i_largest = i_pivot

    print(f'Length: {len(data_list)}, iterations: {iterations}')

def test_sort_word_list():
    ''' Test Driver function to test sort_word_list '''

    # Test file names.
    test_file_names = ['Lab08.empty.json', 
                       'Lab08.trivial.json',
                       'Lab08.languages.json', 
                       'Lab08.states.json', 
                       'Lab08.cities.json'] 

    # Loop through each test file, asking the user to continue.
    for file_name in test_file_names:
        print(f'Testing {file_name}')
        word_list = read_file(file_name)

        assert len(word_list) >= 0
        print(word_list)
        print()

        sort_word_list(word_list)
        assert len(word_list) >= 0
        print(word_list)

        # Traverse the entire list to make sure the list is in order.
        for index in range(1, len(word_list)):
            assert(word_list[index-1] < word_list[index])

        response = input('Press enter to continue . . . ')
        print('\n\n\n\n')



def main():
    ''' Main function for convience '''

    # Run automated tests
    run_automated_tests = input('Would you like to run the automated tests (y/n)?: ')
    if run_automated_tests.lower() == 'y':
        test_sort_word_list()

    file_name = input('Please input the name of the file containing the unsorted list of items: ')
    # read the word list
    data_list = read_file(file_name)

    if len(data_list) > 0:
        print(data_list)

        # Sort the words and print out the sorted list.
        sort_word_list(data_list)
        print(data_list)

         # Traverse the entire list to make sure the list is in order.
        for index in range(1, len(data_list)):
            assert(data_list[index-1] <= data_list[index])

main()