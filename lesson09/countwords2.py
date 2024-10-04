# Python

def receive_file_name():
    file_name = input('Input the file name for which you wish to count words: ')
    return file_name


def count_word_numbers(file_name):
    with open(file_name, 'rt') as file_handle:
        for line in file_handle:
            # print(line)
            line = line.strip()
            words = line.split(' ')

            words_dictionary = {}
            for word in words:
                if word in words_dictionary:
                    words_dictionary[word] += 1
                else:
                    words_dictionary[word] = 1
        return words_dictionary

def search_word_counts(word_counts):
    search_word = ''

    while search_word != 'q':
        search_word = input('What word do you wish to search for: (q to quit): ').lower()

        if search_word != 'q':
            if search_word in word_counts:
                print(word_counts[search_word])
            else:
                print(f'{search_word} No in word count dictionary')

def main():
    file_name = receive_file_name()
    # print(file_name)
    word_counts = count_word_numbers(file_name)

    # print(words_counts)

    search_word_counts(word_counts)

main()