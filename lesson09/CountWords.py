# Python

# This program will count the words of an input file.


def create_word_counts_dictionary(file_name):
    '''Receive the string of the file from read_file and then create a word count dictionary '''
   
    # Dictionary to hold the word counts <key, int>, i.e., <word, count>
    word_counts = {}

    # Open file and read line by line and add words to dicitionary
    with open(file_name, 'r') as file_handle:
        for line in file_handle:
            # line = line.strip()
            # line = line.lower()
            words = line.split()
            for word in words:
                assert word != ''

                # if word is already in the dictionary, just update its count
                if word in word_counts.keys():
                    word_counts[word] += 1
                else:
                    # else this word is not yet in the dictionary, add it and set count to 1
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

    print(f'There are {len(word_counts.keys())} unique words in {file_name}')

    # Allow the user to list all of the words and their counts
    list_words = input('Would you like to list all of the words (y/n)? ')

    if list_words.lower() == 'y':
        # This will also write the word counts to a file.
        with open(file_name+'wordcounts.txt', 'w') as file_handle:
            for key in word_counts.keys():
                value = word_counts[key]
                print(f'word: {key}: count: {value}')
                write_string = str(key) + ': ' +  str(value) + '\n'
                file_handle.write(write_string)

    # Allow the user to repeatedly search for words.    
    searched_word = ''
    while searched_word != 'q':
        searched_word = input(f'For which word do you wish to search the file{file_name} (q to quit)? ')

        searched_word = searched_word.lower()

        if searched_word in word_counts:
            print(f'There are {word_counts[searched_word]} occurances of the word: \'{searched_word}\' in the file: {file_name}')
        else:
            print(f'{searched_word} is not in the {file_name} document')


main()