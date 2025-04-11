try:
    age = int(input('What is your age:'))
    message = "Adult" if age >= 21 else "minor"
    print(message)
except ValueError:
    print("Invalid value. Please enter a numeric value.")