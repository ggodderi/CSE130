name = 'Favorite uncle Bob'
search_letter = 'o'

letter_found = False

# if search_letter in name:
#     print(f'Found the letter: {search_letter} in: {name}')
# else:
#     print('Letter not found')


# for letter in name:
#     if search_letter == letter:
#         letter_found = True
#         break

# if letter_found:
#     print(f'Found the letter: {search_letter} in: {name}')
# else:
#     print('Letter not found')


found = False
index = 0
while not found and index < len(name):
    if search_letter == name[index]:
        letter_found = True
        found = True
    index += 1

if letter_found:
    print(f'Found the letter: {search_letter} in: {name}')
else:
    print('Letter not found')

