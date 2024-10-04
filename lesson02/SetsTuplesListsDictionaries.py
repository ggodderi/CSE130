# Python

# This file will test sets, tuples, lists, and dictionaries


test_set = {'Apple', 'Cherry', 'Banana'}

print(test_set)
test_set.add('Orange')
print(test_set)
test_set.add('Grape')
print(test_set)
test_set.

test_tuple = (1, 2, 3, 4)

print(test_tuple, test_tuple[3])

test_list = ['Apple', 'Cherry', 'Banana']
print(test_list)
test_list.append('Cherry')
print(test_list)
print(test_list[3])

test_dictionary = {'brand' : 'Ford', 'model' : 'Mustang', 'year' : 1964}

print(test_dictionary)
print(test_dictionary['year'])
test_dictionary['brand'] = 'Chevy'
print(test_dictionary)
test_dictionary['age'] = 100
print(test_dictionary)
test_dictionary[10] = 'This is a test element'
print(test_dictionary)
item = test_dictionary.pop(10)
print(item)
print(test_dictionary)
