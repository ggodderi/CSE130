# Python

# This program will implement the solution to the CSE 130 winter 2023 final

import json

def get_filename():
    '''Return the name of the input file'''
    return 'WinterFinalInputData.json'

def read_file_data(filename):
    '''Open the provided file name, read its contents, and return the contents'''
    assert filename != ''
    with open(filename, "r") as file_handle:
        data = file_handle.read()
        json_data = json.loads(data)
        attendee_list = json_data['attendee_list']
    
    assert len(attendee_list) != 0
    return attendee_list

def write_file_data(filename, attendee_list):
    '''Output the data in attendee_list to the file specified by filename'''
    assert filename != ''
    assert type(filename) == type('')
    assert len(attendee_list) != 0
    with open(filename, "w") as file_handle:
        attendee_dictionary = {'attendee_list': attendee_list}
        json_data = json.dumps(attendee_dictionary)
        file_handle.write(json_data)
    
    return attendee_list

def remove_duplicate_names(attendee_list):
    '''Loop though all of the names in attendee_list and remove all of
       the duplicates.'''
    assert attendee_list != ''
    assert attendee_list != None
    length = len(attendee_list)
    assert length != 0
    for attendee in attendee_list:
        index = attendee_list.index(attendee)
        if index < len(attendee_list) - 1 and attendee == attendee_list[index + 1]:
            while attendee == attendee_list[index + 1]:
                attendee_list.remove(attendee)
                # index = attendee_list.index(attendee)
    return attendee_list

def remove_duplicate_names_using_counts(attendee_list):
    '''Loop though all of the names in attendee_list and remove all of
       the duplicates.'''
    assert attendee_list != ''
    assert attendee_list != None
    length = len(attendee_list)
    assert length != 0
    attendee_counts = {}
    for attendee in attendee_list:
        if attendee in attendee_counts:
            attendee_counts[attendee] +=1 
        else:
            attendee_counts[attendee] = 1
    print(attendee_counts)
    
    for key in attendee_counts.keys():
        if attendee_counts[key] > 1:
            for i in range(attendee_counts[key] - 1):
                attendee_list.remove(key)
                
    #     index = attendee_list.index(attendee)
    #     if index < len(attendee_list) - 1 and attendee == attendee_list[index + 1]:
    #         attendee_list.remove(attendee)
    return attendee_list

def remove_duplicate_names_in_reverse(attendee_list):
    '''Start at the end of the list and remove all duplicate names as the
       the list is traversed from the end to the beginning.'''
    assert attendee_list != ''
    assert attendee_list != None
    assert len(attendee_list) != 0
    for index in range(len(attendee_list) - 1, 0, -1):
        # print(index)
        if attendee_list[index] == attendee_list[index - 1]:
            attendee_list.remove(attendee_list[index])
    return attendee_list


# def remove_duplicate_names(attendee_list):
#     for index in range(0, len(attendee_list) - 1):
#         if attendee_list[index] == attendee_list[index + 1]:
#             attendee_list.remove(attendee_list[index])
#     return

def remove_duplicate_names_second_array(attendee_list):
    '''Use a second array.  Only copy one copy of each name to the new array.
       This algorithm saves lots of time over other solutions, but the cost is a second
        array'''
    assert attendee_list != ''
    assert attendee_list != None
    assert len(attendee_list) != 0
    attendee_list_single_name = []
    for index in range(0, len(attendee_list) - 1):
        if attendee_list[index] != attendee_list[index + 1]:
            attendee_list_single_name.append(attendee_list[index])
    attendee_list_single_name.append(attendee_list[index + 1])
    return attendee_list_single_name

def main():
    '''Test driver - test all of the different functions.'''
    filename = get_filename()
    assert filename != ''
    attendee_list = read_file_data(filename)
    attendee_list2 = attendee_list.copy()
    attendee_list3 = attendee_list.copy()
    attendee_list_single_name = remove_duplicate_names_second_array(attendee_list)
    print(attendee_list_single_name)
    attendee_list_single_name = remove_duplicate_names(attendee_list)
    print(attendee_list_single_name)
    attendee_list_single_name = remove_duplicate_names_in_reverse(attendee_list2)
    print(attendee_list_single_name)
    attendee_list_single_name = remove_duplicate_names_using_counts(attendee_list3)
    print(attendee_list_single_name)

    write_file_data('WinterFinalSingleNames.json', attendee_list)


main()

