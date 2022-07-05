# # Program to find the sum of all numbers stored in a list

# # List of numbers
# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# # variable to store the sum
# sum = 0

# # iterate over the list
# for val in numbers:
#     sum = sum+val

# print("The sum is", sum)
# print(range(10)) #range(0, 10)
# print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(2, 8))) #[2, 3, 4, 5, 6, 7]
# print(list(range(2, 20, 3))) #[2, 5, 8, 11, 14, 17]

# program to iterate through a list using index
from unicodedata import digit


animals = ['gorilla', 'fish', 'goat', 'dog']

for i in range(len(animals)):
    print('i love', animals[i])

digits = [1,2,3,4]
for i in digits:
    print(i)
else:
    print('no items found');

# program to display student's marks from record

student_name = 'Tobi'

marks = {'james': 30, 'fola': 70, "john": 76}

for i in marks:
    if student_name == marks:
        print(i)
        break
else:
    print('Not found in the list')
