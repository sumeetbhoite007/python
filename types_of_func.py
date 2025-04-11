# there are two types of functions
# 1 - Which performs the tassk
# 2- which returns a value

def get_greetings(name):
    return f"Hi {name}"

message = get_greetings("Sumeet")
file = open("F:/python/test/Greetings.txt", "w")
file.write(message)