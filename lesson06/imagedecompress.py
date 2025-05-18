# Python

# This file will decompress simple binary images.
# The pattern is:  Data by Column.  First number is Number of filled blocks
# The second number is the number of emply blocks.
# The third number is the number of filled blocks.
# So it goes:  Filled, Empty, Filled, Empty, . . . .
# 0, 5 - This is a row of 5 empty block (because there were 0 filled)
# 3, 1, 1 - This is 3 filled, 1 empty, 1 filled

import json 

def read_data_from_file(filename):
    with open(filename, "rt") as filehandle:
        file_data = filehandle.read()
        json_data = json.loads(file_data)
        return json_data

def obtain_file_name():
    filename = input('Please input the filename: ')
    return filename

def create_emtpy_image(rows, columns):
    empty_image = []
    empty_row = [' '] * rows
    for column in range(columns):
        empty_image.append([' ']*rows)

    return empty_image



def main():
    filename = obtain_file_name()
    json_data = read_data_from_file(filename)
    print(json_data)

    empty_image = create_emtpy_image(json_data['num_rows'], json_data['num_columns'])
    print(empty_image)

main()