# Bug - Fixing Exercise 1
# The code below tries to write the items of temperatures each
# in one line in the file.txt list.However, the code has an error.
# Try to fix the error.
#
# temperatures = [10, 12, 14]
#
# file = open("file.txt", 'w')
#
# file.writelines(temperatures)

# # Fix
temperatures = [10, 12, 14]
temperatures = [str(i) + '\n' for i in temperatures]
file = open("file.txt", 'w')

file.writelines(temperatures)




# Bug-Fixing Exercise 2
# The code below tries to convert all the numbers to integers. However, the code has an error. Try to fix the error.
#
# numbers = [10.1, 12.3, 14.7]
# numbers = [int(number) for item in numbers]
# print(numbers)

# Fix
# numbers = [10.1, 12.3, 14.7]
# numbers = [int(item) for item in numbers]
# print(numbers)