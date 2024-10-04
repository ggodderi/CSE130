# Python

# This program will implement the Final Example 1

import json

def read_file_data():
    '''Open a json file with a list of stock prices and return that data'''
    with open('Example1Input2.json') as file_handle:
        assert file_handle != None
        file_data = file_handle.read()
        assert file_data != None
        # print(file_data)
        json_data = json.loads(file_data)
        # print(json_data['stock_prices'])
    assert json_data != None
    assert type(json_data) == type({})
    return json_data['stock_prices']


def reverse_by_swap(data):
    length = len(data)
    assert length > 0

    length -= 1
    
    for index in range(len(data) // 2):
        data[index], data[length-index] = data[length-index], data[index]
    
    return data


def main():
    '''Obtain a list of stock prices, print that list, reverse the list, and reprint the list'''
    stock_prices = read_file_data()
    assert type(stock_prices) == type([])
    assert stock_prices != []
    assert len(stock_prices) > 0
    print(stock_prices)
    original_length = len(stock_prices)
    corrected_stock_prices = []

    stock_prices2 = stock_prices.copy()

    # Loop through the original list backwards and add it to the new list.
    # Pop/remove the item from the original list as we go.  
    # When done, the original list should be empty and the new list populated
    for index in range(len(stock_prices) - 1, -1, -1):
        assert 0 <= index <= len(stock_prices)
        corrected_stock_prices.append(stock_prices.pop(index))
        # print(stock_prices[index], end = ', ' )
    
    assert stock_prices == []
    assert len(stock_prices) == 0
    print(stock_prices)
    assert len(corrected_stock_prices) == original_length
    print(corrected_stock_prices)

    corrected_stock_prices = reverse_by_swap(stock_prices2)
    print(corrected_stock_prices)


main()

