# Python

def count_words_in_file(file_name):
    with open(file_name, 'rt') as file_handle:
        word_counts = {}
        for line in file_handle:
            # print(line)
            line = line.strip()
            word_list = line.split(' ')
            # print(word_list)
            for word in word_list:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

        # print(word_counts)
        return word_counts

def obtain_filename():
    file_name = input('Input the file name for which you wish to count words: ')
    return file_name

def search_word_counts(word_counts):
    search_word = ''

    while search_word != 'q':
        search_word = input('Input the word for which you wish to search: (q to quit) ')
        if search_word in word_counts:
            print(word_counts[search_word])
        else:
            print(f'{search_word} not in dictionary')

def main():
    file_name = obtain_filename()
    print(file_name)
    word_counts = count_words_in_file(file_name)

    # print(word_counts)

    search_word_counts(word_counts)

main()

