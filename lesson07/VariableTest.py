# Python
odd = 0
even = 0

for count in range (1, 4):
    if count % 2 == 0:
        even += 1
    else:
        odd += 1
    

print(even, odd)