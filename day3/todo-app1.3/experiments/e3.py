# Experiment 1 case-match

# todos = []
#
# while True:
#     user_action = input("Type add, show, or exit: ")
#     user_action = user_action.strip()   # strip action takes away unnecessary white spaces with strings
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case 'show':
#             for item in todos:
#                 print(item)
#         case 'exit':
#             break
#         case _:
#             print("You entered an unknown command. Try again")
# #         this case _ was added as an additional condition just in case the user input doesnt match the 3.
#
# print("Bye! See you later.")


# Experiment 2: Bitwise OR Operator

# todos = []
#
# while True:
#     user_action = input("Type add, show, or exit: ")
#     user_action = user_action.strip()   # strip action takes away unnecessary white spaces with strings
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case 'show' | 'display':
#             # the bitwise OR operator (|) was added to the conditional to match either show or display strings
#             for item in todos:
#                 print(item)
#         case 'exit':
#             break
#
# print("Bye! See you later.")


# Experiment 3: For-loop

todos = []

while True:
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip()   # strip action takes away unnecessary white spaces with strings

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        #   this experiment just shows you that you can add more line under the for loop
        case 'exit':
            break

print("Bye! See you later.")
