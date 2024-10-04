# Python

# Test iterators

my_iterator = iter(range(10))

print(type(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for n in my_iterator:
#     print(n)

# n = next(my_iterator)
# while n != -1:
#     print(n)
#     n = next(my_iterator)
   
n = next(my_iterator)
while n != StopIteration:
    print(n)
    try:
        n = next(my_iterator)
    except StopIteration:
        n = StopIteration
