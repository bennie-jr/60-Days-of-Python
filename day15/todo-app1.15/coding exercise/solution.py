import random

# Get two numbers from the user and covert them to integers
first_choice = int(input("Enter the lower bound: "))
second_choice = int(input("Enter the upper bound: "))

# Pick a random int using randint()
random_value = random.randint(first_choice,second_choice)
print(random_value)