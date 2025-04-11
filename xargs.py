# in xargs we use * which uses the tuples for the arguement inputs


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(9,8,7,5))