

PYRAMID_HEIGHT = 40

for num in range(1, PYRAMID_HEIGHT, 2):
    # print('*' * num)
    print()
    print(' ' * ((PYRAMID_HEIGHT - num) // 2) , end ='')
    for j in range(1, num+1):
        print('*', end='')