# # Python
import string


def count_number_of_substrings(search_string, sub_string):
    '''This function will count the number of times the sub_string is 
    found in the search_string.
    It will return the number of times the sub_string is found'''

    # Setup indexes, lengths, and a count
    sub_string_count = 0
    search_string_index = 0
    search_string_length = len(search_string)
    sub_string_index = 0
    sub_string_length = len(sub_string)

    algorithm_count = 0

    assert sub_string_length > 0
    assert search_string_length > 0

    # Search the entire search_string for a sub_string
    while search_string_index < search_string_length:
        algorithm_count += 1
        # If the first character of the sub_string is found, search for the rest of the string
        if sub_string[sub_string_index] == search_string[search_string_index]:

            # Search for rest of sub_string
            # Important! the index < lenght MUST be checked first or will get index out of range
            while sub_string_index < sub_string_length and \
                sub_string[sub_string_index] == search_string[search_string_index]:
                sub_string_index += 1
                search_string_index += 1
                algorithm_count += 1

            # If the entire sub_string was searched, it was found            
            if sub_string_index == sub_string_length:
                sub_string_count += 1
            
            # Reset the index so we can check for the next occurance of the sub_string
            sub_string_index = 0

        search_string_index += 1
    
    print(f'N: {search_string_length}, count is: {algorithm_count}')
    return sub_string_count


def main():
    main_string = 'This is a test string'
    sub_string = 'is'
    substring_count = count_number_of_substrings(main_string, sub_string)
    print(f'The number of: "{sub_string}" in "{main_string}" is: {substring_count}')

    main_string = 'This is a test string'
    sub_string = 'a'
    substring_count = count_number_of_substrings(main_string, sub_string)
    print(f'The number of: "{sub_string}" in "{main_string}" is: {substring_count}')

    main_string = '''35 Yea, I know that God will give liberally to him that asketh. 
    Yea, my God will give me, if I ask not amiss; therefore I will lift up my voice unto thee; 
    yea, I will cry unto thee, my God, the rock of my righteousness. 
    Behold, my voice shall forever ascend up unto thee, my rock and mine everlasting God. Amen.'''
    sub_string = 'th'
    substring_count = count_number_of_substrings(main_string, sub_string)
    print(f'The number of: "{sub_string}" in "{main_string}" is: {substring_count}')

main()