# Python

# This file will solve the spring final, which is:
# Steve is a teacher and has given each of his students an ID number from 1 to N where there are N students in 
# his class. Every day, he has his students stand in line and turn in their homework according to their ID number. 
# On occasion, Steve notices that a student is missing. The problem is, which one… 
# Assignment Definition
# You are given an array of size n with the range of numbers from 1 to n+1. This array has no duplicates, one 
# number is missing, and the array is not sorted. Find the missing number. Of course, we want this design to be 
# as efficient as possible

data = [3, 9, 1, 20, 21, 19, 17, 7, 4, 2, 15, 13, 18, 16, 5, 6, 12, 8, 10, 14, 20]
n = 21
student_in_attendance = [False] * 21

print(student_in_attendance)

for i in data:
    student_in_attendance[i-1] = True

print(student_in_attendance)
for i in range(len(student_in_attendance)):
    if not student_in_attendance[i]:
        print(f'Student {i+1} is not present.')