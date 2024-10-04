# Python

print('Hello World')
print(f'I was born in {1971}')

name = input('Please input your name: ')
print(f'Your name is: {name}')


with open('lesson02problem.txt', 'w') as file_handle:
    file_handle.write(name)

with open('lesson02problem.txt', 'r') as file_handle:
    read_in_name = file_handle.read()
    print(f'Your name is: {read_in_name}')


alpha_charcter = '\u03B1'
print(alpha_charcter)
beta_charcter = '\u03B2'
print(beta_charcter)