# Python

# This program will count the words of an input file.

import re
def remove_sym(s):
    """ Remove symbols in a string """
    return re.sub(r'[^\w|\s]', '', s)


def read_file(file_name):
    '''Open the file specified by file_name and return the string of the entire file'''
    assert file_name != ''
    data = ''
    with open(file_name, 'r') as file_handle:
        data = file_handle.read()
    
    assert len(data) > 0
    return data


def create_word_counts_dictionary(file_name):
    '''Receive the string of the file from read_file and then create a word count dictionary '''
    # file_text = read_file('DeclarationOfIndepdence.txt')

    # # Get the string of the file
    # file_text = read_file(file_name)
    # file_text = file_text.strip()
    # file_text = file_text.strip('\r')
    # file_text = file_text.strip('\n')
    # file_text = file_text.lower()
    # file_text = remove_sym(file_text)

    # with open(file_name + 'NoPunc.txt', "w") as file_handle:
    #     file_handle.write(file_text)
    # with open(file_name + 'hexdump.txt', 'w') as file_handle:
    #     for letter in file_text:
    #         #print(letter)
    #         int_value = ord(letter)
    #         write_string = f'{letter}: {int_value}: {int_value:#x} \n'
    #         file_handle.write(write_string)

    # word_counts = {}
    # # Remove carriage returns and transform data to lower case


    # # Find the words
    # words = file_text.split(' ')
    # with open(file_name + 'debug.txt', 'w') as file_handle:
    #     for word in words:
    #         file_handle.write(word)

    word_counts = {}
    #print('Entering function:')
    file_handle_no_punch = open(file_name + 'nopunch.txt', 'w')
    with open(file_name, 'r') as file_handle:
        for line in file_handle:
            #print(line)
            line = remove_sym(line)
            line = line.strip()
            line = line.lower()
            words = line.split()
            file_handle_no_punch.write(line)
            file_handle_no_punch.write(' ')
            for word in words:
            #assert word != ''
                if word in word_counts.keys():
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
        
    assert word_counts != {}
    return word_counts

def obtain_file_name():
    file_name = input('What is the file name of the text file? ')
    return file_name

def main():
    '''Main routine - get the word count dictionary and allow user to search for words'''
    file_name = obtain_file_name()
    word_counts = create_word_counts_dictionary(file_name)
    #print(word_counts)

    print(f'There are {len(word_counts.keys())} unique words in {file_name}')

    list_words = input('Would you like to list all of the words (y/n)? ')

    if list_words.lower() == 'y':
        with open(file_name+'wordcounts.txt', 'w') as file_handle:
            for key in word_counts.keys():
                value = word_counts[key]
                print(f'word: {key}: count: {value}')
                write_string = str(key) + ': ' +  str(value) + '\n'
                file_handle.write(write_string)

    searched_word = ''
    while searched_word != 'q':
        searched_word = input(f'For which word do you wish to search the file{file_name} (q to quit)? ')

        searched_word = searched_word.lower()

        if searched_word in word_counts:
            print(f'There are {word_counts[searched_word]} occurances of the word: \'{searched_word}\' in the file: {file_name}')
        else:
            print(f'{searched_word} is not in the {file_name} document')


main()