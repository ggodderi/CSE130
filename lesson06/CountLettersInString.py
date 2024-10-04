# # Python
import string

# import string

# alphabet = string.ascii_lowercase
# alphabet_dict = {letter: ord(letter) for letter in alphabet}
# print(alphabet_dict)


# list_of_words = ['Charlie', 'Bob', 'Bubba', 'Lisa', 'Lilly', 'Mike', 'Nancy']

# search_letter = 'a'
# number_of_letters = 0
# number_of_searches = 0

# for word in list_of_words:
#     for letter in word:
#         number_of_searches += 1
#         if letter == search_letter:
#             number_of_letters += 1
        
    
# print(f'The number of {search_letter} letters is: {number_of_letters}.  It took {number_of_searches} to count them')

def count_letters_in_string_dictionary(stringToSearch):
    # alphabet = string.ascii_lowercase
    # letter_counts = {letter : 0 for letter in alphabet}
    # print(letter_counts)
    letter_counts = {}
    for letter in stringToSearch:
        if letter.lower() in letter_counts:
            letter_counts[letter.lower()] += 1
        else:
            letter_counts[letter] = 1

    return letter_counts

def count_letters_in_string(stringToSearch):
    alphabet = string.ascii_lowercase

    letter_counts = {}

    for letter in alphabet:
        for l in stringToSearch:
            if letter == l:
                if letter 
    print(alphabet)
    # print(letter_counts)
    # for letter in stringToSearch:
    #     letter_counts[letter] += 1

    # return letter_counts




def main():
    letter_counts = count_letters_in_string_dictionary("This is a test string")
    print(letter_counts)

    letter_counts = count_letters_in_string('This is a test string')
    print(letter_counts)


main()