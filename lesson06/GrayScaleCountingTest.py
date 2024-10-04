# Python

# Test Counting GrayScale pixels

import random

def count_white_pixel_rows(image_size):
    white_pixels = 0
    loop_count = 0
    number_of_rows_with_significant_white_pixels = 0

    for x in range(image_size):

        white_pixels = 0
        for y in range(image_size):
            pixel_value = random.randint(0, 255)
            loop_count += 1

            if pixel_value > 200:
                white_pixels += 1

            if white_pixels > image_size * 0.15:
                number_of_rows_with_significant_white_pixels += 1
                break
    return loop_count, number_of_rows_with_significant_white_pixels


image_sizes = [64, 128, 256, 512]

for image_size in image_sizes:
    loop_count, number_white_pixel_rows = count_white_pixel_rows(image_size)
    print(f'image size: {image_size}, loop count: {loop_count}, number of white rows: {number_white_pixel_rows}')



