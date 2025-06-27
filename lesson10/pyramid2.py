

for num in range(1, 20, 2):
    # print('*' * num)
    print()
    print(' ' * ((20 - num) // 2) , end ='')
    for j in range(1, num):
        print('*', end='')