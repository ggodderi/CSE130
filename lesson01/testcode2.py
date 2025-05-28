name = 'Favorite Uncle Bob'
test_letter = 'o'
letter_found = False

# if test_letter in name:
#     print(f'The letter {test_letter} is in the name: {name}')
# else:
#     print('Letter not found in name.')


for letter in name:
    if letter == test_letter:
        letter_found = True

if letter_found:
    print(f'The letter {test_letter} is in the name: {name}')
else:
    print('Letter not found in name.')

letter_found = False
index = 0
while not letter_found and index < len(name):
    if letter == name[index]:
        letter_found = True
    index += 1

if letter_found:
    print(f'The letter {test_letter} is in the name: {name}')
else:
    print('Letter not found in name.')

