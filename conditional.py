try:
    temperature = int(input("What is the temperature today? "))
    if temperature > 30:
        print("It's warm. Drink plenty of water.")
    elif temperature > 10 and temperature < 30:
        print("It's pleasant today.")
    else:
        print("It's cold today.")
except ValueError:
    print("Invalid input! Please enter a numeric value for the temperature.")
