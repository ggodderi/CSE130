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
    '''Read the data from the file whose name is filename.
    convert that data from json to a dictionary and return it.'''
    with open(filename, "rt") as filehandle:
        file_data = filehandle.read()
        json_data = json.loads(file_data)
        return json_data

def obtain_file_name():
    '''Get the compressed image filename from the user.'''
    filename = input('Please input the filename: ')
    return filename

def create_emtpy_image(rows, columns):
    '''Create an empty image with the given number for rows and columns.'''
    empty_image = []

    # Create a new column with an space at each row.
    for column in range(columns):
        empty_image.append([' ']*rows)

    return empty_image


def decompress_image(columns, compressed_image, decompressed_image):
    '''Given the columns, compressed_image, and the decompressed image, 
    Decompress the data into the decompressed_image'''

    # Go through all of the compressed image data for each column
    for column in range(columns):
        # print(compressed_data[column])

        # count is used to switch between On and Off data
        count = 0  

        # Keep track of which row is currently being decompressed
        row = 0  

        # For each compressed data in the data, decompress it.
        for d in compressed_image[column]:
            # print(d)          

            # Switch the ON/OFF character based upon whether this is a On or Off bit.
            if not count % 2:
                output_character = '*'
            else:
                output_character = ' '
            count += 1

            # Process the number of compressed bits.
            for r in range(d):
                # print(column, row, output_character)
                decompressed_image[column][row] = output_character
                # print(empty_image[column][row])
                row += 1


def display_image(rows, image_data):
    '''Display the image.  Do so by printing the row entry for each of the columns.  I.e., go 
    through each row on at a time.'''

    for row in range(rows):
        for column in image_data:
            print(column[row], end = ' ')
        print()

def main():
    filename = obtain_file_name()
    json_data = read_data_from_file(filename)
    # print(json_data)

    number_rows = json_data['num_rows']
    number_columns = json_data['num_columns']
    image_data = json_data['data']

    decompressed_image = create_emtpy_image(number_rows, number_columns)
    # empty_image[0][1] = 'A'
    # print(empty_image)

    decompress_image(number_columns, image_data, decompressed_image)
    # print(empty_image)
    display_image(number_rows, decompressed_image)
main()