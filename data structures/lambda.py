# lamda is a annonymous function which uses the parameter:expression format
# that lambda parameter:expression

items = [ ("item1", 10), ("item2", 12), ("item3", 8) ]

items.sort(key = lambda item:item[1])
print(items)
