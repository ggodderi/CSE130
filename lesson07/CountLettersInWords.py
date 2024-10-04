# Python

list_of_words = ['Charlie', 'Bob', 'Bubba', 'Lisa', 'Lilly', 'Mike', 'Nancy']

search_letter = 'a'
number_of_letters = 0
number_of_searches = 0

for word in list_of_words:
    for letter in word:
        number_of_searches += 1
        if letter == search_letter:
            number_of_letters += 1
        
    
print(f'The number of {search_letter} letters is: {number_of_letters}.  It took {number_of_searches} to count them')