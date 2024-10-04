# Python

# Test Counting GrayScale pixels

import random

# Pick varying image sizes
image_sizes = [4, 8, 16, 32, 64, 128, 256, 512]

# Check each image size for rows with signficant white pixels
for image_size in image_sizes:
    white_pixels = 0
    loop_count = 0
    number_of_rows_with_significant_white_pixels = 0

    # Check the entire image
    for x in range(image_size):
        white_pixels = 0
        for y in range(image_size):

            # Pick a random pixel value
            pixel_value = random.randint(0, 255)
            loop_count += 1

            # Pixel value > 210 is mostly white
            if pixel_value > 210:
                white_pixels += 1

            # A row with 15% or more white pixels is considered significantly white row
            if white_pixels > image_size * 0.15:
                number_of_rows_with_significant_white_pixels += 1
                break

    # Print out the number of rows in this image.
    print(f'image size: {image_size}, loop count: {loop_count}, number of white rows: {number_of_rows_with_significant_white_pixels}')



