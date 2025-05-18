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
    for column in range(columns):
        empty_image.append([' ']*rows)

    return empty_image


def decompress_image(rows, columns, compressed_data, empty_image):
    for column in range(columns):
        print(compressed_data[column])
        # output_character = '*'
        count = 0
        row = 0  
        for d in compressed_data[column]:
            print(d)          
            if not count % 2:
                output_character = '*'
            else:
                output_character = ' '
            count += 1
            for r in range(d):
                print(column, row, output_character)
                empty_image[column][row] = output_character
                print(empty_image[column][row])
                row += 1

    
    print(empty_image)

def display_image(rows, columns, image_data):
    for row in range(rows):
        for column in image_data:
            print(column[row], end = ' ')
        print()

def main():
    filename = obtain_file_name()
    json_data = read_data_from_file(filename)
    print(json_data)

    number_rows = json_data['num_rows']
    number_columns = json_data['num_columns']
    image_data = json_data['data']

    empty_image = create_emtpy_image(number_rows, number_columns)
    # empty_image[0][1] = 'A'
    print(empty_image)

    decompress_image(number_rows, number_columns, image_data, empty_image)
    print(empty_image)
    display_image(number_rows, number_columns, empty_image)
main()