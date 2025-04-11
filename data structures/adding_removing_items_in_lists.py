#to add the items in the list we use the methods such as
# append method to add the item in the end of the list
# insert method to add the item at any place or index in the list

numbers = list(range(6))
numbers.append(10)
numbers.insert(2,22)

print(numbers)

# to remove the items in the list we use the following methods
# pop method is used to remove the item at the last of the list if the index is not specified
# remove method is used to remove a specific item in the list by giving its value in the method
# del is a function used to delete multiple items in the list, we can also specify the starting index as well
# as the last index to be deleted
# clear is the method used to delete all the items in the list
numbers.pop()
numbers.pop(2)
numbers.remove(4)
print(numbers)

del numbers[0:3]
print(numbers)

numbers.clear()
print(numbers)
