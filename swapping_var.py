'''
y = int(input("Enter an integer for y:"))
x = int(input("Enter an integer for x:"))
dec = input("Do you want swap the variables. Answer in yes\no:").strip().lower()

if dec == "yes":
    a = y
    y = x
    x = a
    print(f"x = {x}")
    print(f" y = {y}")
    '''
    
# other way of executing the above logic is
# it i basically creating a tuple and unpacking it to assign the values to the variables
x = 10
y = 20

x,y = y,x

print(f"x = {x} and y = {y}")