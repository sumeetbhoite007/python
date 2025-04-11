letters = ("a", "b", "c")
for letter in letters:
    print(letter)
    
for index, items in enumerate(letters): #enumerate is a function which creates a tuple value (key, value - pair),
                                        # hence it gives the index values as well assigned to the value.
    print(index, items)