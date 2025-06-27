# Python
# imports
import json
# This program will implement the power design for the weeks 12 and 13 of CSE 130

def load_data(file_name):
    '''Read the data from the filename and return the array element of the json data'''
    with open(file_name, 'rt') as file_handle:
        json_data = file_handle.read()
        dictionary_data = json.loads(json_data)
        return dictionary_data['array']
    
def get_power_in_sample(sample_size, data):
    '''Find the largest average sum from the data given a sample_size.
    Examine every sample_size sub segment of the data array.  Calculate its total.
    # Return a list of all of the totals and also the largest average total.'''
    # print(f'Data Length: {len(data)}')
    # print(sum(data))
    # print(data)
    if sample_size > len(data):
        print(f'Error:  Sample size: {sample_size}, is larger than data array: {len(data)}')
        return 0, 0
    assert type(sample_size) == int
    assert type(data) == list
    assert sample_size <= len(data)

    start_index = 0
    end_index = sample_size
    largest_average = 0
    totals = []
    while end_index <= len(data):
        assert end_index <= len(data)
        total = 0
        for i in range(start_index, end_index, 1):
            total += data[i]
        totals.append(total)
        if total > largest_average:
            largest_average = total
        end_index += 1
        start_index += 1

    assert len(totals) != 0
    assert len(totals) == len(data) - sample_size + 1
    assert type(largest_average) == type(data[0])
    return totals, largest_average

def obtain_file_name():
    '''Ask the user for the name of the file that contains the data.'''
    file_name = input('Please input the name of the data file: ')
    return file_name

def obtain_sample_size():
    '''Ask the user for the sample size - the size of the sub array that will be checked.'''

    sample_size = 0
    while sample_size <= 0:
        try:
            sample_size = int(input('Please input the sample size (int > 0): '))
        except (TypeError, ValueError):
            print('Incorrect input. ')
    
    return sample_size

def test_get_power_in_sample(file_name):
    '''Test every sample size associated with the data, plus 3 extra'''
    data = load_data(file_name)
    for i in range(len(data)+4):
        totals, largest_average = get_power_in_sample(i, data)
        print(largest_average)

def main():
    file_name = obtain_file_name()
    test_get_power_in_sample(file_name)
    sample_size = obtain_sample_size()
    data = load_data(file_name)
    print(data)
    totals, largest_average = get_power_in_sample(sample_size, data)
    print(totals, largest_average)

main()