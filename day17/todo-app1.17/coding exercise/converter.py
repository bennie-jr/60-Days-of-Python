def convert_meters(feet, inches):
    feet = float(feet)
    inches = float(inches)
    meters = feet * 0.3048 + inches * 0.0254
    return meters


if __name__ == "__main__":
    convert_meters(3,4)