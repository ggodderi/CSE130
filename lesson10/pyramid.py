
for i in range(1, 20, 2):
    print()
    print(' ' * ((20 - i) // 2), end='')
    for j in range(1, i+1):
        print('*', end='')