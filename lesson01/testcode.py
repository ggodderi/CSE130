# Python test

# test python in command (membership test)

name = 'Uncle Bob'

letter = 'z'

# # Test if the letter is in the name using in
# if letter in name:
#     print(f'{letter} is in: {name}')
# else:
#     print(f'{letter} is NOT in: {name}')

# # Tset if the letter is in the name using a for loop
# letter_found = False
# for l in name:
#     if l == letter:
#         letter_found = True

# if letter_found:
#     print(f'{letter} is in: {name}')
# else:
#     print(f'{letter} is NOT in: {name}')

# Test if the letter is in the name using a while loop
letter_found = False
index = 0
while not letter_found and index < len(name):
    if letter == name[index]:
        letter_found = True
    index += 1

if letter_found:
    print(f'{letter} is in: {name}')
else:
    print(f'{letter} is NOT in: {name}')


 