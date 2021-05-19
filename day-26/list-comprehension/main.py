# List Comprehension template
# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
name = "Angela"
letters_list = [letter for letter in name]
range_list = [num * 2 for num in range(1,5)]

# Conditional List Comprehension template
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Eleanor"]
short_names = [name.lower() for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) >= 5]


# List Comprehension 1
# Instructions
# You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain
# every number in the list numbers but each number should be squared.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]

print(squared_numbers)

# List Comprehension 2
# Instructions
# You are going to write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]

print(result)

# List Comprehension 3
# Instructions
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.

with open("file1.txt") as file1:
    list_file1 = [int(item) for item in file1.readlines()]

with open("file2.txt") as file2:
    list_file2 = [int(item) for item in file2.readlines()]


print(list_file1)
print(list_file2)

final_list = [num for num in list_file1 if num in list_file2]
print(final_list)