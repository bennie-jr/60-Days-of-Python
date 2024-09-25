from bonus.coverters import convert
from bonus.parsers import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
results = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {results} meters")

if results < 1:
    print("Kid is too small")
else:
    print("Kid can ride the rollercoaster ")