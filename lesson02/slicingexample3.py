alphabet = 'ABCDEFGHIJKL        MNOPQRSTUVWXYZ'

print(alphabet)
print(alphabet[:5])
print(alphabet[0:5])

print(alphabet[10:15])
print(alphabet[20:])

print('15 - 10')
print(alphabet[15:10])

print(alphabet[-9:-3])

my_slice = alphabet[11:]

my_slice += 'Hey Bob'
print(my_slice)
print(alphabet)
