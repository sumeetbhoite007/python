# problem statment - Find the most repeated character in the sentence
sent = "This is the most common interview question."
 
character = [*sent.lower().replace(" ", "")]
#print(character)
char_count = {}

for char in character:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

max_char = max(char_count, key = char_count.get)

print(f" the highest repeated character is {max_char} ")

