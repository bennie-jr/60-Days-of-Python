# Bug - Fixing Exercise 1
# The following get_maximum function is designed to return the maximum value
# of the celsius list, while the last two lines of the code will convert the
# Celsius value to Fahrenheit and print it out.
#
#
# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)
#
# However, when running the code, the following error is generated:
#
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
#
# Try to fix the problem so that the last two lines can correctly get the
# maximal Celsius value from the function definition and convert that value
# to Fahrenheit.

# Fix
def get_maximum():
    celsius_local = [14, 15.1, 12.3]
    maximum = max(celsius_local)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(celsius)
print(fahrenheit)