### problem statement - develop an algorithm where if the number is divisible by 3 return fizz, if divisible by 5
# return buzz, if divisible by both return fizzbuzz and if not divisible by both return the number.

def fizz_buzz(number):
    if (number%3 == 0) and (number%5 == 0):
        return "fizzbuzz"
    elif number%3 == 0:
        return "fizz"
    elif number%5 == 0:
        return "buzz"
    else:
        return number
    
number = int(input("Please enter the number:"))
print(fizz_buzz(number))