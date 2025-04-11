n = input("Enter the number of times you want attempt: ")
if not n.isdigit():
    raise ValueError("Please enter a numeric value.")
n = int(n)

for numbers in range(1, n + 1):
    print("attempt", numbers, numbers * ".")
    print("successfull")
    break
else:
    print("Unsuccessful Attempt")
