# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)
print(range(10)) #range(0, 10)
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(2, 8))) #[2, 3, 4, 5, 6, 7]
print(list(range(2, 20, 3))) #[2, 5, 8, 11, 14, 17]
